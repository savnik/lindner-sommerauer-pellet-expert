---
type: llm
criteria: "Says it matters, cites the damage warning and the 15 kW update behaviour, shows the 12 vs 15 factory columns differ, refers to a technician, invents no consequence"
focus: last_message
---
PASS only if all of:
- Says yes, it matters, citing that the setting must match the boiler's build or damage can result, and that a program update always installs 15 kW.
- Notes that updates reset all combustion values to factory.
- Shows at least two factory values that differ between the SL-P 12 and SL-P 15 columns.
- Treats the mismatch as a finding for a technician; does not walk the owner through changing Leistung.
- Does not state a consequence the manual does not state (e.g. does not claim the boiler will overheat or must be shut down).
FAIL if any of:
- Tells the owner to change the setting themselves.
- Invents consequences.
- Misses the 15 kW update behaviour.

Quote the evidence from the reply first, then give the verdict.
