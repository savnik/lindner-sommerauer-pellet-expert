# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.4] - 2026-11-21

### Added

- Logbook: optional Readings columns "Level (sacks)" and "Level before fill
  (sacks)", for a store read on a sack scale. A level read between fills is a
  row of its own instead of a Note.
- `logbog.py forbrug`: "Consumption between level readings": kg, kg per day,
  kg per hour and kg per burner hour from one level reading to the next, fills
  or not, with its own summary (median from n ≥ 3, n, range). Marked
  approximate and kept out of the fill-to-fill headline figures. A fill
  without a level read before it breaks the chain.
- `logbog.py validate`: a level before fill on a row without a fill is an
  error; a level that rises without a fill, or a fill whose levels do not
  match the sacks added (by more than one sack), is a warning.

## [0.3.3] - 2026-11-17

### Changed

- What the counters count (verification.md line 52, closing lines 50 and 51):
  Betrieb-STD counts hours the boiler is in an operating mode and available;
  the Aschenlade counter counts burner time. Field observation on one
  controller, labelled as such; the manual prints neither. The `logbog` skill
  now says kg per Betrieb-STD hour is per available hour, not per burner hour,
  and `parameters.md` carries a pointer at Betrieb-STD.

### Added

- `logbog.py forbrug`: burner hours per fill interval from the Aschenlade
  counter, summed across "reset Aschenlade" rows, and kg per burner hour, with
  median, n and range over exact intervals, and burner hours per month or
  season. A reset without a reading is a gap, as for Betrieb-STD. The skill
  says kg per burner hour is fuel use, not efficiency.

## [0.3.2] - 2026-11-15

### Fixed

- `logbog.py status` and `prognose`: after a "reset Aschenlade" row the ash
  counter counts as 0 from that date. Before, the value read just before the
  reset was used, so ASCHE showed as due or overdue right after emptying.
- `logbog.py validate`: a date (YYYY-MM-DD) in a Note no longer triggers the
  "phone-number-like digit string" warning.

## [0.3.1] - 2026-11-15

### Added

- Logbook template: optional "Pellet product" column in Readings (brand and
  product from the sack, never the shop), so a change in consumption can be
  tied to a change of pellets. Logbooks without the column stay valid.
- Logbook template and `logbog` skill: read the fill level the same way every
  time, for example by running the suction manually before filling so the
  boiler's hopper is full. Labelled as an owner practice, not from the manual,
  with the Handbetrieb safety lines.

## [0.3.0] - 2026-11-15

### Added

- `logbog` skill: a private logbook per installation at
  `pellet-installations/logbog/<label>.md`, with service done, a service plan
  triggered by time, operating hours or the Aschenlade counter, counter
  readings and pellet fills. Same rules as the installation record: rows shown
  before writing, written only on a yes, owner or technician but no names,
  source code on every row, append only.
- `logbog.py`, a standard-library script that validates the logbook and
  computes consumption (kg, operating hours, kg per hour, per interval, month
  or heating season), service status, forecasts and the TRVB monthly
  checklist. The skill quotes its numbers and never computes them itself.
  It reads one local file, writes nothing and sends nothing.
- Service-plan template seeded with the printed intervals from the
  Putzanleitung and TRVB H 118, with the Rauchrohr and Wartung GAPs and the
  three conflicting ash intervals passed on unresolved. A forecast may
  shorten a printed interval, never lengthen it; the script refuses a plan
  that does.
- Unit tests (`evals/unit/`, `evals/run.sh unit`) on a fictional logbook, and
  six eval cases for the logbook: consent and no identifiers, consumption
  figures, counter-reset gap, no lengthening (safety tier), the three ash
  sources, and the Rauchrohr GAP.
- Verification log lines 50–51: what Betrieb-STD counts, and whether the
  Aschenlade counter counts the same hours.

### Changed

- Installation record template schema 2: maintenance moves to the logbook. A
  schema-1 record's Maintenance rows are offered for copying, never moved.
- Main skill routes logging, due tasks and consumption to the logbook skill,
  and does not read `pellet-installations/logbog/` as records.
- Privacy policy and READMEs describe the logbook and the local script.

## [0.2.0] - 2026-09-22

### Added

- `feedback` skill: reports a wrong, missing, unsafe or confusing answer as a
  GitHub issue. Shows the full text first, posts only on a yes, via the GitHub
  CLI or a pre-filled link, from the user's own account. Excludes identifiers
  and installation-record contents. Issue template and labels in the repo.

### Changed

- Data-handling rule 1 and the privacy policy name the feedback skill as the
  single exception to "nothing leaves the machine".

## [0.1.1] - 2026-09-22

### Added

- README and LICENSE inside the plugin directory, so the plugin is self-contained when installed from a catalogue that references the subdirectory.

### Changed

- Plugin description now states that it is unofficial and mentions the private installation record.

## [0.1.0] - 2026-09-22

### Added

- All five eval sets run at least once (proxy runs); all rows pass. A live
  test with a real record passed. Verification log gained a status index so
  closed lines are not cited as open doubt.

- Eval sets completed: five owner-written integration questions and three
  manual-reasoning questions, with pass bars. Integration set passes in a
  proxy run after one skill fix (routing row for switching off and seasonal
  questions). Gap-marking and anchor conventions finalised; three
  verification lines closed by full-resolution re-reads.

- Skill sections written: data handling, safety (danger signals first, hard
  limits, pre-work warnings), audience modes, basis and tiers, routing with an
  English-to-German search glossary. Chapter 1 safety text of the operating
  manual ingested so the safety section can cite it.

- Installation records: a private, local, per-installation file the skill
  reads before answering and extends with consent. Template in
  `templates/installation-record.md`, behaviour in SKILL.md ("What am I
  looking at", "Installation record"), development skill `ingest-installation`,
  eval set `installation-adaptation` with a fictional fixture.

- Reference content from the SL-P 8/12/15/25 (Modell 2008) Betriebsanleitung,
  ingested with the `ingest-document` skill: hydraulics, components, technical
  data, commissioning and room-unit notes in `system-integration.md`; all
  controller menus, parameter lists, service parameters and error messages
  F2–F167 in `parameters.md`. Coverage manifests filled; 21 uncertain readings
  logged in `verification.md`.
- Anhang content: the one-page Lindner & Sommerauer Putz- und
  Reinigungsanleitung and the TRVB H 118 (2003) Anhang 2 Kontrollbuch, added
  to `system-integration.md`; 5 further verification lines.
- Montageanleitung SL-P (Stand 05-2009): store, fill pipes, suction nozzles,
  wall opening, suction distributor flap table, boiler dismantling and
  placement, chimney connection, main board terminal assignment. Also the
  blank Inbetriebnahme-Protokoll form, the TÜV test certificate for the
  SL-P 12, and the EAP RTFH4 room-sensor datasheet. 13 further verification
  lines.
- Marketplace and plugin manifests.
- Skill skeleton `lindner-sommerauer` with section headers and empty
  reference stubs carrying coverage manifests.
- Development skill `ingest-document`.
- Eval sets: out-of-scope, safety, personal-data (written); integration and
  manual-reasoning (stubs).

[Unreleased]: https://github.com/savnik/lindner-sommerauer-pellet-expert/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/savnik/lindner-sommerauer-pellet-expert/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/savnik/lindner-sommerauer-pellet-expert/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/savnik/lindner-sommerauer-pellet-expert/releases/tag/v0.1.0
