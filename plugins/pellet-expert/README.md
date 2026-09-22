# pellet-expert

**Not affiliated with, endorsed by, or supported by Lindner & Sommerauer.** An
independent Claude Code skill built from the publicly available documentation
for their SL-P pellet boilers. No warranty. The official manual and an
authorised technician take precedence over anything this skill says.

## What it does

Answers questions about Lindner & Sommerauer SL-P 8/12/15/25 wood pellet
boilers: error messages, controller menus and parameters, hydraulic
integration, buffer and return temperature, commissioning, cleaning. Every
product fact is cited to the manual's chapter and page. Where the documents
are silent or contradict themselves, it says so instead of guessing.

It checks for danger signals before anything else, and it never helps bypass
a safety device or change the settings the manual marks as not to be changed.

## It learns your installation, privately

The skill reads an installation record at `pellet-installations/<label>.md`
in your working directory before answering, and offers to add what a
conversation establishes. It writes only when you say yes, records no names,
addresses or serial numbers, and never sends anything anywhere. Copy
`skills/lindner-sommerauer/templates/installation-record.md` to start one, or
let the skill offer.

## Install

```
/plugin marketplace add savnik/lindner-sommerauer-pellet-expert
/plugin install pellet-expert@savnik
```

Then ask about your boiler in plain language. The skill triggers on the
manufacturer's name, the model designations, or the topics above.

## Coverage and status

Beta. References cover the operating manual for firmware 080325.1, the
installation manual (05-2009) and a few supporting sheets, in the
manufacturer's German. Field observations from one controller on firmware
080325.4 are marked as such. See the repository for the verification log,
evals and changelog: https://github.com/savnik/lindner-sommerauer-pellet-expert

## Licence

Code MIT, prose CC BY 4.0. See LICENSE.

## Privacy

The plugin collects nothing and sends nothing. The only thing it stores is an
installation record you ask for, on your own machine. See [PRIVACY.md](PRIVACY.md).
