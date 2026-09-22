---
type: llm
criteria: "Leads with the answer and stays near 300 words"
focus: last_message
---
PASS only if all of:
- The first two sentences already contain the key sequence (+ and − together on the Aschenlade screen).
- The whole reply is under about 350 words, or is a step-by-step procedure whose steps justify the length.
- There is no preamble about what the skill is or how it works before the answer.
FAIL if any of:
- The key sequence first appears after more than 100 words.
- The reply exceeds about 450 words without a step-by-step procedure.

Quote the evidence from the reply first, then give the verdict.
