---
name: record-timer-with-room-unit
tags: [regression, record, deterministic]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill, Write]
expected_outcome: "Uses the record's room unit to route to UWP lock times, not Uhrzeitbetrieb."
---
I want the heating off between 23:00 and 05:00. Can I just use Uhrzeitbetrieb?
