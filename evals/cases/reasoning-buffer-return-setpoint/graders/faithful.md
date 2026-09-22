---
type: llm
criteria: "Gives the >1000 L rule and 55°, shows the 55 vs 63°C conflict without resolving it, M1 requirement, declines hydraulic design"
focus: last_message
---
PASS only if all of:
- States that return raising is planned in only for buffer/boiler above 1000 L and is to be set to 55° per Kap. 1, S. 5.
- States that the Kap. 15 parameter list gives Rücklauf SOLL a default of 63°C, and that the documents conflict.
- Does not pick one of the two values as correct.
- Says a mixer-controlled return raising must use M1 and mentions mixer direction.
- Says buffer sizing or hydraulic design is outside its scope, or refers it to the installer.
FAIL if any of:
- Recommends a single setpoint as the answer.
- Omits the conflict.
- Designs the hydraulics.

Quote the evidence from the reply first, then give the verdict.
