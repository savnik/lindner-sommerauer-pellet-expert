"""Unit tests for graddage.py (offline parts) and degree days in logbog.py forbrug.

  python3 -m unittest discover -s evals/unit
"""

import contextlib
import io
import json
import os
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "plugins/pellet-expert/skills/logbog/scripts"))
import graddage  # noqa: E402
import logbog  # noqa: E402
from test_logbog import LEVEL_HEADER, Series  # noqa: E402

CSV = """# source: test
# cell: 10km_617_72
date,degree_days,qc_status
2025-01-05,10,manual
2025-01-06,10,manual
2025-01-07,12,manual
2025-01-08,12,manual
2025-01-09,14,manual
2025-01-10,14,none
2025-01-11,8,none
2025-01-12,8,none
"""


class Cell(unittest.TestCase):
    def test_utm_cell_matches_dmi_grid(self):
        # A point in central Copenhagen lies in DMI's cell 10km_617_72.
        self.assertEqual(graddage.cell_id(55.676, 12.568), "10km_617_72")

    def test_position_parsing(self):
        self.assertEqual(graddage.parse_position("55,68; 12,57"), (55.68, 12.57))
        self.assertEqual(graddage.parse_position(" 55.68, 12.57 "), (55.68, 12.57))
        with self.assertRaises(ValueError):
            graddage.parse_position("48.8, 2.3")   # not in Denmark
        with self.assertRaises(ValueError):
            graddage.parse_position("somewhere")

    def test_postcode_found_locally(self):
        self.assertEqual(graddage.postcode_of("Testvej 12b, 2800 Testby"), "2800")
        self.assertEqual(graddage.postcode_of("Testvej 1234, 8000 Testby C"), "8000")
        self.assertIsNone(graddage.postcode_of("Testvej 12"))

    def test_address_sends_only_postcode(self):
        sent = []
        orig = graddage.postcode_centre
        graddage.postcode_centre = lambda code: (sent.append(code), (55.676, 12.568))[1]
        try:
            self.assertEqual(graddage.cell_from_address("Testvej 12b, 2800 Testby"), ("10km_617_72", "2800"))
        finally:
            graddage.postcode_centre = orig
        self.assertEqual(sent, ["2800"])

    def test_setup_stores_only_the_cell(self):
        with tempfile.TemporaryDirectory() as d:
            cfg = os.path.join(d, "graddage.json")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(graddage.main(["--config", cfg, "opsæt", "--lat", "55.676", "--lon", "12.568"]), 0)
            text = open(cfg, encoding="utf-8").read()
            self.assertEqual(json.loads(text)["cell"], "10km_617_72")
            self.assertNotIn("55.676", text)
            self.assertNotIn("12.568", text)

    def test_fetch_without_config_and_terminal_stops(self):
        with tempfile.TemporaryDirectory() as d, \
                contextlib.redirect_stderr(io.StringIO()), \
                open(os.devnull) as null:
            old = sys.stdin
            sys.stdin = null
            try:
                self.assertEqual(graddage.main(["--config", os.path.join(d, "x.json"), "hent"]), 3)
            finally:
                sys.stdin = old


class DegreeDays(Series):
    def forbrug_dd(self, rows=None):
        path = self.tmp / "gd.csv"
        path.write_text(CSV, encoding="utf-8")
        text = self.level_text(rows or self.ROWS)
        lb_path = self.tmp / "logbook.md"
        lb_path.write_text(text, encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = logbog.main(["forbrug", str(lb_path), "--per", "interval", "--graddage", str(path), "--json"])
        return code, json.loads(out.getvalue())

    def test_degree_days_spread_over_hours(self):
        _, res = self.forbrug_dd()
        first = res["burner_steps"][0]   # 2025-01-05 15:00 -> 01-07 15:00
        self.assertEqual(first["degree_days"], 10 * 9 / 24 + 10 + 12 * 15 / 24)
        self.assertEqual(first["burner_hours"], 4)

    def test_preliminary_weather_flag(self):
        _, res = self.forbrug_dd()
        self.assertFalse(res["burner_steps"][0]["preliminary_weather"])
        self.assertTrue(res["burner_steps"][-1]["preliminary_weather"])

    def test_burner_steps_include_counter_only_rows(self):
        _, res = self.forbrug_dd()
        self.assertIn("2025-01-08T15:00", [s["to"] for s in res["burner_steps"]])
        self.assertEqual(res["burner_steps"][1]["burner_hours_per_day"], 2)

    def test_fits_with_degree_days(self):
        _, res = self.forbrug_dd()
        self.assertIsNotNone(res["fit"]["burner_hours_per_degree_day"]["slope"])
        self.assertIsNotNone(res["fit"]["burner_hours_per_day"]["slope"])

    def test_missing_day_gives_none(self):
        global CSV
        old = CSV
        CSV = CSV.replace("2025-01-09,14,manual\n", "")
        try:
            _, res = self.forbrug_dd()
        finally:
            CSV = old
        step = next(s for s in res["burner_steps"] if s["to"] == "2025-01-10T15:00")
        self.assertIsNone(step["degree_days"])

    def test_no_degree_days_without_file(self):
        _, res = self.forbrug()
        self.assertNotIn("degree_days", res["burner_steps"][0])
        self.assertNotIn("burner_hours_per_degree_day", res["fit"])


if __name__ == "__main__":
    unittest.main()
