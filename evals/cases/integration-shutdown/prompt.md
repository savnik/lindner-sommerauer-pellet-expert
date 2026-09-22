---
name: integration-shutdown
tags: [judged, integration]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill, Write]
expected_outcome: "Five cases, inference labelled, asks which."
---
What is the proper shutdown procedure for the heating system?
