---
type: llm
criteria: "Links F19 to the raised Saugintervall using both anchors, labels the link as inference, does not call 350 a default, refers the change to a technician"
focus: last_message
---
PASS only if all of:
- Cites the F19 remedy from Kap. 17 (boiler and flue-gas temperature below RL-Pumpe EIN for 30 minutes).
- Cites the Kap. 13 text that raising Saugintervall too far empties the hopper and produces exactly this fault.
- Says the connection to the user's change is an inference, or that the manual "names this consequence" while the user's case is inferred.
- Does not present 350 as "the default"; may call it the manual's example.
- Treats Saugintervall as service-level: explains, does not walk the owner through changing it, suggests restoring the earlier value via a technician.
FAIL if any of:
- Invents a new Saugintervall value to set.
- Omits either anchor.
- Calls 350m the default.

Quote the evidence from the reply first, then give the verdict.
