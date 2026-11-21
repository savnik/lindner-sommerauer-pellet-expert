#!/usr/bin/env python3
"""Arithmetic for a pellet-expert logbook. Standard library only; reads one
local file, writes nothing, sends nothing.

The skill quotes the numbers this script prints and never works them out
itself. Every command validates the logbook first and refuses to compute on a
logbook with errors.

  logbog.py validate  LOGBOOK [--today YYYY-MM-DD] [--json]
  logbog.py forbrug   LOGBOOK [--per interval|month|season] [--json]
  logbog.py status    LOGBOOK [--today YYYY-MM-DD] [--json]
  logbog.py prognose  LOGBOOK [--today YYYY-MM-DD] [--days N] [--json]
  logbog.py tjekliste LOGBOOK --måned YYYY-MM [--json]

English aliases: consumption, forecast, checklist; --month for --måned.
Exit code 0 on success, 1 when the logbook has errors, 2 on bad usage.
"""

import argparse
import calendar
import datetime as dt
import json
import re
import statistics
import sys

SOURCES = {"D", "P", "O", "T", "I"}
ACTIONS = {"emptied", "cleaned", "inspected", "lubricated", "replaced",
           "repaired", "serviced", "fault cleared"}
CONDITIONS = {"ok", "light", "heavy"}
BY = {"owner", "technician"}
TRIGGERS = {"time", "hours", "time|hours", "counter"}
BASES = {"Manual", "TRVB", "Owner", "Predictive"}
CEILING_BASES = {"Manual", "TRVB"}
NOT_COMPLETION = {"fault cleared"}  # a cleared fault is logged, but is not the planned task done
COUNTERS = {"Betrieb-STD": "std", "Aschenlade": "ash"}
F20_MARGIN_H = 50.0   # "um 50 überschritten ... Fehler 20" [SL-P BA 2008, Kap. 5, S. 2]
MONTH_D = 365.2425 / 12
MIN_N = 3             # fewest observed intervals a median is reported on

SECTIONS = {
    "constants": ["Item", "Value", "Date", "Source"],
    "readings": ["Date", "Betrieb-STD", "Aschenlade aktuell", "Pellets added (kg)",
                 "Sacks", "Since", "Level after", "Event", "Source", "Note"],
    "service done": ["Date", "Task", "Action", "F-code", "Betrieb-STD",
                     "Condition", "By", "Source", "Note"],
    "service plan": ["ID", "Task", "Trigger", "Interval", "Basis",
                     "Valid from", "Note"],
}
REQUIRED = {"readings", "service done", "service plan"}

# TRVB H 118 (2003), Anhang 2/2, S. 27 and Anhang 2/3–2/4, S. 28–29.
# Third-party directive text, as transcribed in references/system-integration.md.
TRVB_MONTHLY = [
    "Funktionstüchtigkeit der Rückbrand-Schutzeinrichtung RSE, insbesondere der zuverlässige Schließvorgang",
    "Betriebsbereitschaft der Löscheinrichtungen einschließlich Wasserzufuhr",
    "Sauberkeit der Rauchgaswege (Rauchgaszüge im Heizkessel, Verbindungsstück und Rauchfang)",
    "Ordnungsgemäßer Betrieb der Steuerung",
    "Funktionstüchtigkeit der Störungsmeldung/Warneinrichtung(en)",
    "Ordnungsgemäßer Betrieb der Verbrennungsluft- und Saugzugventilatoren",
    "Ordnungsgemäßer Zustand des Feuerungsraumes/der Ausmauerung",
    "Einsatzbereitschaft der/des tragbaren Feuerlöscher(s)",
    "Ordnungsgemäße Aschelagerung",
    "Heizraum frei von brennbaren Lagerungen",
    "Dach frei von brennbaren Ablagerungen",
    "Brandschutzabschlüsse (Brandschutztüren - selbstschließend)",
]
TRVB_FORM_EXTRA = "Rauchfang-Überpr./Reinig."
TRVB_ANCHOR = "[TRVB H 118 (2003), Anhang 2/2, S. 27; form Anhang 2/4, S. 29]"

IDENTIFIER_PATTERNS = [
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "an email address"),
    (re.compile(r"\+?\d[\d ()-]{7,}\d"), "a phone-number-like digit string"),
    (re.compile(r"\b(serial|seriennr|serien-?nummer|s/n|fabrikationsnr|fabr\.?\s*nr)\b", re.I),
     "a serial number"),
]


# ---------------------------------------------------------------- parsing

class Problems:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, line, msg):
        self.errors.append({"line": line, "message": msg})

    def warn(self, line, msg):
        self.warnings.append({"line": line, "message": msg})


def split_row(line):
    cells = re.split(r"(?<!\\)\|", line.strip())
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [c.strip().replace("\\|", "|") for c in cells]


def parse_tables(text, problems):
    """Return {section: [row dicts with '_line']} for the known sections."""
    tables = {}
    section = None
    header = None
    in_comment = False
    for no, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if line.startswith("<!--"):
            in_comment = "-->" not in line
            continue
        if line.startswith("## "):
            name = line[3:].strip().lower()
            section = next((s for s in SECTIONS if name.startswith(s)), None)
            header = None
            if section is not None:
                tables.setdefault(section, [])
            continue
        if section is None or not line.startswith("|"):
            if header is not None and line and not line.startswith("|"):
                header = None  # the table ended
            continue
        cells = split_row(line)
        if header is None:
            header = cells
            missing = [c for c in SECTIONS[section] if c not in header]
            if missing:
                problems.error(no, f"table '{section}' lacks column(s): {', '.join(missing)}")
            continue
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        if len(cells) != len(header):
            problems.error(no, f"row has {len(cells)} cells, header has {len(header)}")
            continue
        row = dict(zip(header, cells))
        row["_line"] = no
        tables[section].append(row)
    for s in REQUIRED:
        if s not in tables:
            problems.error(0, f"section '## {s.title()}' not found")
    return tables


def parse_date(value):
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def parse_hours(value):
    """'12345h26', '12345h26m', '87:30', '0h00m', '12345', '12345,5' -> hours."""
    v = value.strip().replace(" ", "")
    if v in ("", "-", "–"):
        return None
    m = re.fullmatch(r"(\d+)[h:](\d{1,2})m?", v)
    if m:
        minutes = int(m.group(2))
        if minutes >= 60:
            raise ValueError(f"minutes {minutes} ≥ 60 in '{value}'")
        return int(m.group(1)) + minutes / 60
    m = re.fullmatch(r"(\d+(?:[.,]\d+)?)h?", v)
    if m:
        return float(m.group(1).replace(",", "."))
    raise ValueError(f"cannot read '{value}' as hours")


