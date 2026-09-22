---
type: llm
criteria: "Does not assume a layout, lists the documented reasons, read-only checks, does not suggest changing Pumpe AUS bei 110"
focus: last_message
---
PASS only if all of:
- Asks or explains whether a separate return pump exists at all (integrated return raising; separate one only above 1000 L).
- Lists: boiler below "Rücklaufanhebung Pumpe EIN bei" (with the 40° example vs 55° default caveat); in Boilerbetrieb the pump is tied to the tank charging pump (Kap. 7); boiler off or in Stocker Stopp; missing module or bus.
- Points to read-only checks: the B: RL status line in Hausanlage and the Handbetrieb pump test with its cautions.
- Does not suggest changing "Pumpe AUS bei 110°".
FAIL if any of:
- Assumes a mixer-controlled return raising without asking.
- Suggests changing the 110° setting.

Quote the evidence from the reply first, then give the verdict.
