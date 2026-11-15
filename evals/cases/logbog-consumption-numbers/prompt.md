---
name: logbog-consumption-numbers
tags: [regression, logbog, deterministic]
runs: 3
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
expected_outcome: "Runs the script and quotes 1.5 kg/h from exact intervals, n=3."
---
Hvor mange kg piller bruger kedlen pr. driftstime?
