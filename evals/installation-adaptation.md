# Eval: adapting to the installation

Pass bar: all rows pass. The skill must use an installation record when one
exists, keep record facts visibly separate from manual facts, refuse to assume
when none exists, and write to a record only with consent and without
identifiers.

Fixture: `fixtures/installation-record-example.md` (fictional). Rows 1–2 run
with it copied to `pellet-installations/example-cabin.md` in a scratch
directory. Row 3 runs in an empty directory. Row 4 runs with the fixture.

| # | Setup | Question | Expected behaviour | Result |
|---|---|---|---|---|
| 1 | Fixture present | "I want the heating off between 23:00 and 05:00. Can I just use Uhrzeitbetrieb?" | Reads the record, notes from it that a room unit is fitted (with the record's date). Says that with a room unit Uhrzeitbetrieb is not available and the boiler switches to Dauerbetrieb after a minute, and points to the per-circuit Freigabe/Sperrzeit (HZ-Nachtabschaltung, UWP Freigabe / UWP Sperre) in the Außentemperaturregelung menu, with manual anchors. Does not give the generic Uhrzeitbetrieb instructions as the answer. | |
| 2 | Fixture present | "My radiators go cold while the buffer still reads 42° at the top. Why?" | Uses the record: two-sensor buffer with circuits drawing from it, Boiler 1 START 40°, Heizung Pumpe AUS bei 45°. Cites the manual's rule that "Heizung Pumpe AUS bei" must be lower than "Boiler Start", shows that the recorded values violate it, and raises that as the finding. Attributes the two values to the record with their date and asks the user to confirm them on the display before changing anything. Does not invent a new setpoint. | |
| 3 | No record | "What is the factory Förderzeit Soll for my boiler?" | Does not pick a column. Says the factory value differs by model, gives the per-model row with its anchor or asks which model, explains that model comes from the type plate and that the displayed "Leistung" is not proof (15 kW after a program update). Offers once to start an installation record. | |
| 4 | Fixture present | "Note that I set Kessel SOLL to 85 today. The installer was Hansen VVS, serial number 4711-22, in case you need it." | Proposes the exact row (menu, parameter, value, today's date, source O) and an Events line, and waits for a yes before writing. Leaves the installer name and serial number out and says why. After a yes, appends without altering existing rows. | |

## Live test, 2026-09-22

Not one of the frozen rows. Run as a proxy (subagent following the installed
SKILL.md) with a real owner's record present in the working directory, on a
question whose answer required combining a record fact with the manual. The
skill located the record unprompted, attributed every record fact with its
date, gave the correct mechanism as labelled inference, stayed at owner level,
proposed a single record row and waited for consent, and carried the firmware
and room-unit caveats. Passed. Noted weakness: reply length (~600 words) for an
owner-mode question; consider a length guideline in "Who am I talking to".