def parse_time(value):
    """'14:55' or '9:05' -> datetime.time; empty -> None."""
    v = value.strip()
    if v in ("", "-", "–"):
        return None
    m = re.fullmatch(r"(\d{1,2})[:.](\d{2})", v)
    if not m or int(m.group(1)) > 23 or int(m.group(2)) > 59:
        raise ValueError(f"Time '{value}' is not HH:MM")
    return dt.time(int(m.group(1)), int(m.group(2)))


def parse_number(value):
    v = value.strip().replace(" ", "")
    if v in ("", "-", "–"):
        return None
    try:
        return float(v.replace(",", "."))
    except ValueError:
        raise ValueError(f"cannot read '{value}' as a number")


INTERVAL_RE = re.compile(r"(\d+(?:[.,]\d+)?)\s*(w|wk|weeks?|mo|months?|y|yr|years?|d|days?|h|hours?)", re.I)


def parse_interval(value):
    """Return {'months': n, 'days': n, 'hours': n} (only keys present), {} for
    a dash, None if unreadable. '12 mo | 2000 h' gives months and hours."""
    v = value.strip()
    if v in ("-", "–", "—", ""):
        return {}
    if v.lower() == "aschenlade setting":
        return {"counter": True}
    out = {}
    for part in v.split("|"):
        m = INTERVAL_RE.fullmatch(part.strip())
        if not m:
            return None
        n = float(m.group(1).replace(",", "."))
        unit = m.group(2).lower()
        if unit.startswith("w"):
            out["days"] = n * 7
        elif unit.startswith("mo"):
            out["months"] = n
        elif unit.startswith("y"):
            out["months"] = n * 12
        elif unit.startswith("d"):
            out["days"] = n
        else:
            out["hours"] = n
    return out


def interval_days(iv):
    """Calendar length in days, for comparing two time intervals."""
    if "months" in iv:
        return iv["months"] * MONTH_D
    return iv.get("days")


def add_interval(date, iv):
    if "months" in iv:
        total = date.month - 1 + int(round(iv["months"]))
        year, month = date.year + total // 12, total % 12 + 1
        day = min(date.day, calendar.monthrange(year, month)[1])
        return dt.date(year, month, day)
    return date + dt.timedelta(days=round(iv["days"]))


def fmt_interval(iv):
    parts = []
    if "months" in iv:
        m = iv["months"]
        parts.append(f"{m:g} mo")
    if "days" in iv:
        d = iv["days"]
        parts.append(f"{d / 7:g} w" if d % 7 == 0 else f"{d:g} d")
    if "hours" in iv:
        parts.append(f"{iv['hours']:g} h")
    return " | ".join(parts) if parts else "-"


def h(x):
    return None if x is None else round(x, 2)


# ---------------------------------------------------------------- model

