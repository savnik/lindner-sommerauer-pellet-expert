# Logbook: testkedel

<!-- FICTIONAL fixture for evals/unit/test_logbog.py and the logbog eval cases.
     Every number is invented. It is not any real installation's data. -->

schema: 1
installation record: testkedel.md
created: 2025-01-05

## Constants

| Item | Value | Date | Source |
|---|---|---|---|
| Sack size (kg) | 15 | 2025-01-05 | O |
| Aschenlade setting (h) | 150:00 | 2025-01-05 | D |

## Readings

| Date | Betrieb-STD | Aschenlade aktuell | Pellets added (kg) | Sacks | Since | Level after | Event | Source | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2025-01-05 | 10000h00 | 20:00 | 150 | | | full | | D | |
| 2025-01-19 | 10100h00 | 60:00 | 150 | | | full | | D | |
| 2025-02-02 | 10200h00 | 100:00 | | 10 | | full | | D | |
| 2025-02-16 | 10300h00 | 140:00 | 150 | | | full | reset Aschenlade | D | ash emptied |
| 2025-03-02 | 10380h00 | 30:00 | 120 | | | half | | D | |
| 2025-03-16 | | | 90 | | | full | reset Betrieb-STD | D | counter not read before the reset |
| 2025-03-30 | 50h00 | 70:00 | 135 | | | full | | D | |
| 2025-09-01 | 300h00 | 90:00 | | 25 | 2025-06-01 | | | O | summer, from memory |
| 2025-09-10 | | | 1000 | | | | | I | guess, context only |

## Degree days

| From | To | Degree days | Source | Note |
|---|---|---|---|---|
| 2025-01-01 | 2025-01-31 | 465 | P | fictional monthly total |
| 2025-02-01 | 2025-02-28 | 392 | P | |
| 2025-03-01 | 2025-03-31 | 341 | P | |

## Service done

| Date | Task | Action | F-code | Betrieb-STD | Condition | By | Source | Note |
|---|---|---|---|---|---|---|---|---|
| 2022-10-01 | SAUGZUG | cleaned | | | light | technician | P | |
| 2023-10-01 | SAUGZUG | cleaned | | | light | technician | P | |
| 2024-03-01 | WT | cleaned | | | heavy | owner | O | |
| 2024-09-01 | WT | cleaned | | | heavy | owner | O | |
| 2024-10-01 | SAUGZUG | cleaned | | | ok | technician | P | |
| 2025-01-10 | RAUCHROHR | inspected | | | light | owner | D | |
| 2025-02-14 | ASCHE | fault cleared | F20 | 10290h00 | | owner | D | ash drawer full |
| 2025-02-16 | ASCHE | emptied | | 10300h00 | | owner | D | |
| 2025-03-01 | WT | cleaned | | | heavy | owner | D | |
| 2025-03-30 | LAMBDA | inspected | | 50h00 | ok | owner | D | |
| 2025-04-10 | RAUCHROHR | inspected | | | light | owner | D | |
| 2025-07-10 | RAUCHROHR | inspected | | | light | owner | D | |
| 2025-09-01 | WT | cleaned | | | heavy | owner | D | |
| 2025-10-01 | SAUGZUG | cleaned | | | ok | technician | P | |
| 2025-10-10 | RAUCHROHR | inspected | | | light | owner | D | |
| 2025-11-03 | TRVB-MON | inspected | | | ok | owner | D | |
| 2025-11-03 | SICHT | inspected | | | ok | owner | D | |
| 2025-11-10 | SICHT | inspected | | | ok | owner | D | |

## Service plan

| ID | Task | Trigger | Interval | Basis | Valid from | Note |
|---|---|---|---|---|---|---|
| SAUGZUG | Saugzug reinigen und kontrollieren | time | 12 mo | Manual [L&S Putzanleitung, S. 1] | | ceiling |
| PUTZMECH | Putzmechanik reinigen und kontrollieren | time | 12 mo | Manual [L&S Putzanleitung, S. 1] | | ceiling |
| WT | Wärmetauscher reinigen und kontrollieren | time | 12 mo | Manual [L&S Putzanleitung, S. 1] | | |
| WT | Wärmetauscher reinigen und kontrollieren | time | 6 mo | Owner | 2025-10-01 | heavy deposits every time |
| RAUCHROHR | Rauchrohr kontrollieren | time | - | Manual [L&S Putzanleitung, S. 1] | | GAP |
| ASCHE | Aschenlade entleeren | counter | Aschenlade setting | Manual [SL-P BA 2008, Kap. 5, S. 1–2] | | |
| SICHT | Wöchentliche Sichtkontrolle | time | 1 w | TRVB [TRVB H 118 (2003), Anhang 2/2, S. 27] | | |
| TRVB-MON | Monatliche Kontrollen | time | 1 mo | TRVB [TRVB H 118 (2003), Anhang 2/2, S. 27] | | |
| LAMBDA | Lambdasonde kontrollieren | time\|hours | 12 mo \| 1000 h | Owner | | owner's own choice |
