#!/usr/bin/env python3
"""Heating degree days from DMI's open Climate Data API, saved to a local CSV.

The only script in the plugin that reaches the network, and only when the owner
runs it. It sends one 10 km grid cell id and a date range, nothing else: no
logbook content, no coordinates. Coordinates given with --lat/--lon are turned
into a cell id here, offline. logbog.py never reaches the network; it reads the
CSV this script writes (logbog.py forbrug --graddage FILE).

  graddage.py opsæt --adresse "Vejnavn 1, 2800 By"   # once: save the 10 km cell
  graddage.py opsæt --lat 55.68 --lon 12.57           # or from coordinates, offline
  graddage.py hent [--fra YYYY-MM-DD] [--til YYYY-MM-DD]

First run: with no config, "hent" asks for the address when run in a terminal,
or tells you to run "opsæt". From an address only the four-digit postal code
is used: it is looked up in OpenStreetMap's Nominatim (the postal code and the
country, nothing else) to get the centre of the postal area, which is turned
into the 10 km cell id. The street, the house number and the town are not sent
and not stored. Only the cell id is saved (pellet-installations/graddage.json),
and only the cell id is sent to DMI. A large rural postal area may land in a
neighbouring 10 km cell; use --lat/--lon for an exact cell. "hent" continues from the first day
DMI had not yet quality controlled, or else the day after the last one in the CSV (default pellet-installations/logbog/graddage.csv) up to yesterday.

Data: parameter acc_heating_degree_days_17 (17 °C minus the daily mean
temperature, days below 17 °C only), daily, collection 10kmGridValue, DMI Climate
Data API v2 [opendataapi.dmi.dk]. DMI's terms of use apply; cite DMI as the source.
Values with qcStatus "none" are not yet quality controlled and may change; a
later run replaces them.
"""

import argparse
import csv
import datetime as dt
import json
import math
import os
import re
import sys
import urllib.parse
import urllib.request

API = "https://opendataapi.dmi.dk/v2/climateData/collections/10kmGridValue/items"
PARAM = "acc_heating_degree_days_17"
CELL_RE = re.compile(r"10km_\d{3}_\d{2,3}")
CONFIG = os.path.join("pellet-installations", "graddage.json")
CSV_DEFAULT = os.path.join("pellet-installations", "logbog", "graddage.csv")
DK = (54.4, 57.9, 7.9, 15.3)   # rough bounding box of Denmark incl. Bornholm


def utm32(lat, lon):
    """WGS84/ETRS89 latitude, longitude -> UTM zone 32N easting, northing (m)."""
    a, f, k0 = 6378137.0, 1 / 298.257223563, 0.9996
    e2 = f * (2 - f)
    ep2 = e2 / (1 - e2)
    phi, lam, lam0 = math.radians(lat), math.radians(lon), math.radians(9.0)
    n = a / math.sqrt(1 - e2 * math.sin(phi) ** 2)
    t, c = math.tan(phi) ** 2, ep2 * math.cos(phi) ** 2
    A = math.cos(phi) * (lam - lam0)
    m = a * ((1 - e2 / 4 - 3 * e2 ** 2 / 64 - 5 * e2 ** 3 / 256) * phi
             - (3 * e2 / 8 + 3 * e2 ** 2 / 32 + 45 * e2 ** 3 / 1024) * math.sin(2 * phi)
             + (15 * e2 ** 2 / 256 + 45 * e2 ** 3 / 1024) * math.sin(4 * phi)
             - (35 * e2 ** 3 / 3072) * math.sin(6 * phi))
    east = k0 * n * (A + (1 - t + c) * A ** 3 / 6 + (5 - 18 * t + t * t + 72 * c - 58 * ep2) * A ** 5 / 120) + 500000
    north = k0 * (m + n * math.tan(phi) * (A * A / 2 + (5 - t + 9 * c + 4 * c * c) * A ** 4 / 24
                                           + (61 - 58 * t + t * t + 600 * c - 330 * ep2) * A ** 6 / 720))
    return east, north


