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

## It learns your installation, privately

The plugin itself contains only common knowledge taken from the manufacturer's
documents. What is particular to your system (model, firmware, buffer and
sensor layout, the values actually set, errors and maintenance) goes into an
installation record: a plain Markdown file at `pellet-installations/<label>.md`
in your own working directory. The skill reads it before answering, proposes
additions as you talk, and writes only when you say yes.

The record stays on your machine. It is never sent anywhere by the plugin and
nothing from it is ever added to this repository. It is meant to hold no
names, addresses or serial numbers. You can read, edit or delete it at any time.

## Status: beta

Version 0.1.0 is an early beta. The references cover the SL-P 8/12/15/25
operating manual (Modell 2008), the SL-P installation manual (05-2009) and a
few supporting sheets, in the manufacturer's German. The safety, audience and
routing sections of the skill are not written yet, and 39 uncertain readings
are open in `verification.md`. Do not rely on it.

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
- `evals/` — frozen evaluation questions per set, with a fictional fixture record

## Licence

Code is MIT. Prose (skill text, reference files, evals, this README) is
CC BY 4.0. See `LICENSE`.
