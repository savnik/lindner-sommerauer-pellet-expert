# Failure taxonomy

One row per failure mode observed in real transcripts or issues. New rows
are added before a fix is attempted; the case column is filled when a case
covers it. Codes are stable once assigned.

| Code | Failure mode | First seen | Source | Covered by |
|---|---|---|---|---|
| STALE-CITE | Cites a verification line as open after a later line closed it | 2026-09-22 | proxy run, installation-adaptation row 3 | status index in verification.md; `record-absent-factory-value` |
| NO-ROUTE-SEASON | No route to summer / season-end material; shutdown answer omits them | 2026-09-22 | proxy run, integration row 1 | routing row; `integration-shutdown` |
| SCOPE-SILENT-REPORT | Feedback drafted for an out-of-scope product without saying so | 2026-09-22 | proxy run, feedback row 2 | scope rule in feedback skill; `feedback-identifiers-out-of-scope` |
| OWNER-TOO-LONG | Owner-mode reply far beyond 300 words without a procedure | 2026-09-22 | live test | length rule in SKILL.md; `length-owner-mode` |
