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
   never with logbook or installation-record contents or identifiers. The
   other is `scripts/graddage.py` (Degree days, below), which sends a postal
   code once to OpenStreetMap and then one 10 km grid-square id and a date
   range to DMI, only on the owner's yes. The address an owner gives for it is
   the one exception to rule 2: use it only for that, pass it to the script,
   and never store or repeat it.
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
- Time: ask for the time of day of a reading when the owner gives counters or
  a level ("hvad var klokken?"), and put it in "Time" (HH:MM). Rates over a
  day or two depend on it. A time taken from a photo's file name or metadata
  is fine; one you assume yourself is not a reading and goes in Note.
- Levels in sacks: when the owner reads the store on a sack scale, the number
  goes in "Level (sacks)" (the level after any fill in that row), and on a
  fill row the level read just before filling goes in "Level before fill
  (sacks)". A level read without a fill is its own row, with the counters if
  they were read. Do not put levels in Note when the logbook has these
  columns; a logbook without them can get them added (empty in older rows),
  shown to the owner first like any other change.
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
| `forbrug` | "how much have we used", kg per hour, kg per burner hour, per season | `--per interval\|month\|season` |
| `status` | "what's due", "what needs doing" | `--today` |
| `prognose` | "how much will we need", "should this interval change" | `--days N` |
| `silo` | "when is the store empty", "when must we fill", after every fill | `--dage N`, `--under SACKS` |
| `tjekliste` | the TRVB monthly checklist | `--måned YYYY-MM` |

Exit code 1 means the logbook has errors and the script refused to compute.
Show the errors and offer to correct them with correcting rows. Do not work
around it.

No Python, or the script fails: say that you cannot compute the figures here,
show the relevant rows as they stand, and stop. Do not compute them yourself.

Pass on the script's own qualifiers with its numbers: "approximate" for
intervals not ending at the same level, gaps across a counter reset, n, the
median and range, "stale" on an ash estimate. Source I rows are not in any
figure; say so if the owner asks why their estimate is missing.

"Betrieb-STD" counts the hours the boiler is in an operating mode and
available, whether or not it is firing. The Aschenlade counter counts burner
time, so it rises far more slowly. The manual prints neither; this is a field
observation on one controller (verification.md line 52, closing lines 50 and
51). So kg per Betrieb-STD hour is kg per available hour, not per burner hour.
Say so when kg per hour is the question, and say that it is a field
observation, not manufacturer text.

`forbrug` also gives burner hours (the Aschenlade counter, summed across
"reset Aschenlade" rows) and kg per burner hour: how much the boiler burns per
hour it burns. Quote it as the script prints it, with n and range. It is fuel
use, not efficiency. Efficiency is heat delivered over the energy in the
pellets, and the logbook has no measurement of heat delivered; never present
kg per burner hour, or anything derived from it, as efficiency. It also
depends on how hard the boiler worked in the period (a cold spell raises it),
so a change is a reason to look, not a finding. A burner-hour figure needs the
Aschenlade counter read at both fills and before every reset in between; when
it is missing, say which reading would have given it.

With level readings in sacks, `forbrug` treats the readings as the time
series they are: irregular readings of quantities that accumulate and reset.
It gives
- `series`: one point per reading at its own time: cumulative kg consumed
  (kg added since the first level reading plus the fall in level times the
  sack size, so fills drop out) and the counters made continuous across
  resets, each starting at 0;
- `steps`: the average rate between consecutive points (kg per day, kg per
  burner hour, kg per Betrieb-STD hour), constant over the step;
- `fit`: the least-squares slope through all points (n ≥ 3), which is less
  sensitive to one rough level reading than any single step.
All three are approximate (a level on a sack scale is an estimate, typically
to about one sack, which weighs heavily on a short step) and are kept apart
from the headline figures, which come from fill-to-fill intervals only. Quote
them as approximate, with n. Show a rate as constant over its step, never as
a point at the middle of an interval, and put every reading at its own time.

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

## Degree days

Burner hours per day rise and fall with the weather; burner hours (and kg)
per degree day take the weather out. Degree days come from DMI's open Climate
Data API (`acc_heating_degree_days_17`: 17 °C minus the daily mean, days below
17 °C only), for the 10 km grid square the home is in.

- Only the owner starts this. Before the first fetch, say what is sent (the
  square's id and the dates, to DMI), what is stored (the id in
  `pellet-installations/graddage.json`, the values in
  `pellet-installations/logbog/graddage.csv`) and that the position itself is
  not stored. Fetch only on a yes, and ask again before a later fetch unless
  the owner said fetching is fine from now on.
- First time: ask the owner for the address. Say that only its postal code
  leaves the machine (to OpenStreetMap, to find the postal area's centre) and
  that only the 10 km square's id is saved. Run
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/logbog/scripts/graddage.py" opsæt --adresse "..."`
  from the working directory. Never write the address anywhere else, and do
  not repeat it back. A large rural postal area can land in a neighbouring
  square; coordinates (`--lat --lon`, converted offline) give the exact one.
  Run in a terminal without a config, `hent` asks for the address itself.
- Then `graddage.py hent` fetches up to yesterday (today is not complete),
  continuing from the first day DMI had not yet quality controlled.
- `logbog.py forbrug ... --graddage pellet-installations/logbog/graddage.csv`
  reads that file only, adds degree days to `series`, `steps` and
  `burner_steps`, and the slopes `burner_hours_per_degree_day` and
  `kg_per_degree_day` to `fit`. Each day's degree days are spread evenly over
  its 24 hours; say so when a step is shorter than a few days.
  `preliminary_weather` marks a step with days DMI has not yet quality
  controlled; pass that on.
- A step that reaches into a day missing from the file has no degree-day
  figure; say which days are missing and that `hent` will fill them.
- Burner hours per degree day is how hard the boiler works for the weather;
  it says nothing about efficiency, and a change is a reason to look, not a
  finding. Degree days are a DMI figure for a 10 km square, not a measurement
  at the house.

## Next fill

`silo` shows the store level since the last fill and draws a straight line
from the last level reading at the average rate of the last week (`--dage`,
default 7; shorter when there are no older readings, and it says so). It gives
`below_threshold_at`, the date the store falls below the refill level, and
`empty_at`. The refill level is the Constants row "Refill level (sacks)", the
owner's own choice, else 5 sacks.

- After writing a fill row (and `validate`), run `silo` and tell the owner the
  latest expected next fill: `below_threshold_at`, as the date the store
  reaches the refill level, with the rate and window it rests on, quoted as
  the script prints them. Mark it approximate: levels are estimated on the
  sack scale and consumption follows the weather (it rises in a cold spell).
  This is the one forecast given without being asked, and only right after a
  fill.
- In the same answer, ask whether to make a calendar reminder for the day
  before that date. On a yes, run `silo` again with
  `--ics pellet-installations/logbog/naeste-paafyldning.ics` and open the file
  (`open` on macOS, `xdg-open` on Linux, `start` on Windows) so the owner's
  calendar app imports it; say that the owner confirms it there. The file is
  local; nothing is sent. Its text names no person, address or installation.
  On a no, do not ask again until the next fill.
- No levels in sacks, or too few readings: say that no date can be given yet
  and which reading would give one.