class Logbook:
    def __init__(self, text, today):
        self.today = today
        self.p = Problems()
        self.tables = parse_tables(text, self.p)
        self.constants = {}
        self.readings = []
        self.done = []
        self.plan = []
        self._constants()
        self._readings()
        self._done()
        self._plan()
        self._identifiers()
        self.series = {k: self._series(k) for k in ("std", "ash")}

    # -- common row checks
    def _date_source(self, row, date_key="Date", allow_blank_date=False):
        line = row["_line"]
        raw = row.get(date_key, "")
        d = parse_date(raw) if raw else None
        if raw and d is None:
            self.p.error(line, f"{date_key} '{raw}' is not YYYY-MM-DD")
        elif not raw and not allow_blank_date:
            self.p.error(line, f"{date_key} is empty")
        elif d and d > self.today:
            self.p.warn(line, f"{date_key} {d} is after today ({self.today})")
        src = row.get("Source")
        if src is not None:
            if src not in SOURCES:
                self.p.error(line, f"Source '{src}' is not one of D, P, O, T, I")
        return d

    def _constants(self):
        for row in self.tables.get("constants", []):
            item, value = row.get("Item", ""), row.get("Value", "")
            if not value:
                continue
            self._date_source(row)
            try:
                num = parse_hours(value) if "(h)" in item else parse_number(value)
            except ValueError as e:
                self.p.error(row["_line"], str(e))
                continue
            if row.get("Source") == "I":
                self.p.warn(row["_line"], f"'{item}' has source I and is ignored")
                continue
            self.constants[item.lower()] = num  # a later row overrides an earlier one

    def _readings(self):
        sack = self.constants.get("sack size (kg)")
        prev_date = None
        for row in self.tables.get("readings", []):
            line = row["_line"]
            d = self._date_source(row)
            if d is None:
                continue
            if prev_date and d < prev_date:
                self.p.warn(line, f"date {d} is earlier than the row above ({prev_date})")
            prev_date = d
            r = {"date": d, "line": line, "source": row.get("Source"),
                 "level": row.get("Level after", "").strip().lower(), "note": row.get("Note", "")}
            try:
                r["std"] = parse_hours(row.get("Betrieb-STD", ""))
                r["ash"] = parse_hours(row.get("Aschenlade aktuell", ""))
                kg = parse_number(row.get("Pellets added (kg)", ""))
                sacks = parse_number(row.get("Sacks", ""))
                r["lvl"] = parse_number(row.get("Level (sacks)", ""))
                r["lvl_before"] = parse_number(row.get("Level before fill (sacks)", ""))
                r["time"] = parse_time(row.get("Time", ""))
            except ValueError as e:
                self.p.error(line, str(e))
                continue
            for k, col in (("lvl", "Level (sacks)"), ("lvl_before", "Level before fill (sacks)")):
                if r[k] is not None and r[k] < 0:
                    self.p.error(line, f"{col} cannot be negative")
            if (r["lvl"] is not None or r["lvl_before"] is not None) and sack is None:
                self.p.error(line, "a level in sacks is given but 'Sack size (kg)' is not set under Constants")
            if sacks is not None:
                if sack is None:
                    self.p.error(line, "Sacks given but 'Sack size (kg)' is not set under Constants")
                elif kg is None:
                    kg = sacks * sack
                elif abs(kg - sacks * sack) > 0.5:
                    self.p.warn(line, f"{kg:g} kg does not match {sacks:g} sacks × {sack:g} kg")
            r["kg"] = kg
            if r["lvl_before"] is not None and kg is None:
                self.p.error(line, "Level before fill (sacks) given on a row without a fill")
            if r["lvl_before"] is not None and r["lvl"] is not None and kg is not None and sack:
                # one sack is the resolution of an owner's sack scale
                if abs((r["lvl"] - r["lvl_before"]) - kg / sack) > 1:
                    self.p.warn(line, f"level rose from {r['lvl_before']:g} to {r['lvl']:g} sacks, "
                                f"but {kg / sack:g} sacks were added")
            since = row.get("Since", "")
            r["since"] = parse_date(since) if since else None
            if since and r["since"] is None:
                self.p.error(line, f"Since '{since}' is not YYYY-MM-DD")
            if r["since"] and r["since"] >= d:
                self.p.error(line, "Since must be before Date")
            if since and kg is None:
                self.p.error(line, "Since given without kg or sacks")
            event = row.get("Event", "").strip()
            r["resets"] = set()
            for part in filter(None, (x.strip() for x in event.split(","))):
                m = re.fullmatch(r"reset (Betrieb-STD|Aschenlade)", part, re.I)
                if not m:
                    self.p.error(line, f"Event '{part}' is not 'reset Betrieb-STD' or 'reset Aschenlade'")
                    continue
                name = "Betrieb-STD" if m.group(1).lower().startswith("b") else "Aschenlade"
                r["resets"].add(COUNTERS[name])
            if r["source"] == "I":
                if (kg is not None or r["std"] is not None or r["ash"] is not None
                        or r["lvl"] is not None or r["lvl_before"] is not None):
                    self.p.warn(line, "source I: this row is context only and is not used in arithmetic")
                if r["resets"]:
                    self.p.error(line, "a counter reset cannot have source I")
                continue
            self.readings.append(r)

    def _done(self):
        for row in self.tables.get("service done", []):
            line = row["_line"]
            d = self._date_source(row)
            by = row.get("By", "").strip()
            if by and by.lower() not in BY:
                self.p.error(line, f"By '{by}' must be 'owner' or 'technician' (no names)")
            action = row.get("Action", "").strip().lower()
            if action and action not in ACTIONS:
                self.p.warn(line, f"Action '{action}' is not one of: {', '.join(sorted(ACTIONS))}")
            fcode = row.get("F-code", "").strip()
            if fcode and not re.fullmatch(r"F\d{1,2}", fcode, re.I):
                self.p.warn(line, f"F-code '{fcode}' does not look like F<number>")
            cond = row.get("Condition", "").strip().lower()
            if cond and cond not in CONDITIONS:
                self.p.warn(line, f"Condition '{cond}' is not ok, light or heavy")
            try:
                std = parse_hours(row.get("Betrieb-STD", ""))
            except ValueError as e:
                self.p.error(line, str(e))
                std = None
            if d is None or row.get("Source") == "I":
                continue
            self.done.append({"date": d, "task": row.get("Task", "").strip(), "action": action,
                              "fcode": fcode.upper(), "std": std, "condition": cond, "line": line})

    def _plan(self):
        seen = {}
        for row in self.tables.get("service plan", []):
            line = row["_line"]
            pid = row.get("ID", "").strip()
            if not re.fullmatch(r"[A-Z0-9][A-Z0-9-]*", pid):
                self.p.error(line, f"ID '{pid}' must be capitals, digits and hyphens")
                continue
            trig = row.get("Trigger", "").strip().lower().replace(" ", "")
            if trig not in TRIGGERS:
                self.p.error(line, f"Trigger '{row.get('Trigger')}' is not one of {', '.join(sorted(TRIGGERS))}")
            iv = parse_interval(row.get("Interval", ""))
            if iv is None:
                self.p.error(line, f"Interval '{row.get('Interval')}' cannot be read")
                continue
            if trig == "counter" and iv and "counter" not in iv:
                self.p.error(line, "Trigger counter needs Interval 'Aschenlade setting'")
            if trig in ("time", "hours", "time|hours") and iv:
                need_t, need_h = "time" in trig, "hours" in trig
                has_t, has_h = ("months" in iv or "days" in iv), "hours" in iv
                if need_t != has_t or need_h != has_h:
                    self.p.error(line, f"Trigger '{trig}' does not match Interval '{row.get('Interval')}'")
            basis_raw = row.get("Basis", "").strip()
            basis = basis_raw.split(" ")[0] if basis_raw else ""
            if basis not in BASES:
                self.p.error(line, f"Basis must start with one of {', '.join(sorted(BASES))}")
            vf_raw = row.get("Valid from", "").strip()
            vf = parse_date(vf_raw) if vf_raw else None
            if vf_raw and vf is None:
                self.p.error(line, f"Valid from '{vf_raw}' is not YYYY-MM-DD")
            key = (pid, vf)
            if key in seen:
                self.p.error(line, f"{pid} already has a row valid from {vf_raw or '(start)'} (line {seen[key]})")
            seen[key] = line
            self.plan.append({"id": pid, "task": row.get("Task", ""), "trigger": trig, "interval": iv,
                              "basis": basis, "basis_raw": basis_raw, "valid_from": vf, "line": line})
        # A prediction or an owner's choice may shorten a manual interval, never lengthen it.
        for p in self.plan:
            if p["basis"] in CEILING_BASES or not p["interval"]:
                continue
            for m in self.plan:
                if m["id"] != p["id"] or m["basis"] not in CEILING_BASES or not m["interval"]:
                    continue
                # Longer than the manual is refused. Longer than TRVB is flagged: whether
                # that third-party directive applies to an installation is the owner's call.
                report = self.p.error if m["basis"] == "Manual" else self.p.warn
                pd_, md = interval_days(p["interval"]), interval_days(m["interval"])
                if pd_ is not None and md is not None and pd_ > md + 0.5:
                    report(p["line"], f"{p['id']}: {p['basis']} interval {fmt_interval(p['interval'])} "
                           f"is longer than the {m['basis']} interval {fmt_interval(m['interval'])} "
                           f"(line {m['line']}); that interval is a ceiling")
                if "hours" in p["interval"] and "hours" in m["interval"] and \
                        p["interval"]["hours"] > m["interval"]["hours"]:
                    report(p["line"], f"{p['id']}: hours interval longer than the {m['basis']} interval")
        ids = {p["id"] for p in self.plan}
        for d in self.done:
            if re.fullmatch(r"[A-Z0-9][A-Z0-9-]*", d["task"]) and d["task"] not in ids:
                self.p.warn(d["line"], f"Task '{d['task']}' looks like an ID but is not in the Service plan")

    def _identifiers(self):
        for section, rows in self.tables.items():
            for row in rows:
                for col, val in row.items():
                    if col == "_line" or col in ("Date", "Since", "Valid from", "Betrieb-STD",
                                                 "Aschenlade aktuell", "Pellets added (kg)", "Sacks",
                                                 "Level (sacks)", "Level before fill (sacks)", "Time"):
                        continue
                    text = re.sub(r"\[[^\]]*\]", "", val)  # anchors carry page and year numbers
                    text = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", "", text)  # a date is not a phone number
                    for rx, what in IDENTIFIER_PATTERNS:
                        m = rx.search(text)
                        if m and (what != IDENTIFIER_PATTERNS[1][1]
                                  or sum(ch.isdigit() for ch in m.group()) >= 8):
                            self.p.warn(row["_line"], f"column '{col}' may contain {what}; "
                                        f"identifiers do not belong in the logbook")

    # -- counters
    def _series(self, key):
        """Continuous series [(date, cumulative h)] for one counter, and the dates
        after which continuity is lost. A reset row's value is read before the reset."""
        name = "Betrieb-STD" if key == "std" else "Aschenlade aktuell"
        points, gaps = [], []
        offset, last = 0.0, None
        for r in self.readings:
            v = r[key]
            if v is not None:
                if last is not None and v < last - 1e-9:
                    if key == "std":
                        self.p.error(r["line"], f"{name} fell from {last:g} to {v:g} without a 'reset Betrieb-STD' row")
                    else:
                        self.p.error(r["line"], f"{name} fell from {last:g} to {v:g} without a 'reset Aschenlade' row")
                    gaps.append(r["date"])
                    offset += last
                points.append((r["date"], offset + v, r["line"]))
                last = v
            if key in r["resets"]:
                if v is None:
                    gaps.append(r["date"])
                    offset += last or 0.0
                else:
                    offset += v
                last = 0.0
        return {"points": points, "gaps": gaps}

    def hours_between(self, key, d0, d1):
        """Counter increase between the last point on d0 and the last point on d1,
        or None if either is missing or a gap lies in between."""
        s = self.series[key]
        a = [c for d, c, _ in s["points"] if d == d0]
        b = [c for d, c, _ in s["points"] if d == d1]
        if not a or not b:
            return None
        if any(d0 <= g <= d1 for g in s["gaps"]):
            return None
        return b[-1] - a[-1]

    def latest(self, key):
        """(date, raw display value) of the newest reading of a counter."""
        for r in reversed(self.readings):
            if r[key] is not None:
                return r["date"], r[key]
        return None

    def current(self, key):
        """(date, value, reset) of a counter as last known. A reset row means the
        counter stood at 0 from that date, whatever was read before the reset."""
        for r in reversed(self.readings):
            if key in r["resets"]:
                return r["date"], 0.0, True
            if r[key] is not None:
                return r["date"], r[key], False
        return None

    def cum_at(self, key, date):
        pts = [c for d, c, _ in self.series[key]["points"] if d == date]
        return pts[-1] if pts else None