def cell_id(lat, lon):
    e, n = utm32(lat, lon)
    return f"10km_{int(n // 10000)}_{int(e // 10000)}"


def parse_position(text):
    m = re.fullmatch(r"\s*(-?\d+(?:[.,]\d+)?)\s*[,; ]\s*(-?\d+(?:[.,]\d+)?)\s*", text)
    if not m:
        raise ValueError("write the position as latitude, longitude, e.g. 55.68, 12.57")
    lat, lon = (float(x.replace(",", ".")) for x in m.groups())
    if not (DK[0] <= lat <= DK[1] and DK[2] <= lon <= DK[3]):
        raise ValueError("the position is not in Denmark; DMI's grid covers Denmark only")
    return lat, lon


POSTCODE_RE = re.compile(r"(?<!\d)([1-9]\d{3})(?!\d)")
NOMINATIM = "https://nominatim.openstreetmap.org/search"


def postcode_of(address):
    """The Danish postal code in an address, found locally; None if absent."""
    codes = POSTCODE_RE.findall(address)
    return codes[-1] if codes else None


def postcode_centre(code):
    """Centre of a Danish postal area from OpenStreetMap. Sends the code only."""
    q = urllib.parse.urlencode({"postalcode": code, "countrycodes": "dk", "format": "jsonv2", "limit": "1"})
    req = urllib.request.Request(NOMINATIM + "?" + q, headers={"User-Agent": "pellet-expert-graddage"})
    with urllib.request.urlopen(req, timeout=30) as r:
        hits = json.load(r)
    if not hits:
        raise ValueError(f"postal code {code} not found")
    return float(hits[0]["lat"]), float(hits[0]["lon"])


def cell_from_address(address):
    code = postcode_of(address)
    if code is None:
        raise ValueError("no four-digit postal code found in the address")
    lat, lon = postcode_centre(code)
    parse_position(f"{lat},{lon}")   # inside Denmark
    return cell_id(lat, lon), code


