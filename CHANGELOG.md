# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/savnik/lindner-sommerauer-pellet-expert/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/savnik/lindner-sommerauer-pellet-expert/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/savnik/lindner-sommerauer-pellet-expert/releases/tag/v0.1.0
