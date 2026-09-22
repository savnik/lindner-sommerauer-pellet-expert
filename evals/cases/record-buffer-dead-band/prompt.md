---
name: record-buffer-dead-band
tags: [regression, record, deterministic]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill, Write]
expected_outcome: "Finds the 40/45 conflict from the record, cites the rule, asks for a fresh reading."
---
My radiators go cold while the buffer still reads 42° at the top. Why?