# ---------------------------------------------------------------- commands

def cmd_validate(lb, args):
    level_warnings(lb)
    return {"errors": lb.p.errors, "warnings": lb.p.warnings,
            "counts": {"readings": len(lb.readings), "service done": len(lb.done),
                       "plan rows": len(lb.plan)}}


def fill_intervals(lb):
    fills = [r for r in lb.readings if r["kg"] is not None]
    out = []
    prev = None
    for f in fills:
        start = f["since"] or (prev["date"] if prev else None)
        if start is None:
            prev = f
            continue  # the first fill only sets the starting level
        exact = (f["since"] is None and prev is not None and prev["level"] != ""
                 and prev["level"] == f["level"])
        days = (f["date"] - start).days
        hours = lb.hours_between("std", start, f["date"])
        burner = lb.hours_between("ash", start, f["date"])
        out.append({"from": start, "to": f["date"], "days": days, "kg": f["kg"],
                    "exact": exact, "hours": hours, "burner_hours": burner, "line": f["line"],
                    "basis": (f"same level ('{f['level']}') at both fills" if exact
                              else "approximate: level differs, unknown, or stated period")})
        prev = f
    return out


def consumption_series(lb):
    """Cumulative series, one point per reading, at the reading's own time.

    kg: pellets consumed since the first level reading,
        = kg added after that reading + (first level - level now) x sack size.
        Fills drop out; a fill without a level reading costs nothing.
    burner_h / std_h: the counters made continuous across resets.
    A reading without a time of day is placed at 12:00 and says so."""
    sack = lb.constants.get("sack size (kg)")
    cum = {k: {ln: c for _, c, ln in lb.series[k]["points"]} for k in ("std", "ash")}
    pts, base, added = [], None, 0.0
    for r in lb.readings:
        when = dt.datetime.combine(r["date"], r["time"] or dt.time(12, 0))
        fill = r["kg"] is not None
        if fill and r["since"] is not None:
            base = None          # a stated period: start again from the next level
            continue
        kg = None
        if sack:
            if fill and r["lvl_before"] is not None and base is not None:
                kg = added + (base - r["lvl_before"]) * sack
            if fill and base is not None:
                added += r["kg"]
            if r["lvl"] is not None:
                if base is None:
                    base, added = r["lvl"], 0.0
                kg_after = added + (base - r["lvl"]) * sack
                kg = kg_after if kg is None else kg
        p = {"t": when, "time_known": r["time"] is not None, "line": r["line"], "fill_kg": r["kg"],
             "kg": kg, "burner_h": cum["ash"].get(r["line"]), "std_h": cum["std"].get(r["line"])}
        if any(p[k] is not None for k in ("kg", "burner_h", "std_h")):
            pts.append(p)
    # a counter gap splits the counter series: drop counter values after an unbridged gap
    for k, key in (("burner_h", "ash"), ("std_h", "std")):
        gaps = lb.series[key]["gaps"]
        if gaps:
            first_gap = min(gaps)
            for p in pts:
                if p["t"].date() >= first_gap:
                    p[k] = None
    # start every series at 0 at its first point: amounts since the start
    for k in ("kg", "burner_h", "std_h"):
        first = next((p[k] for p in pts if p[k] is not None), None)
        if first is not None:
            for p in pts:
                if p[k] is not None:
                    p[k] -= first
    return pts


