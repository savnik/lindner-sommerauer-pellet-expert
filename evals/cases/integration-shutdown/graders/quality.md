---
type: llm
criteria: "Separates the cases (Aus key, main switch, maintenance, summer, season end) instead of one recipe, and asks which is meant"
focus: last_message
---
PASS only if all of:
- Says the manual has no shutdown chapter.
- Covers: stopping with the Aus key (with fan run-on); the main AUS switch and that it also cuts pumps while modules stay live; pulling the plug before maintenance; summer hot-water-only operation (Boilerbetrieb or Uhr-Boilerbetrieb); end-of-season cleaning.
- Advice on the order of steps that the manual does not print is labelled as inference.
- Asks which situation the user is in, or covers each briefly.
FAIL if any of:
- Gives a single numbered procedure as "the" shutdown.
- Omits the summer case or the season-end cleaning.
- Mixes emergency guidance in without a danger signal present.

Quote the evidence from the reply first, then give the verdict.
