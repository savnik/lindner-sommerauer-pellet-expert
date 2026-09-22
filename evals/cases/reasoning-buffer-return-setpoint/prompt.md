---
name: reasoning-buffer-return-setpoint
tags: [judged, reasoning]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill, Write]
expected_outcome: "Rule, conflict left open, M1, scope boundary."
---
I'm adding a 1500 litre buffer. What return temperature should the return raising be set to?
