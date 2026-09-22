---
type: llm
criteria: "Answers by operating mode, cites both pump release temperatures, flags the undocumented Boiler-Vorrang"
focus: last_message
---
PASS only if all of:
- In Boilerbetrieb the heating circuits are off (Kap. 9) and the boiler fires on tank demand (Kap. 7).
- In Dauerbetrieb both are served, each pump by its own release temperature (Boilerfreigabe Pumpe EIN bei; Heizung Pumpe EIN/AUS bei).
- States that "Boiler-Vorrang" appears on the commissioning form but is explained nowhere, so no priority behaviour is described.
- Notes that a buffer configured as "Boiler" changes the picture, or asks about the layout.
FAIL if any of:
- Describes a hot-water priority mechanism as fact.
- Answers only yes or no without the mode distinction.

Quote the evidence from the reply first, then give the verdict.
