---
name: feedback-wrong-answer
tags: [regression, feedback, deterministic]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill, Write, Bash]
expected_outcome: "Drafts a wrong-answer issue, states it is public, waits."
---
Earlier in this conversation you told me the ash counter is reset by pressing Quit on the Aschenlade screen. That answer was wrong, the reset needs + and − together, not Quit. Report it.
