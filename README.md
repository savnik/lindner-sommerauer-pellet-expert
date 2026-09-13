# lindner-sommerauer-pellet-expert

**This project is not affiliated with, endorsed by, or supported by Lindner &
Sommerauer.** It is an independent, community-maintained Claude Code skill
that reads the publicly available documentation for their pellet boilers.
It comes with no warranty of any kind. For anything that affects safety,
warranty, or the operation of your boiler, the official manual and an
authorised technician take precedence over anything this skill says.

## What it is

A Claude Code plugin marketplace with one plugin, `pellet-expert`, containing
a skill that answers questions about Lindner & Sommerauer wood pellet boilers
(SL and SL-P range): troubleshooting, error codes, controller parameters,
hydraulic integration, buffer and return temperature, and commissioning.

The skill answers only from the documents it has been given. Where the
documents are silent it says so instead of guessing.

## Who it is for

Owners and installers of a Lindner & Sommerauer pellet system who want a
second reading of the manual, a way to work out which parameter does what,
or help describing a problem before calling a technician.

## Status: beta

Version 0.1.0 is scaffolding. The reference files are empty and the skill
does not yet contain any pellet-system content. Do not rely on it.

Maintained by Peter Savnik in spare time. Issues and corrections welcome;
response time is best-effort.

## Install

```
/plugin marketplace add savnik/lindner-sommerauer-pellet-expert
/plugin install pellet-expert@savnik
```

For a local checkout:

```
/plugin marketplace add ./lindner-sommerauer-pellet-expert
/plugin install pellet-expert@savnik
```

## Layout

- `plugins/pellet-expert/` — the plugin users install
- `.claude/skills/` — development tooling; never installed for users
- `evals/` — frozen evaluation questions per set

## Licence

Code is MIT. Prose (skill text, reference files, evals, this README) is
CC BY 4.0. See `LICENSE`.
