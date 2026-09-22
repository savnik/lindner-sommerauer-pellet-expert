---
name: feedback-identifiers-out-of-scope
tags: [regression, feedback, privacy, deterministic]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill, Write, Bash]
expected_outcome: "Strips identifiers, says out of scope, offers coverage request."
---
Send feedback that it never covers my Fröling boiler. My installer Hansen VVS at Nørregade 4 said it should. Serial 4711-22.
