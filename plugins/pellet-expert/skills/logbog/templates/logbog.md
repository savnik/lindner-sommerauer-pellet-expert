# Logbook: <label>

<!-- A private logbook for ONE installation, kept by its owner, outside the plugin.
     Location: pellet-installations/logbog/<label>.md in the owner's working
     directory, next to the installation record pellet-installations/<label>.md.
     <label> is the same nickname as the record's. Not a name, not an address.

     The same rules as the installation record apply:
     - No names of people, addresses, phone numbers, serial numbers, installer or
       company names. "By" says owner or technician, nothing more.
     - Every row carries a date (YYYY-MM-DD) and a source code:
         D  read from the controller display by the owner
         P  paper: a receipt, delivery note, technician's report
         O  stated by the owner from memory
         T  stated by a technician
         I  inferred. Context only; the script ignores I rows for arithmetic.
     - Append, never rewrite. A wrong row gets a correcting row below it and a
       Note saying which row it corrects.

     The tables are read by skills/logbog/scripts/logbog.py. Keep the column
     names. Leave a cell empty when there is nothing to put in it.
     "Last done" and "next due" are never stored here: the script computes them
     from "Service done" and "Service plan". -->

schema: 1
installation record: <label>.md
created:

## Constants

| Item | Value | Date | Source |
|---|---|---|---|
| Sack size (kg) | | | |
| Aschenlade setting (h) | | | |
| Refill level (sacks) | | | |

## Readings

Counter readings and pellet fills. One row per occasion.

- Time: optional, the time of day of the reading (HH:MM). Consumption rates
  between readings use it; a reading without a time is placed at 12:00.
- Betrieb-STD and Aschenlade aktuell: as the display shows them ("12345h26",
  "87:30"). Betrieb-STD is in Zusatzparameter Service [SL-P BA 2008, Kap. 13,
  S. 3]; Aschenlade aktuell is the first number of the Aschenlade item in
  Dauerbetrieb [SL-P BA 2008, Kap. 5, S. 1].
- Pellets added (kg) or Sacks: what went in at this fill. Sacks are converted
  with "Sack size (kg)".
- Since: only when the kg cover a stated period that started earlier than the
  previous fill row ("25 sacks since June"). Otherwise empty.
- Level after: the store or hopper level after the fill, in the owner's own
  words ("full", "to the mark"). Two fills that end at the same level give an
  exact consumption figure for the time between them; anything else is marked
  approximate.
- Level (sacks) and Level before fill (sacks): optional, for a store read on
  a sack scale. "Level (sacks)" is the number of sacks in the store as read
  at this row, after any fill in it; "Level before fill (sacks)" is read just
  before filling, on a fill row only. A level read between fills is a row of
  its own. The script then gives cumulative consumption at each reading, the
  rate between readings and the slope through them (approximate), alongside
  the fill-to-fill figures.
- Measure the level the same way every time. One way: before filling, run
  the suction manually so the boiler's own hopper is full, then fill the
  store and read the level. This is an owner practice, not printed in the
  manual. A fill where it was not done says so in Note.
- Pellet product: the brand and product name on the sack ("ENplus A1, brand
  X"), so a change in consumption can be tied to a change of pellets. Not the
  shop or supplier. Optional column; an older logbook without it stays valid.
- Event: "reset Betrieb-STD" or "reset Aschenlade" when a counter was set to
  zero. The counter values in that row are the values just BEFORE the reset;
  leave them empty if they were not read, and the script will mark a gap.

| Date | Time | Betrieb-STD | Aschenlade aktuell | Pellets added (kg) | Sacks | Since | Level after | Level (sacks) | Level before fill (sacks) | Pellet product | Event | Source | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Service done

What was actually done, when, and by whom (owner or technician, no names).

- Task: an ID from "Service plan", or free text for anything else.
- Action: emptied, cleaned, inspected, lubricated, replaced, repaired,
  serviced, fault cleared.
- F-code: the error number shown, if this was a fault (F20, F5, ...).
- Condition: what was found, if anything: ok, light, heavy. This is what lets
  the script see whether an interval is too long.

| Date | Task | Action | F-code | Betrieb-STD | Condition | By | Source | Note |
|---|---|---|---|---|---|---|---|---|

## Service plan

Planned maintenance. One row per task and interval; a changed interval gets a
new row with a later "Valid from", and the old row stays.

- Trigger: time, hours, time|hours (whichever comes first), or counter (the
  controller's own Aschenlade counter).
- Interval: "1 w", "1 mo", "12 mo", "3 y", "500 h", or "12 mo | 2000 h". A dash
  means the documents give no number: the owner chooses one, or it stays open.
- Basis: Manual, TRVB, Owner or Predictive, then the anchor. A Manual interval
  printed as "mind. 1x jährlich" is a ceiling. An Owner or Predictive row may
  shorten it, never lengthen it; the script refuses a plan that does.
- Predictive rows are added only after the owner has seen the script's
  forecast and said yes.

| ID | Task | Trigger | Interval | Basis | Valid from | Note |
|---|---|---|---|---|---|---|
| SAUGZUG | Saugzug reinigen und kontrollieren | time | 12 mo | Manual [L&S Putzanleitung, S. 1] | | "mind. 1x jährlich": ceiling. Also check after every Rauchrohr cleaning |
| PUTZMECH | Putzmechanik reinigen und kontrollieren | time | 12 mo | Manual [L&S Putzanleitung, S. 1] | | "mind. 1x jährlich": ceiling |
| WT | Wärmetauscher reinigen und kontrollieren | time | 12 mo | Manual [L&S Putzanleitung, S. 1] | | "1x Jährlich" |
| BRENNRAUM | Brennraum reinigen und kontrollieren | time | 12 mo | Manual [L&S Putzanleitung, S. 1] | | "mind. 1x jährlich": ceiling |
| ZAHNRAD | Zahnräder kontrollieren, nach Bedarf schmieren | time | 12 mo | Manual [L&S Putzanleitung, S. 1] | | "1x jährlich" |
| RAUCHROHR | Rauchrohr kontrollieren | time | - | Manual [L&S Putzanleitung, S. 1] | | GAP: printed only "regelmäßig". The owner chooses an interval |
| ASCHE | Aschenlade entleeren, Zähler zurücksetzen | counter | Aschenlade setting | Manual [SL-P BA 2008, Kap. 5, S. 1–2] | | Three printed sources disagree: counter (Kap. 5), "im Winter monatlich" [Kap. 3, S. 2], "nach Bedarf" [L&S Putzanleitung, S. 1]. Not reconciled |
| SICHT | Wöchentliche Sichtkontrolle, Anlage und Lager | time | 1 w | TRVB [TRVB H 118 (2003), Anhang 2/2, S. 27] | | Third-party directive, during the heating season |
| TRVB-MON | Monatliche Kontrollen (12 Punkte) | time | 1 mo | TRVB [TRVB H 118 (2003), Anhang 2/2, S. 27] | | Third-party directive, during the heating season |
| WARTUNG | Wartung durch eine fachkundige Person | time | - | TRVB [TRVB H 118 (2003), Anhang 2/2, S. 27] | | GAP: "≤ 150 KW alle 3 Jahre" is printed, but whether it applies to an SL-P is not stated (verification.md line 23). Kap. 1, S. 2 recommends a Wartungsvertrag |
