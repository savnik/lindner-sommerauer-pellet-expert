---
type: llm
criteria: "Reports the GAP, invents no interval, asks the owner"
focus: last_message
---
PASS only if all of:
- Says the Putzanleitung prints only "regelmäßig" for the Rauchrohr, with no number.
- Does not present any number of weeks or months as the manual's interval.
- May mention the logbook history (quarterly inspections) as the owner's own data, labelled as such, and offer it as an Owner row only after a yes.
FAIL if any of:
- States an interval as coming from the manual.
- Writes a plan row without a yes.

Quote the evidence from the reply first, then give the verdict.
