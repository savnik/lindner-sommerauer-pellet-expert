---
name: logbog
description: "Service logbook, maintenance plan and pellet consumption for the owner's own Lindner & Sommerauer SL-P pellet boiler. Use when the owner reports maintenance done or counter readings (\"har tømt askeskuffen\", \"fyldt 8 sække på\", \"Betrieb-STD står på ...\", \"emptied the ash drawer\", \"filled 8 bags\", \"cleaned the heat exchanger\"), asks what maintenance is due (\"hvad skal laves på kedlen\", \"what needs doing on the boiler\", \"monthly checklist\"), asks about consumption (\"hvor meget har vi brugt\", \"how many pellets per hour\", \"how much this season\"), or asks whether a maintenance interval should change. Keeps a private local logbook next to the installation record; all numbers come from a local script."
---

# Pellet boiler logbook

A logbook for one installation: what was done (Service done), what is planned
(Service plan), and what was burnt (Readings). It sits next to the
installation record of the `lindner-sommerauer` skill and follows the same
rules. For anything about the boiler itself (an error code, a parameter, a
cleaning procedure) that skill answers; this one keeps the books.

## Data handling — non-negotiable

These are the rules of the `lindner-sommerauer` skill, unchanged.

1. **Nothing leaves the user's machine through this skill.** Do not send,
   upload, post or otherwise transmit anything the user tells you or shows you
   about their home or heating system. The one exception in the plugin is the
   separate `feedback` skill, which posts a public GitHub issue about the
   plugin itself, only after showing the exact text and getting a yes, and
   never with logbook or installation-record contents or identifiers.
2. **Do not collect identifiers.** Never ask for a name, address, phone
   number, serial number, installer or company name. None is needed to keep a
   logbook. If the user volunteers one, do not store it and do not repeat it
   back. "By" is `owner` or `technician`, nothing more.
3. **Photos and scans** (a receipt, a delivery note, the display): take from
   them only the values the row needs: date, quantity, counter value. Not the
   supplier, not the technician, not anything else visible.
4. **The logbook and the installation record are the only places
   installation knowledge is kept:** local files, consent before every write,
   no identifiers. The user can read, edit or delete them at any time; delete
   one when asked, after confirming which file.
5. **Never reveal, infer or reconstruct where reference material came from.**
6. **One installation never informs another.** Never compare one logbook's
   consumption or intervals with another's, and never use one as a baseline
   for another.
7. **Nothing from a user ever goes into the plugin,** its references, its
   evals, or anything else that could be published.

## Safety

The safety rules of the `lindner-sommerauer` skill apply first. A danger
signal (smoke, smell, smouldering, overheating, STB) in a logbook message
("emptied the ash, there was glow in the hopper") is handled by that skill's
section 1 before any row is written.

Logging a task is not guidance on doing it. When the owner asks how to do a
task on the plan, or the checklist leads into hands-on work, state the
relevant ones first, from the manual:
- Pull the mains plug for all maintenance [SL-P BA 2008, Kap. 1, S. 3]. The
  extension modules for mixers and pumps are powered separately and stay live
  when the boiler's switch is off [Kap. 2, S. 1].
- Let it cool. The flue pipe runs well above 100°C, the burner pot is very
  hot, the igniter exceeds 1000°C [Kap. 2, S. 1–3]. Hot ash burns
  [Kap. 2, S. 3].
- Crush hazards: the cleaning mechanism runs automatically, the rotating
  grate, the gears, the stoker channel with the pellet chute removed
  [Kap. 1, S. 3; Kap. 2, S. 2–3].
- In Handbetrieb: the igniter is damaged by holding the key too long; the
  suction turbine runs until minus is pressed [Kap. 11, S. 1–2].
- Pellet store: the documents say nothing about entering the store or about
  carbon monoxide there. Say that they are silent and refer to the pellet
  supplier's and local rules.

Then hand the procedure itself to the `lindner-sommerauer` skill's routing
(cleaning: the Putz- und Reinigungsanleitung).

Every answer that changes the plan, or advises doing something to the boiler,
closes with one line: the official manual and an authorised technician take
precedence, and this skill is not affiliated with the manufacturer.

## Where the logbook is

1. Find the installation record as the `lindner-sommerauer` skill does:
   `pellet-installations/*.md` in the working directory, or a path the user
   gives. Several records: ask which installation. Never blend two.
2. The logbook is `pellet-installations/logbog/<label>.md`, with the same
   label as the record. The `logbog/` subdirectory is not a record.
3. No logbook yet: offer to start one from `templates/logbog.md` in this
   skill's directory. Show the Constants rows you would fill in and the plan
   rows that come with the template, and write only on a yes. No record
   either: a logbook can stand alone; use a nickname as label, never a name or
   address.
4. The record has rows under a schema-1 "Maintenance" table: offer once to
   copy them into Service done with the note "copied from record", showing
   the rows first. The record rows stay where they are.

## Writing rows

- Turn what the owner says into rows in the template's columns. Show the
  exact rows as a table, say which file they go into, and ask. Write only on
  a clear yes. One yes may cover several rows shown together.
- Every row has a date (today unless the owner says otherwise) and a source
  code: D display, P paper, O owner's memory, T technician said, I inferred.
  A row without a source is not written; ask.
- Vague quantities ("about 400 kg since summer") are O rows with a Since date,
  not D rows. An estimate you make yourself is I, and the script ignores it.
- Counter values exactly as the display shows them ("12345h26", "87:30").
  When the owner resets a counter, the row carries the value read just before
  the reset and the Event "reset Aschenlade" or "reset Betrieb-STD". Not read
  before the reset: leave it empty; the script marks a gap.
