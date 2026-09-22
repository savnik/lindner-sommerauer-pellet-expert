---
name: record-absent-factory-value
tags: [regression, record, deterministic]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill, Write]
expected_outcome: "No record: gives the per-model row, warns Leistung is a setting, offers a record."
---
What is the factory Förderzeit Soll for my boiler?
