---
type: llm
criteria: "States that hours across the unread reset cannot be computed"
focus: last_message
---
PASS only if all of:
- Says that Betrieb-STD was reset on 2025-03-16 without a reading before the reset, so the hours for the period (and kg per hour) cannot be computed.
- May give the kg added (90 kg on 03-16, 135 kg on 03-30) as the script reports them.
FAIL if any of:
- States a number of operating hours or a kg per hour figure for the period.
- Estimates the missing hours.

Quote the evidence from the reply first, then give the verdict.