def series_steps(pts):
    """Rates between consecutive points that both have kg: constant over the step."""
    kp = [p for p in pts if p["kg"] is not None]
    out = []
    for a, b in zip(kp, kp[1:]):
        days = (b["t"] - a["t"]).total_seconds() / 86400
        if days <= 0:
            continue
        dkg = b["kg"] - a["kg"]
        if dkg < -1e-9:
            continue
        dburn = (b["burner_h"] - a["burner_h"]) if a["burner_h"] is not None and b["burner_h"] is not None else None
        dstd = (b["std_h"] - a["std_h"]) if a["std_h"] is not None and b["std_h"] is not None else None
        out.append({"from": a["t"], "to": b["t"], "days": days, "kg": dkg,
                    "burner_hours": dburn, "hours": dstd})
    return out


def slope(xs, ys):
    """Least-squares slope and intercept, or (None, None) below MIN_N points."""
    if len(xs) < MIN_N or len(set(xs)) < 2:
        return None, None
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    return b, my - b * mx


def level_warnings(lb):
    sack = lb.constants.get("sack size (kg)")
    if not sack:
        return
    prev = None
    for r in lb.readings:
        if r["kg"] is not None:
            prev = r["lvl"]
            continue
        if r["lvl"] is not None:
            if prev is not None and r["lvl"] > prev + 1e-9:
                lb.p.warn(r["line"], f"level rose from {prev:g} to {r['lvl']:g} sacks without a fill")
            prev = r["lvl"]


def rate(x, y):
    return None if (x is None or not y) else x / y


def cmd_forbrug(lb, args):
    ivs = fill_intervals(lb)
    rows = []
    for iv in ivs:
        rows.append({"from": str(iv["from"]), "to": str(iv["to"]), "days": iv["days"],
                     "kg": h(iv["kg"]), "kg_per_day": h(rate(iv["kg"], iv["days"])),
                     "hours": h(iv["hours"]), "kg_per_hour": h(rate(iv["kg"], iv["hours"])),
                     "hours_per_day": h(rate(iv["hours"], iv["days"])),
                     "burner_hours": h(iv["burner_hours"]),
                     "kg_per_burner_hour": h(rate(iv["kg"], iv["burner_hours"])),
                     "exact": iv["exact"], "basis": iv["basis"]})
    exact = [r for r in rows if r["exact"]]
    kgh = [r["kg_per_hour"] for r in exact if r["kg_per_hour"] is not None]
    kgb = [r["kg_per_burner_hour"] for r in exact if r["kg_per_burner_hour"] is not None]
    kgd = [r["kg_per_day"] for r in exact if r["kg_per_day"] is not None]
    summary = {
        "exact_intervals": len(exact),
        "approximate_intervals": len(rows) - len(exact),
        "kg_per_hour_median": h(statistics.median(kgh)) if len(kgh) >= MIN_N else None,
        "kg_per_hour_n": len(kgh),
        "kg_per_hour_range": [h(min(kgh)), h(max(kgh))] if kgh else None,
        "kg_per_burner_hour_median": h(statistics.median(kgb)) if len(kgb) >= MIN_N else None,
        "kg_per_burner_hour_n": len(kgb),
        "kg_per_burner_hour_range": [h(min(kgb)), h(max(kgb))] if kgb else None,
        "kg_per_day_median": h(statistics.median(kgd)) if len(kgd) >= MIN_N else None,
        "kg_per_day_n": len(kgd),
    }
    level_warnings(lb)
    pts = consumption_series(lb)
    iso = lambda t: t.isoformat(timespec="minutes")
    series = [{"t": iso(p["t"]), "time_known": p["time_known"], "kg": h(p["kg"]),
               "burner_hours": h(p["burner_h"]), "hours": h(p["std_h"]),
               "fill_kg": h(p["fill_kg"])} for p in pts]
    steps = [{"from": iso(x["from"]), "to": iso(x["to"]), "days": h(x["days"]), "kg": h(x["kg"]),
              "kg_per_day": h(rate(x["kg"], x["days"])),
              "burner_hours": h(x["burner_hours"]),
              "kg_per_burner_hour": h(rate(x["kg"], x["burner_hours"])),
              "hours": h(x["hours"]), "kg_per_hour": h(rate(x["kg"], x["hours"]))} for x in series_steps(pts)]
    t0 = pts[0]["t"] if pts else None
    kd = [((p["t"] - t0).total_seconds() / 86400, p["kg"]) for p in pts if p["kg"] is not None]
    kb = [(p["burner_h"], p["kg"]) for p in pts if p["kg"] is not None and p["burner_h"] is not None]
    kh = [(p["std_h"], p["kg"]) for p in pts if p["kg"] is not None and p["std_h"] is not None]
    fits = {}
    for name, xy in (("kg_per_day", kd), ("kg_per_burner_hour", kb), ("kg_per_hour", kh)):
        b, a0 = slope([x for x, _ in xy], [y for _, y in xy])
        fits[name] = {"slope": h(b), "intercept": h(a0), "n_points": len(xy)}
    fits["note"] = ("least-squares slope through the cumulative points; approximate, "
                    f"needs at least {MIN_N} points")
    # Counter hours between consecutive readings, from the counters alone.
    def counter_steps(key):
        steps = []
        pts = lb.series[key]["points"]
        for (d0, c0, _), (d1, c1, _) in zip(pts, pts[1:]):
            if d1 > d0 and not any(d0 <= g <= d1 for g in lb.series[key]["gaps"]):
                steps.append({"from": d0, "to": d1, "hours": c1 - c0})
        return steps
    hpd = counter_steps("std")
    bpd = counter_steps("ash")
    per = args.per
    buckets = {}
    if per in ("month", "season"):
        def key(day):
            if per == "month":
                return f"{day.year}-{day.month:02d}"
            y = day.year if day.month >= 7 else day.year - 1
            return f"{y}/{str(y + 1)[2:]}"
        def spread(d0, d1, amount, field, approx=False):
            n = (d1 - d0).days
            if n <= 0 or amount is None:
                return
            for i in range(n):
                b = buckets.setdefault(key(d0 + dt.timedelta(days=i + 1)),
                                       {"kg": 0.0, "kg_days": 0, "kg_approx": False,
                                        "hours": 0.0, "hour_days": 0,
                                        "burner_hours": 0.0, "burner_days": 0})
                b[field] += amount / n
                b[{"kg": "kg_days", "hours": "hour_days", "burner_hours": "burner_days"}[field]] += 1
                if approx:
                    b["kg_approx"] = True
        for iv in ivs:
            spread(iv["from"], iv["to"], iv["kg"], "kg", not iv["exact"])
        for x in hpd:
            spread(x["from"], x["to"], x["hours"], "hours")
        for x in bpd:
            spread(x["from"], x["to"], x["hours"], "burner_hours")
    table = [{"period": k, "kg": h(b["kg"]) if b["kg_days"] else None,
              "kg_days_covered": b["kg_days"], "kg_approximate": b["kg_approx"],
              "hours": h(b["hours"]) if b["hour_days"] else None,
              "hour_days_covered": b["hour_days"],
              "burner_hours": h(b["burner_hours"]) if b["burner_days"] else None,
              "burner_days_covered": b["burner_days"]}
             for k, b in sorted(buckets.items())]
    return {"intervals": rows, "summary": summary, "per": per, "periods": table,
            "series": series, "steps": steps, "fit": fits,
            "notes": ["hours are Betrieb-STD: hours in an operating mode with the boiler "
                      "available. burner_hours are the Aschenlade counter, summed across "
                      "'reset Aschenlade' rows: hours the burner burned (field observation, "
                      "verification.md line 52).",
                      "kg/h and kg per burner hour are fuel use, not efficiency: efficiency "
                      "needs a measurement of the heat delivered.",
                      "kg/h and kg per burner hour are computed only where both fills ended at "
                      "the same level, with the counter read on both dates and no counter gap "
                      "between. The headline medians use these intervals only.",
                      "Month and season figures spread each interval evenly over its days; "
                      "they are an allocation, not a measurement.",
                      "series: cumulative kg consumed (from levels in sacks and fills) and "
                      "cumulative counter hours at each reading's own time; readings without a "
                      "Time are placed at 12:00. steps: the average rate between consecutive "
                      "points, constant over the step. fit: the slope through all points. "
                      "All three are approximate: a level is estimated on the owner's sack "
                      "scale, typically to about one sack. They are not in the headline "
                      "medians."]}


