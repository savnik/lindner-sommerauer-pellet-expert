---
type: llm
criteria: "Full owner-level walkthrough with the + and − reset, the message variants, and the 150 vs 200 inconsistency passed on"
focus: last_message
---
PASS only if all of:
- Says to switch to Dauerbetrieb, page to Aschenlade, press + and − together (Kap. 5, S. 1).
- Says that when "Aschenlade voll" is showing, + and − together works directly and Quit only hides the message (Kap. 5, S. 2).
- Mentions that the boiler stops with error 20 when the set value is exceeded by 50.
- Passes on the 150 hours vs default 200 inconsistency without resolving it.
- Warns that ash may be hot.
FAIL if any of:
- Says Quit resets the counter.
- Omits the + and − together step.

Quote the evidence from the reply first, then give the verdict.
