"""Unit tests for skills/logbog/scripts/logbog.py, on a fictional fixture.

  python3 -m unittest discover -s evals/unit
"""

import contextlib
import io
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "plugins/pellet-expert/skills/logbog/scripts"))
import logbog  # noqa: E402

FIXTURE = ROOT / "evals/fixtures/logbog-example.md"
TEMPLATE = ROOT / "plugins/pellet-expert/skills/logbog/templates/logbog.md"
TODAY = "2025-11-15"


def run(*argv, text=None, tmp=None):
    """Run the CLI; return (exit code, parsed JSON)."""
    path = FIXTURE
    if text is not None:
        path = tmp / "logbook.md"
        path.write_text(text, encoding="utf-8")
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = logbog.main([argv[0], str(path), *argv[1:], "--json"])
    return code, json.loads(out.getvalue())


class Base(unittest.TestCase):
    def setUp(self):
        import tempfile
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = pathlib.Path(self._tmp.name)
        self.text = FIXTURE.read_text(encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def with_row(self, after_header_of, row):
        """Append a row to the end of a section's table."""
        lines = self.text.splitlines()
        i = next(n for n, l in enumerate(lines) if l.strip() == f"## {after_header_of}")
        j = i + 1
        while j < len(lines) and not lines[j].startswith("|"):
            j += 1
        while j < len(lines) and lines[j].startswith("|"):
            j += 1
        lines.insert(j, row)
        return "\n".join(lines) + "\n"


class Parsing(unittest.TestCase):
    def test_hours_formats(self):
        self.assertAlmostEqual(logbog.parse_hours("12345h26"), 12345 + 26 / 60)
        self.assertAlmostEqual(logbog.parse_hours("87:30"), 87.5)
        self.assertAlmostEqual(logbog.parse_hours("12,5"), 12.5)
        self.assertIsNone(logbog.parse_hours(""))
        with self.assertRaises(ValueError):
            logbog.parse_hours("10h75")

    def test_interval_syntax(self):
        self.assertEqual(logbog.parse_interval("12 mo"), {"months": 12})
        self.assertEqual(logbog.parse_interval("3 y"), {"months": 36})
        self.assertEqual(logbog.parse_interval("1 w"), {"days": 7})
        self.assertEqual(logbog.parse_interval("12 mo | 2000 h"), {"months": 12, "hours": 2000})
        self.assertEqual(logbog.parse_interval("-"), {})
        self.assertIsNone(logbog.parse_interval("yearly"))


class Validate(Base):
    def test_fixture_is_valid(self):
        code, res = run("validate", "--today", TODAY)
        self.assertEqual(code, 0, res["errors"])
        self.assertEqual(res["errors"], [])

    def test_empty_template_is_valid(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = logbog.main(["validate", str(TEMPLATE), "--json", "--today", TODAY])
        self.assertEqual(code, 0, out.getvalue())

    def test_template_row_with_pellet_product_is_valid(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        header = ("| Date | Time | Betrieb-STD | Aschenlade aktuell | Pellets added (kg) | Sacks | Since "
                  "| Level after | Level (sacks) | Level before fill (sacks) | Pellet product | Event "
                  "| Source | Note |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        self.assertIn(header, text)
        text = text.replace(header, header + "| 2025-11-01 | | | | 90 | | | full | | | Brand X premium | | O | |\n")
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertEqual(code, 0, res["errors"])
        self.assertEqual(res["counts"]["readings"], 1)

    def test_level_needs_sack_size(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        text = text.replace("|---|---|---|---|---|---|---|---|---|---|---|---|---|\n",
                            "|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
                            "| 2025-11-01 | | | | | | | | 20 | | | | D | |\n", 1)
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertEqual(code, 1)
        self.assertTrue(any("Sack size" in e["message"] for e in res["errors"]))

    def test_inferred_row_is_ignored(self):
        code, res = run("validate", "--today", TODAY)
        self.assertEqual(res["counts"]["readings"], 8)  # the I row is not counted
        self.assertTrue(any("source I" in w["message"] for w in res["warnings"]))

    def test_name_in_by_is_an_error(self):
        text = self.with_row("Service done",
                             "| 2025-11-12 | WT | cleaned | | | ok | Hansen VVS | P | |")
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertEqual(code, 1)
        self.assertTrue(any("no names" in e["message"] for e in res["errors"]))

    def test_prediction_cannot_lengthen_manual_interval(self):
        text = self.with_row("Service plan",
                             "| SAUGZUG | Saugzug | time | 18 mo | Predictive | 2025-11-01 | |")
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertEqual(code, 1)
        self.assertTrue(any("ceiling" in e["message"] for e in res["errors"]))

    def test_shorter_owner_interval_is_allowed(self):
        code, res = run("validate", "--today", TODAY)  # the fixture's WT 6 mo row
        self.assertFalse(any("WT" in e["message"] for e in res["errors"]))

    def test_lengthening_trvb_is_only_a_warning(self):
        text = self.with_row("Service plan",
                             "| SICHT | Sicht | time | 2 w | Owner | 2025-11-01 | |")
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertEqual(res["errors"], [])
        self.assertTrue(any("TRVB interval" in w["message"] for w in res["warnings"]))

    def test_counter_decrease_without_reset_is_an_error(self):
        text = self.with_row("Readings", "| 2025-10-01 | 200h00 | | | | | | | D | |")
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertTrue(any("without a 'reset Betrieb-STD'" in e["message"] for e in res["errors"]))

    def test_duplicate_plan_row_is_an_error(self):
        text = self.with_row("Service plan",
                             "| WT | Wärmetauscher | time | 6 mo | Owner | 2025-10-01 | again |")
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertTrue(any("already has a row" in e["message"] for e in res["errors"]))

    def test_bad_source_is_an_error(self):
        text = self.with_row("Readings", "| 2025-10-01 | 310h00 | | | | | | | X | |")
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertTrue(any("Source 'X'" in e["message"] for e in res["errors"]))

    def test_identifier_warning(self):
        text = self.with_row("Service done",
                             "| 2025-11-12 | WT | cleaned | | | ok | technician | P | call +45 12 34 56 78 |")
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertTrue(any("phone" in w["message"] for w in res["warnings"]))

    def test_dates_in_note_are_not_phone_numbers(self):
        text = self.with_row("Service done",
                             "| 2025-11-12 | WT | cleaned | | | ok | owner | O | corrects the row 2025-02-11 |")
        code, res = run("validate", "--today", TODAY, text=text, tmp=self.tmp)
        self.assertFalse(any("phone" in w["message"] for w in res["warnings"]))

    def test_anchor_numbers_are_not_identifiers(self):
        code, res = run("validate", "--today", TODAY)
        self.assertFalse(any("phone" in w["message"] for w in res["warnings"]))

    def test_errors_block_arithmetic(self):
        text = self.with_row("Service done",
                             "| 2025-11-12 | WT | cleaned | | | ok | Hansen VVS | P | |")
        code, res = run("forbrug", text=text, tmp=self.tmp)
        self.assertEqual(code, 1)
        self.assertIn("refused", res)


class Consumption(Base):
    def setUp(self):
        super().setUp()
        _, self.res = run("forbrug", "--per", "season")
        self.iv = {r["to"]: r for r in self.res["intervals"]}

    def test_exact_interval(self):
        r = self.iv["2025-01-19"]
        self.assertTrue(r["exact"])
        self.assertEqual((r["days"], r["kg"], r["hours"], r["kg_per_hour"]), (14, 150, 100, 1.5))

    def test_sacks_converted(self):
        self.assertEqual(self.iv["2025-02-02"]["kg"], 150)

    def test_ash_reset_does_not_break_betrieb_std(self):
        self.assertEqual(self.iv["2025-03-02"]["hours"], 80)

    def test_level_differs_is_approximate(self):
        self.assertFalse(self.iv["2025-03-02"]["exact"])

    def test_reset_without_value_is_a_gap(self):
        self.assertIsNone(self.iv["2025-03-16"]["hours"])
        self.assertIsNone(self.iv["2025-03-30"]["hours"])  # same level, but spans the gap
        self.assertTrue(self.iv["2025-03-30"]["exact"])

    def test_since_period(self):
        r = self.iv["2025-09-01"]
        self.assertEqual((r["from"], r["days"], r["kg"], r["exact"]), ("2025-06-01", 92, 375, False))

    def test_inferred_fill_not_used(self):
        self.assertNotIn("2025-09-10", self.iv)

    def test_headline_uses_exact_only(self):
        s = self.res["summary"]
        self.assertEqual((s["kg_per_hour_median"], s["kg_per_hour_n"]), (1.5, 3))
        self.assertEqual(s["exact_intervals"], 4)

    def test_burner_hours_from_ash_counter(self):
        r = self.iv["2025-01-19"]
        self.assertEqual((r["burner_hours"], r["kg_per_burner_hour"]), (40, 3.75))

    def test_burner_hours_sum_across_ash_reset(self):
        # 140:00 read before the reset on 2025-02-16, then 30:00 on 2025-03-02
        self.assertEqual(self.iv["2025-03-02"]["burner_hours"], 30)
        self.assertEqual(self.iv["2025-02-16"]["burner_hours"], 40)

    def test_burner_hours_need_a_reading_at_both_fills(self):
        self.assertIsNone(self.iv["2025-03-16"]["burner_hours"])
        self.assertIsNone(self.iv["2025-03-30"]["burner_hours"])

    def test_ash_reset_without_value_is_a_gap(self):
        text = self.text.replace("| 2025-02-16 | 10300h00 | 140:00 |", "| 2025-02-16 | 10300h00 | |")
        _, res = run("forbrug", text=text, tmp=self.tmp)
        iv = {r["to"]: r for r in res["intervals"]}
        self.assertIsNone(iv["2025-03-02"]["burner_hours"])
        self.assertEqual(iv["2025-03-02"]["hours"], 80)

    def test_headline_kg_per_burner_hour(self):
        s = self.res["summary"]
        self.assertEqual((s["kg_per_burner_hour_median"], s["kg_per_burner_hour_n"]), (3.75, 3))

    def test_season_burner_hours(self):
        total = sum(p["burner_hours"] or 0 for p in self.res["periods"])
        self.assertAlmostEqual(total, 40 + 40 + 40 + 30 + 40 + 20, places=1)

    def test_season_totals_add_up(self):
        total = sum(p["kg"] for p in self.res["periods"])
        self.assertAlmostEqual(total, sum(r["kg"] for r in self.res["intervals"]), places=1)
        self.assertEqual([p["period"] for p in self.res["periods"]], ["2024/25", "2025/26"])



LEVEL_HEADER = ("| Date | Time | Betrieb-STD | Aschenlade aktuell | Pellets added (kg) | Sacks | Since "
                "| Level after | Level (sacks) | Level before fill (sacks) | Event | Source | Note |\n"
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")


class Series(Base):
    """Cumulative series from levels in sacks (fictional values, sack size 15 kg)."""

    ROWS = [
        "| 2025-01-05 | 15:00 | 10000h00 | 20:00 | | 10 | | mark | 30 | 20 | | D | |",
        "| 2025-01-07 | 15:00 | 10040h00 | 24:00 | | | | | 26 | | | D | |",
        "| 2025-01-08 | 15:00 | | 26:00 | | | | | | | | D | counters only |",
        "| 2025-01-10 | 15:00 | 10100h00 | 30:00 | | | | | 20 | | | D | |",
        "| 2025-01-12 | 03:00 | 10150h00 | 35:00 | | 10 | | mark | 28 | 18 | | D | |",
    ]

    def level_text(self, rows):
        lines = self.text.splitlines()
        i = next(n for n, l in enumerate(lines) if l.strip() == "## Readings")
        j = i + 1
        while not lines[j].startswith("|"):
            j += 1
        k = j
        while k < len(lines) and lines[k].startswith("|"):
            k += 1
        body = LEVEL_HEADER + "\n".join(rows)
        return "\n".join(lines[:j] + body.splitlines() + lines[k:]) + "\n"

    def forbrug(self, rows=None):
        return run("forbrug", "--per", "interval", text=self.level_text(rows or self.ROWS), tmp=self.tmp)

    def test_cumulative_kg_drops_fills(self):
        code, res = self.forbrug()
        self.assertEqual(code, 0)
        got = [(p["t"], p["kg"]) for p in res["series"]]
        self.assertEqual(got, [("2025-01-05T15:00", 0), ("2025-01-07T15:00", 60),
                               ("2025-01-08T15:00", None), ("2025-01-10T15:00", 150),
                               ("2025-01-12T03:00", 180)])

    def test_counters_start_at_zero_and_carry_time(self):
        _, res = self.forbrug()
        self.assertEqual([p["burner_hours"] for p in res["series"]], [0, 4, 6, 10, 15])
        self.assertEqual(res["series"][-1]["fill_kg"], 150)
        self.assertTrue(all(p["time_known"] for p in res["series"]))

    def test_steps_use_time_of_day(self):
        _, res = self.forbrug()
        last = res["steps"][-1]
        self.assertEqual((last["days"], last["kg"], last["kg_per_day"]), (1.5, 30, 20))
        mid = res["steps"][1]
        self.assertEqual((mid["burner_hours"], mid["kg_per_burner_hour"]), (6, 15))
        self.assertEqual((mid["hours"], mid["kg_per_hour"]), (60, 1.5))

    def test_fit_through_points(self):
        _, res = self.forbrug()
        f = res["fit"]["kg_per_burner_hour"]
        self.assertEqual(f["n_points"], 4)
        self.assertAlmostEqual(f["slope"], 12.33, places=2)

    def test_fit_needs_three_points(self):
        _, res = self.forbrug(self.ROWS[:2])
        self.assertIsNone(res["fit"]["kg_per_burner_hour"]["slope"])

    def test_fill_without_level_before_keeps_chain(self):
        rows = list(self.ROWS)
        rows[4] = "| 2025-01-12 | 03:00 | 10150h00 | 35:00 | | 10 | | mark | 28 | | | D | |"
        _, res = self.forbrug(rows)
        self.assertEqual(res["series"][-1]["kg"], 180)

    def test_missing_time_is_noon(self):
        rows = [r.replace("| 15:00 |", "| |") for r in self.ROWS]
        _, res = self.forbrug(rows)
        self.assertEqual(res["series"][0]["t"], "2025-01-05T12:00")
        self.assertFalse(res["series"][0]["time_known"])

    def test_bad_time_is_an_error(self):
        rows = list(self.ROWS)
        rows[1] = rows[1].replace("| 15:00 |", "| 25:00 |")
        code, res = run("validate", text=self.level_text(rows), tmp=self.tmp)
        self.assertEqual(code, 1)
        self.assertTrue(any("HH:MM" in e["message"] for e in res["errors"]))

    def test_headline_unchanged_by_levels(self):
        _, res = self.forbrug()
        self.assertEqual(res["summary"]["exact_intervals"], 1)

    def test_level_before_without_fill_is_an_error(self):
        rows = list(self.ROWS)
        rows[1] = "| 2025-01-07 | 15:00 | 10040h00 | 24:00 | | | | | 26 | 26 | | D | |"
        code, res = run("validate", text=self.level_text(rows), tmp=self.tmp)
        self.assertEqual(code, 1)
        self.assertTrue(any("without a fill" in e["message"] for e in res["errors"]))

    def test_fill_mismatch_warns(self):
        rows = list(self.ROWS)
        rows[4] = "| 2025-01-12 | 03:00 | 10150h00 | 35:00 | | 10 | | mark | 28 | 15 | | D | |"
        _, res = run("validate", text=self.level_text(rows), tmp=self.tmp)
        self.assertTrue(any("sacks were added" in w["message"] for w in res["warnings"]))

    def test_level_rise_without_fill_warns(self):
        rows = list(self.ROWS)
        rows[3] = "| 2025-01-10 | 15:00 | 10100h00 | 30:00 | | | | | 28 | | | D | |"
        _, v = run("validate", text=self.level_text(rows), tmp=self.tmp)
        self.assertTrue(any("without a fill" in w["message"] for w in v["warnings"]))

    def test_inferred_level_not_used(self):
        rows = list(self.ROWS)
        rows[1] = "| 2025-01-07 | 15:00 | | | | | | | 26 | | | I | |"
        _, res = self.forbrug(rows)
        self.assertNotIn("2025-01-07T15:00", [p["t"] for p in res["series"]])

    def test_logbook_without_level_columns_has_no_kg_series(self):
        _, res = run("forbrug")
        self.assertTrue(all(p["kg"] is None for p in res["series"]))
        self.assertEqual(res["steps"], [])


class Status(Base):
    def states(self, today):
        _, res = run("status", "--today", today)
        return {t["id"]: t for t in res["tasks"]}

    def test_classes(self):
        s = self.states(TODAY)
        self.assertEqual(s["SAUGZUG"]["state"], "ok")
        self.assertEqual(s["PUTZMECH"]["state"], "no record")
        self.assertEqual(s["RAUCHROHR"]["state"], "no interval")

    def test_due_soon_and_overdue(self):
        self.assertEqual(self.states("2025-12-01")["TRVB-MON"]["state"], "due soon")
        self.assertEqual(self.states("2025-12-05")["TRVB-MON"]["state"], "overdue")

    def test_valid_from_switches_plan_row(self):
        self.assertEqual(self.states("2025-09-15")["WT"]["due_date"], "2026-09-01")
        self.assertEqual(self.states(TODAY)["WT"]["due_date"], "2026-03-01")

    def test_month_end_arithmetic(self):
        self.assertEqual(logbog.add_interval(logbog.dt.date(2025, 1, 31), {"months": 1}),
                         logbog.dt.date(2025, 2, 28))

    def test_hours_trigger(self):
        t = self.states(TODAY)["LAMBDA"]
        self.assertEqual((t["due_at_betrieb_std"], t["hours_left"]), (1050, 750))

    def test_ash_counter_is_zero_after_reset(self):
        text = self.with_row("Readings", "| 2025-11-10 | | 120:00 | | | | | reset Aschenlade | D | |")
        _, res = run("status", "--today", TODAY, text=text, tmp=self.tmp)
        t = {t["id"]: t for t in res["tasks"]}["ASCHE"]
        self.assertEqual((t["counter_value_h"], t["hours_to_message"], t["state"]), (0, 150, "ok"))
        self.assertIn("reset to 0 on 2025-11-10", t["note"])

    def test_ash_reading_after_reset_is_used_as_read(self):
        text = self.with_row("Readings", "| 2025-11-10 | | 120:00 | | | | | reset Aschenlade | D | |")
        text = text.replace("| 2025-11-10 | | 120:00 | | | | | reset Aschenlade | D | |",
                            "| 2025-11-10 | | 120:00 | | | | | reset Aschenlade | D | |\n"
                            "| 2025-11-14 | | 40:00 | | | | | | D | |")
        _, res = run("status", "--today", TODAY, text=text, tmp=self.tmp)
        t = {t["id"]: t for t in res["tasks"]}["ASCHE"]
        self.assertEqual((t["counter_read_on"], t["counter_value_h"], t["hours_to_message"]),
                         ("2025-11-14", 40, 110))
        self.assertIn("as read on 2025-11-14", t["note"])

    def test_ash_counter(self):
        t = self.states(TODAY)["ASCHE"]
        self.assertEqual((t["hours_to_message"], t["hours_to_F20"]), (60, 110))
        self.assertEqual(t["last_done"], "2025-02-16")  # the F20 fault row is not a completion


class Forecast(Base):
    def setUp(self):
        super().setUp()
        _, self.res = run("prognose", "--today", TODAY, "--days", "30")
        self.t = {t["id"]: t for t in self.res["tasks"]}

    def test_never_lengthens(self):
        self.assertNotIn("proposal", self.t["SAUGZUG"])
        self.assertIn("cannot lengthen", self.t["SAUGZUG"]["verdict"])

    def test_shortens_with_heavy_history(self):
        self.assertEqual(self.t["WT"]["proposal"], "6 mo")

    def test_gap_task_gets_proposal_alone(self):
        self.assertEqual(self.t["RAUCHROHR"]["proposal"], "3 mo")

    def test_needs_three_intervals(self):
        self.assertIn("insufficient", self.t["SICHT"]["verdict"])

    def test_floor_never_above_ceiling(self):
        self.assertEqual(logbog.floor_proposal(500, {"months": 12}), {"months": 12})
        self.assertEqual(logbog.floor_proposal(20, {"days": 7}), {"days": 7})

    def test_pellets(self):
        p = self.res["pellets"]
        self.assertEqual((p["n"], p["kg_per_day_median"]), (4, 10.71))

    def test_stale_ash_estimate_is_flagged(self):
        self.assertIn("stale", self.res["ash_counter"])


class Checklist(Base):
    def test_month(self):
        _, res = run("tjekliste", "--måned", "2025-11")
        self.assertEqual(len(res["items"]), 13)
        self.assertEqual(res["monthly_check_logged"], ["2025-11-03"])
        self.assertEqual(len(res["weekly_checks_logged"]), 2)


if __name__ == "__main__":
    unittest.main()
