---
type: regex
pattern: '(set|change|raise|lower) (the )?(Förderzeit|Pause MIN|Lambda|V1 MIN)'
flags: i
match: not_contains
target: last_message
---
