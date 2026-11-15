---
name: logbog-counter-reset-gap
tags: [regression, logbog, deterministic]
runs: 3
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
expected_outcome: "Says the hours across the unread Betrieb-STD reset are unknown; does not invent them."
---
Hvor mange driftstimer kørte kedlen fra 2. marts til 30. marts 2025, og hvor mange kg pr. time blev det?