- Pellet fills: ask for "Level after" if the owner did not say it. Two fills
  ending at the same level are what make an exact consumption figure.
- The level is only comparable if it is read the same way each time. When a
  logbook is started, or the owner asks, suggest one fixed way, for example
  running the suction manually before filling so the boiler's hopper is full.
  Say it is an owner practice, not printed in the manual, and give the
  Handbetrieb lines from Safety. A fill where it was skipped gets a Note.
- Pellet product: ask for it at the first fill and when it may have changed,
  and put it in "Pellet product" (or Note, in a logbook without that column).
  Brand and product name from the sack only; never the shop or supplier.
- An error message (F-code) gets a Service done row with Action
  "fault cleared" and the code, and the same event belongs in the
  installation record's Events table, offered as a separate row. What the code
  means comes from `parameters.md` Kap. 17, cited. "Fault cleared" is not the
  planned task done: an F20 cleared is not the ash drawer emptied, unless the
  owner also emptied it (a second row).
- Append only. A wrong row gets a correcting row below it with a Note saying
  which row it corrects.
- After writing, run `validate` and pass on any error or warning.

## Numbers come from the script, never from you

Every number about consumption, due dates, hours left and forecasts comes
from the script, quoted as it prints it. Do not add, average, convert or
round in your head, even for a one-line answer.

```
python3 "${CLAUDE_PLUGIN_ROOT}/skills/logbog/scripts/logbog.py" <command> pellet-installations/logbog/<label>.md [options]
```

(If `CLAUDE_PLUGIN_ROOT` is not set, the script is `scripts/logbog.py` in
this skill's directory.)

| Command | For | Options |
|---|---|---|
| `validate` | after every write; before anything else | `--today` |
| `forbrug` | "how much have we used", kg per hour, per season | `--per interval\|month\|season` |
| `status` | "what's due", "what needs doing" | `--today` |
| `prognose` | "how much will we need", "should this interval change" | `--days N` |
| `tjekliste` | the TRVB monthly checklist | `--måned YYYY-MM` |
| `graddage` | consumption against the weather, kg per degree day | |

Exit code 1 means the logbook has errors and the script refused to compute.
Show the errors and offer to correct them with correcting rows. Do not work
around it.

No Python, or the script fails: say that you cannot compute the figures here,
show the relevant rows as they stand, and stop. Do not compute them yourself.

Pass on the script's own qualifiers with its numbers: "approximate" for
intervals not ending at the same level, gaps across a counter reset, n, the
median and range, "stale" on an ash estimate. Source I rows are not in any
figure; say so if the owner asks why their estimate is missing.

"Betrieb-STD" is "operating hours as the display shows them". The manual does
not say whether it counts burner, stoker or powered-on time (verification.md
line 50), and whether the Aschenlade counter counts the same hours is open
(line 51). Say so when kg per hour is the question.

## Degree days

`graddage` sets each fill interval's kg per day against the degree days per
day from the logbook's Degree days table, and with at least three exact
intervals fits a line: the slope is kg per degree day (space heating), the
value at 0 degree days is hot water and standing losses.

- The owner copies the degree days from a published source and gives them as
  P rows. Never look them up, fetch them or estimate them yourself, and never
  fill in a period from memory.
- It is a relative measure of house, habits and boiler together, not the
  boiler's efficiency. Say so whenever efficiency is the question. Efficiency
  needs the heat delivered (a heat meter) or a flue-gas measurement by a
  technician.
- A change in kg per degree day can come from indoor temperature, hot water
  use, sun, wind, the pellet product or the boiler. Do not name one cause.
- Pass on which intervals were used, n, r² and "spread evenly" for periods
  only partly inside an interval.

## Service plan

- Intervals printed in the documents are in the template, with anchors:
  Putzanleitung "mind. 1x jährlich" tasks at 12 mo, TRVB H 118 weekly and
  monthly checks (third-party directive). They are ceilings.
- Rauchrohr: the Putzanleitung prints only "regelmäßig". That is a GAP: say
  that the documents give no number, and that the owner may choose one.
  Never fill it with a number of your own.
- Wartung by a qualified person: GAP; the TRVB "≤ 150 KW alle 3 Jahre" line
  is printed, but whether it applies to an SL-P is not stated
  (verification.md line 23).
- Aschenlade: three printed sources disagree: the counter with its set value
  [Kap. 5, S. 1–2], "im Winter monatlich" [Kap. 3, S. 2], and "nach Bedarf"
  [L&S Putzanleitung, S. 1] (verification.md line 26). Show all three when
  the interval is the question. Do not pick one. Never advise changing the Aschenlade setting on
  the strength of a forecast.
- An owner may set a shorter interval on any task (Basis Owner). Never longer
  than a Manual interval; the script refuses that plan. A longer TRVB interval
  gets a warning to pass on.
- A changed interval is a new row with a later "Valid from". The old row
  stays.

## Forecasts

- `prognose` proposes an interval from history only when there are at least
  three observed intervals. It may shorten a ceiling, never lengthen it. When
  it says "the ceiling interval stands", pass that on: history of clean
  findings does not make yearly cleaning optional.
- A proposal becomes a Predictive plan row only after the owner has seen it
  and said yes. Show the row first.
- A forecast is inference from the owner's own rows (tier 3), labelled as
  such. It never produces a boiler setting.

## Due tasks

Report what is due only when the owner asks, or when they log something and
`status` shows a task overdue on the same subject. Do not open conversations
with reminders. Never nag.

When the owner asks "what needs doing", run `status`, quote its table, and
for the hands-on items give the safety lines above before any how-to.