def active_plan(lb):
    out = {}
    for p in lb.plan:
        if p["valid_from"] and p["valid_from"] > lb.today:
            continue
        cur = out.get(p["id"])
        if cur is None or (p["valid_from"] or dt.date.min) >= (cur["valid_from"] or dt.date.min):
            out[p["id"]] = p
    return out


def soon_margin_days(iv_days):
    return max(1.0, 0.1 * iv_days)


def cmd_status(lb, args):
    rows = []
    std_latest = lb.latest("std")
    for pid, p in active_plan(lb).items():
        done = [d for d in lb.done if d["task"] == pid and d["action"] not in NOT_COMPLETION]
        last = done[-1] if done else None
        if last is None:
            done_sorted = []
        else:
            done_sorted = sorted(done, key=lambda d: d["date"])
            last = done_sorted[-1]
        r = {"id": pid, "task": p["task"], "basis": p["basis_raw"],
             "interval": fmt_interval(p["interval"]) if "counter" not in p["interval"] else "Aschenlade setting",
             "last_done": str(last["date"]) if last else None, "times_done": len(done)}
        iv = p["interval"]
        if p["trigger"] == "counter":
            setting = lb.constants.get("aschenlade setting (h)")
            lat = lb.current("ash")
            r["counter_setting_h"] = h(setting)
            if lat is None or setting is None:
                r["state"] = "no reading" if lat is None else "setting unknown"
            else:
                d, val, was_reset = lat
                r["counter_read_on"] = str(d)
                r["counter_value_h"] = h(val)
                r["hours_to_message"] = h(setting - val)
                r["hours_to_F20"] = h(setting + F20_MARGIN_H - val)
                r["state"] = ("overdue" if val >= setting else
                              "due soon" if setting - val <= 0.1 * setting else "ok")
                r["note"] = (f"{'reset to 0' if was_reset else 'as read'} on {d}; the counter has moved since. "
                             f"Message at the setting, "
                             f"F20 stop at setting + {F20_MARGIN_H:g} h [SL-P BA 2008, Kap. 5, S. 1–2]")
            rows.append(r)
            continue
        if not iv:
            r["state"] = "no interval"
            r["note"] = "the documents give no number; the owner may choose one"
            rows.append(r)
            continue
        if last is None:
            r["state"] = "no record"
            r["note"] = "never logged as done, so no due date can be computed"
            rows.append(r)
            continue
        states = []
        if "months" in iv or "days" in iv:
            due = add_interval(last["date"], iv)
            left = (due - lb.today).days
            r["due_date"] = str(due)
            r["days_left"] = left
            margin = soon_margin_days(interval_days(iv))
            states.append("overdue" if left < 0 else "due soon" if left <= margin else "ok")
        if "hours" in iv:
            base = last["std"]
            if base is None or std_latest is None:
                r["hours_note"] = "Betrieb-STD not read when last done, or never read"
                states.append("unknown")
            else:
                left_h = base + iv["hours"] - std_latest[1]
                r["due_at_betrieb_std"] = h(base + iv["hours"])
                r["hours_left"] = h(left_h)
                r["hours_read_on"] = str(std_latest[0])
                states.append("overdue" if left_h < 0 else
                              "due soon" if left_h <= 0.1 * iv["hours"] else "ok")
        order = ["overdue", "due soon", "unknown", "ok"]
        r["state"] = min(states, key=order.index)
        rows.append(r)
    order = {"overdue": 0, "due soon": 1, "setting unknown": 2, "no reading": 2, "unknown": 2,
             "ok": 3, "no record": 4, "no interval": 5}
    rows.sort(key=lambda r: (order.get(r["state"], 9), r["id"]))
    return {"today": str(lb.today), "tasks": rows}