def save_config(path, cell):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"cell": cell, "csv": CSV_DEFAULT,
                   "note": "10 km DMI grid cell for degree days. The address or position it was made "
                           "from is not stored."},
                  fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def load_config(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        cfg = json.load(fh)
    if not CELL_RE.fullmatch(cfg.get("cell", "")):
        raise SystemExit(f"{path}: 'cell' is not a 10 km cell id")
    return cfg


def fetch(cell, d0, d1):
    q = {"parameterId": PARAM, "timeResolution": "day", "cellId": cell,
         "datetime": f"{d0 - dt.timedelta(days=1)}T00:00:00Z/{d1 + dt.timedelta(days=1)}T00:00:00Z",
         "limit": "1000"}
    url = API + "?" + urllib.parse.urlencode(q)
    req = urllib.request.Request(url, headers={"User-Agent": "pellet-expert-graddage"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    out = {}
    for f in data.get("features", []):
        p = f["properties"]
        day = dt.date.fromisoformat(p["from"][:10])   # DMI's local day
        if d0 <= day <= d1 and day < dt.date.today():  # today is not complete yet
            out[day] = (p["value"], p.get("qcStatus") or "")
    return out


def read_csv(path):
    rows, meta = {}, {}
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("#"):
                    k, _, v = line[1:].strip().partition(":")
                    meta[k.strip()] = v.strip()
                    continue
                break
        with open(path, encoding="utf-8") as fh:
            for r in csv.DictReader(l for l in fh if not l.startswith("#")):
                rows[dt.date.fromisoformat(r["date"])] = (float(r["degree_days"]), r.get("qc_status", ""))
    return rows, meta


def write_csv(path, cell, rows):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(f"# source: DMI Climate Data API, {PARAM}, 10kmGridValue, daily\n")
        fh.write(f"# cell: {cell}\n")
        w = csv.writer(fh)
        w.writerow(["date", "degree_days", "qc_status"])
        for d in sorted(rows):
            w.writerow([d.isoformat(), f"{rows[d][0]:g}", rows[d][1]])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=CONFIG)
    sub = ap.add_subparsers(dest="cmd", required=True)
    o = sub.add_parser("opsæt", aliases=["setup"], help="save the 10 km cell for an address or position")
    o.add_argument("--adresse", "--address", help="address; only its postal code is used and sent")
    o.add_argument("--lat", type=float)
    o.add_argument("--lon", type=float)
    h = sub.add_parser("hent", aliases=["fetch"], help="fetch daily degree days into the local CSV")
    h.add_argument("--fra", type=dt.date.fromisoformat, help="first day; default: day after the CSV's last")
    h.add_argument("--til", type=dt.date.fromisoformat, default=dt.date.today() - dt.timedelta(days=1))
    h.add_argument("--ud", help="CSV file (default from the config)")
    a = ap.parse_args(argv)

    if a.cmd in ("opsæt", "setup"):
        try:
            if a.adresse:
                cell, code = cell_from_address(a.adresse)
                how = f"from postal code {code} (only the postal code was sent, to OpenStreetMap)"
            elif a.lat is not None and a.lon is not None:
                cell = cell_id(*parse_position(f"{a.lat},{a.lon}"))
                how = "from the position, offline"
            else:
                print("give --adresse, or --lat and --lon", file=sys.stderr)
                return 2
        except (ValueError, OSError) as e:
            print(e, file=sys.stderr)
            return 2
        save_config(a.config, cell)
        print(f"Saved cell {cell} in {a.config}, {how}. The address or position was not stored.")
        return 0

    cfg = load_config(a.config)
    if cfg is None:
        if not sys.stdin.isatty():
            print(f"No location configured ({a.config}). Run once: graddage.py opsæt --adresse \"<address>\"",
                  file=sys.stderr)
            return 3
        print("Degree days come from DMI for the 10 km square your home is in.\n"
              "Type your address once. Only its postal code is used: it is sent to OpenStreetMap\n"
              "to find the area's centre. Only the 10 km cell id is saved, and sent to DMI.")
        while True:
            try:
                cell, _ = cell_from_address(input("Address: "))
                break
            except (ValueError, OSError) as e:
                print(e)
            except EOFError:
                return 3
        save_config(a.config, cell)
        cfg = load_config(a.config)
        print(f"Saved cell {cfg['cell']} in {a.config}.")
    cell, out = cfg["cell"], a.ud or cfg.get("csv", CSV_DEFAULT)
    rows, meta = read_csv(out)
    if meta.get("cell") and meta["cell"] != cell:
        print(f"{out} holds cell {meta['cell']}, not {cell}; use another file", file=sys.stderr)
        return 2
    prelim_days = [d for d in rows if rows[d][1] == "none"]
    d0 = a.fra or (min(prelim_days) if prelim_days else max(rows) + dt.timedelta(days=1) if rows else None)
    if d0 is None:
        print("The CSV is empty: give --fra YYYY-MM-DD for the first day", file=sys.stderr)
        return 2
    if d0 > a.til:
        print(f"{out} is up to date (last day {max(rows)})")
        return 0
    new = fetch(cell, d0, a.til)
    rows.update(new)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    write_csv(out, cell, rows)
    prelim = sum(1 for d in new if new[d][1] == "none")
    last = min(a.til, dt.date.today() - dt.timedelta(days=1))
    missing = [d for d in (d0 + dt.timedelta(days=i) for i in range((last - d0).days + 1)) if d not in rows]
    print(f"{len(new)} days fetched for {cell} into {out}; {prelim} not yet quality controlled"
          + (f"; missing: {', '.join(map(str, missing))}" if missing else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
