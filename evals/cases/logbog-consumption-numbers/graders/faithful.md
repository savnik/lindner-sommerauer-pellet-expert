---
type: llm
criteria: "Quotes the script's figure with its basis and the Betrieb-STD caveat"
focus: last_message
---
PASS only if all of:
- Gives 1.5 kg per operating hour as the median of exact intervals, with n = 3 (or says three intervals).
- Says the figure comes from the logbook via the script, not from the manual.
- Mentions that the manual does not say exactly what Betrieb-STD counts, or that it is "operating hours as displayed".
FAIL if any of:
- Gives a different headline figure, or one computed from approximate intervals or the source-I row.
- Compares with another installation or a general rule of thumb for pellet boilers.

Quote the evidence from the reply first, then give the verdict.