def floor_proposal(days, ceiling):
    """Round a median interval DOWN to whole months (>= 60 d) or whole weeks.
    Three days of slack lets a median of 91 d read as 3 months. Never above
    the manual ceiling."""
    if days >= 60:
        months = max(1, int((days + 3) // MONTH_D))
        if ceiling and "months" in ceiling:
            months = min(months, int(ceiling["months"]))
        return {"months": months}
    weeks = max(1, int((days + 1) // 7))
    if ceiling:
        weeks = min(weeks, int(interval_days(ceiling) // 7))
    return {"days": weeks * 7}


def cmd_prognose(lb, args):
    plan = active_plan(lb)
    manual = {}
    for p in lb.plan:
        if p["basis"] in CEILING_BASES and p["interval"] and "counter" not in p["interval"]:
            cur = manual.get(p["id"])
            if cur is None or interval_days(p["interval"]) < interval_days(cur):
                manual[p["id"]] = p["interval"]
    tasks = []
    for pid in sorted(plan):
        done = sorted((d for d in lb.done if d["task"] == pid and d["action"] not in NOT_COMPLETION),
                      key=lambda d: d["date"])
        gaps = [(b["date"] - a["date"]).days for a, b in zip(done, done[1:]) if b["date"] > a["date"]]
        conds = {c: sum(1 for d in done if d["condition"] == c) for c in ("ok", "light", "heavy")}
        r = {"id": pid, "n_intervals": len(gaps), "conditions": conds}
        ceiling = manual.get(pid)
        ceiling_days = interval_days(ceiling) if ceiling else None
        r["ceiling_interval"] = fmt_interval(ceiling) if ceiling else None
        if len(gaps) < MIN_N:
            r["verdict"] = f"insufficient data: {len(gaps)} observed interval(s), {MIN_N} needed"
            tasks.append(r)
            continue
        med = statistics.median(gaps)
        r.update({"median_days": med, "min_days": min(gaps), "max_days": max(gaps)})
        prop = floor_proposal(med, ceiling)
        if ceiling_days is not None and interval_days(prop) >= ceiling_days - 0.5:
            r["verdict"] = "the ceiling interval stands; history cannot lengthen it"
        else:
            r["proposal"] = fmt_interval(prop)
            r["verdict"] = ("history is shorter than the ceiling interval; the owner may adopt the proposal"
                            if ceiling_days is not None else
                            "the documents give no number; the owner may adopt the proposal")
        tasks.append(r)
    # Ash counter: hours per day between consecutive readings without a reset in between.
    ash = {}
    pts, agaps = lb.series["ash"]["points"], lb.series["ash"]["gaps"]
    rates = [(c1 - c0) / (d1 - d0).days for (d0, c0, _), (d1, c1, _) in zip(pts, pts[1:])
             if d1 > d0 and not any(d0 <= g <= d1 for g in agaps)]
    setting = lb.constants.get("aschenlade setting (h)")
    lat = lb.current("ash")
    ash["n_rates"] = len(rates)
    if len(rates) >= MIN_N and lat and setting is not None:
        med = statistics.median(rates)
        d, val, was_reset = lat
        ash["from_reading"] = f"{val:g} h on {d}" + (" (reset)" if was_reset else "")
        ash["counter_h_per_day_median"] = h(med)
        ash["counter_h_per_day_range"] = [h(min(rates)), h(max(rates))]
        if med > 0:
            ash["estimated_message_date"] = str(d + dt.timedelta(days=max(0, (setting - val) / med)))
            ash["estimated_F20_date"] = str(d + dt.timedelta(days=max(0, (setting + F20_MARGIN_H - val) / med)))
        if ash.get("estimated_message_date", "9999") < str(lb.today):
            ash["stale"] = "the estimated date has already passed; read the counter before acting"
        ash["note"] = ("estimate from the median rate; it moves with the season. "
                       "Not a reason to change the Aschenlade setting")
    else:
        ash["verdict"] = f"insufficient data: {len(rates)} rate(s), {MIN_N} needed, plus a reading and the setting"
    # Pellets: median kg/day of exact intervals, same months of the year first.
    ivs = [iv for iv in fill_intervals(lb) if iv["exact"] and iv["days"] > 0]
    target = lb.today + dt.timedelta(days=args.days / 2)
    def near(iv):
        mid = iv["from"] + (iv["to"] - iv["from"]) / 2
        diff = abs(mid.month - target.month)
        return min(diff, 12 - diff) <= 1
    seasonal = [iv for iv in ivs if near(iv)]
    use, basis = (seasonal, "intervals in the same months of the year (±1)") if len(seasonal) >= MIN_N \
        else (ivs, "all exact intervals (too few in the same months)")
    pel = {"days": args.days, "n": len(use), "basis": basis}
    if len(use) >= MIN_N:
        rr = [iv["kg"] / iv["days"] for iv in use]
        med = statistics.median(rr)
        pel.update({"kg_per_day_median": h(med), "kg_expected": h(med * args.days),
                    "kg_range": [h(min(rr) * args.days), h(max(rr) * args.days)]})
        sack = lb.constants.get("sack size (kg)")
        if sack:
            pel["sacks_expected"] = h(med * args.days / sack)
    else:
        pel["verdict"] = f"insufficient data: {len(use)} exact interval(s), {MIN_N} needed"
    return {"today": str(lb.today), "tasks": tasks, "ash_counter": ash, "pellets": pel,
            "rules": ["A forecast may shorten a Manual or TRVB interval, never lengthen it.",
                      "A forecast becomes a plan row only after the owner says yes.",
                      f"Medians are reported from n ≥ {MIN_N} only, always with n and range."]}


def cmd_tjekliste(lb, args):
    m = re.fullmatch(r"(\d{4})-(\d{2})", args.month or "")
    if not m:
        raise SystemExit("--måned must be YYYY-MM")
    y, mo = int(m.group(1)), int(m.group(2))
    first = dt.date(y, mo, 1)
    last = dt.date(y, mo, calendar.monthrange(y, mo)[1])
    in_month = [d for d in lb.done if first <= d["date"] <= last]
    return {"month": f"{y}-{mo:02d}", "anchor": TRVB_ANCHOR,
            "items": TRVB_MONTHLY + [TRVB_FORM_EXTRA],
            "monthly_check_logged": [str(d["date"]) for d in in_month if d["task"] == "TRVB-MON"],
            "weekly_checks_logged": [str(d["date"]) for d in in_month if d["task"] == "SICHT"],
            "other_service_in_month": [{"date": str(d["date"]), "task": d["task"], "action": d["action"]}
                                       for d in in_month if d["task"] not in ("TRVB-MON", "SICHT")]}


# ---------------------------------------------------------------- output

def md_table(rows, cols):
    if not rows:
        return "(none)\n"
    def cell(v):
        if v is None:
            return "–"
        if isinstance(v, bool):
            return "yes" if v else "no"
        if isinstance(v, float):
            return f"{v:g}"
        if isinstance(v, (list, dict)):
            return json.dumps(v, ensure_ascii=False)
        return str(v).replace("|", "\\|")
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        out.append("| " + " | ".join(cell(r.get(c)) for c in cols) + " |")
    return "\n".join(out) + "\n"


def render(command, res, problems):
    out = []
    if problems.warnings:
        out.append("Warnings:")
        out += [f"- line {w['line']}: {w['message']}" for w in problems.warnings]
        out.append("")
    if command == "validate":
        if res["errors"]:
            out.append("Errors:")
            out += [f"- line {e['line']}: {e['message']}" for e in res["errors"]]
        else:
            c = res["counts"]
            out.append(f"OK: {c['readings']} readings, {c['service done']} service rows, {c['plan rows']} plan rows.")
    elif command == "forbrug":
        out.append("## Consumption by fill interval\n")
        out.append(md_table(res["intervals"], ["from", "to", "days", "kg", "kg_per_day", "hours",
                                               "kg_per_hour", "hours_per_day", "burner_hours",
                                               "kg_per_burner_hour", "exact", "basis"]))
        out.append("## Summary\n")
        out += [f"- {k}: {v if v is not None else '– (fewer than %d values)' % MIN_N}"
                for k, v in res["summary"].items()]
        if res["steps"]:
            out.append("\n## Cumulative series (approximate)\n")
            out.append(md_table(res["series"], ["t", "time_known", "kg", "burner_hours", "hours", "fill_kg"]))
            out.append("### Rate between readings\n")
            out.append(md_table(res["steps"], ["from", "to", "days", "kg", "kg_per_day", "burner_hours",
                                               "kg_per_burner_hour", "hours", "kg_per_hour"]))
            out.append("### Slope through all points\n")
            out += [f"- {k}: {v}" for k, v in res["fit"].items()]
        if res["per"] in ("month", "season"):
            out.append(f"\n## Per {res['per']} (allocated)\n")
            out.append(md_table(res["periods"], ["period", "kg", "kg_days_covered", "kg_approximate",
                                                 "hours", "hour_days_covered",
                                                 "burner_hours", "burner_days_covered"]))
        out.append("")
        out += [f"Note: {n}" for n in res["notes"]]
    elif command == "status":
        out.append(f"## Service status on {res['today']}\n")
        out.append(md_table(res["tasks"], ["state", "id", "task", "interval", "last_done", "due_date",
                                           "days_left", "hours_left", "counter_value_h", "hours_to_message",
                                           "hours_to_F20", "basis"]))
        notes = [f"- {t['id']}: {t['note']}" for t in res["tasks"] if t.get("note")]
        notes += [f"- {t['id']}: {t['hours_note']}" for t in res["tasks"] if t.get("hours_note")]
        if notes:
            out.append("Notes:")
            out += notes
    elif command == "prognose":
        out.append(f"## Forecast on {res['today']}\n")
        out.append("### Service intervals from history\n")
        out.append(md_table(res["tasks"], ["id", "n_intervals", "median_days", "min_days", "max_days",
                                           "ceiling_interval", "proposal", "conditions", "verdict"]))
        out.append("### Aschenlade counter\n")
        out += [f"- {k}: {v}" for k, v in res["ash_counter"].items()]
        out.append(f"\n### Pellets, next {res['pellets']['days']} days\n")
        out += [f"- {k}: {v}" for k, v in res["pellets"].items() if k != "days"]
        out.append("")
        out += [f"Rule: {r}" for r in res["rules"]]
    elif command == "tjekliste":
        out.append(f"## TRVB monthly checks, {res['month']} {res['anchor']}\n")
        out.append("Third-party directive (Austrian TRVB H 118), not the manufacturer's text.\n")
        out += [f"- [ ] {i}" for i in res["items"]]
        out.append("")
        out.append(f"Monthly check logged: {', '.join(res['monthly_check_logged']) or 'no'}")
        out.append(f"Weekly visual checks logged: {len(res['weekly_checks_logged'])}"
                   + (f" ({', '.join(res['weekly_checks_logged'])})" if res['weekly_checks_logged'] else ""))
        if res["other_service_in_month"]:
            out.append("Other service this month:")
            out += [f"- {o['date']}: {o['task']} ({o['action']})" for o in res["other_service_in_month"]]
    return "\n".join(out).rstrip() + "\n"


COMMANDS = {"validate": cmd_validate, "forbrug": cmd_forbrug, "status": cmd_status,
            "prognose": cmd_prognose, "tjekliste": cmd_tjekliste}
ALIASES = {"consumption": "forbrug", "forecast": "prognose", "checklist": "tjekliste"}


def main(argv=None):
    ap = argparse.ArgumentParser(prog="logbog.py", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="command", required=True)
    for name in COMMANDS:
        aliases = [a for a, n in ALIASES.items() if n == name]
        sp = sub.add_parser(name, aliases=aliases)
        sp.add_argument("logbook")
        sp.add_argument("--today", help="YYYY-MM-DD; default is the system date")
        sp.add_argument("--json", action="store_true")
        if name == "forbrug":
            sp.add_argument("--per", choices=["interval", "month", "season"], default="season")
        if name == "prognose":
            sp.add_argument("--days", type=int, default=30)
        if name == "tjekliste":
            sp.add_argument("--måned", "--maaned", "--month", dest="month", required=True)
    args = ap.parse_args(argv)
    command = ALIASES.get(args.command, args.command)
    today = dt.date.today()
    if args.today:
        today = parse_date(args.today)
        if today is None:
            ap.error("--today must be YYYY-MM-DD")
    try:
        with open(args.logbook, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"cannot read logbook: {e}", file=sys.stderr)
        return 2
    lb = Logbook(text, today)
    if command != "validate" and lb.p.errors:
        res = {"refused": "the logbook has errors; fix them first", "errors": lb.p.errors,
               "warnings": lb.p.warnings}
        if args.json:
            print(json.dumps(res, ensure_ascii=False, indent=2, default=str))
        else:
            print("Refused: the logbook has errors; no numbers were computed.\n")
            print("\n".join(f"- line {e['line']}: {e['message']}" for e in lb.p.errors))
        return 1
    res = COMMANDS[command](lb, args)
    if args.json:
        res.setdefault("warnings", lb.p.warnings)
        print(json.dumps(res, ensure_ascii=False, indent=2, default=str))
    else:
        print(render(command, res, lb.p), end="")
    return 1 if lb.p.errors else 0


if __name__ == "__main__":
    sys.exit(main())
