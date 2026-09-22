---
name: feedback
description: "Report a problem with the pellet-expert plugin as a GitHub issue: a wrong or unhelpful answer, a missing topic, an unsafe suggestion, a confusing reply. Use when the user says an answer was wrong, asks how to report a problem, or invokes /pellet-expert:feedback. Shows the exact text first and posts only with the user's yes."
---

# Report a problem with pellet-expert

This is the only part of the plugin that sends anything anywhere. It posts a
public GitHub issue at https://github.com/savnik/lindner-sommerauer-pellet-expert/issues,
and only after the user has seen the exact text and said yes.

## Rules that never bend

1. **Show the complete issue text before anything is posted.** Title, labels,
   body. Then ask. No yes, no post.
2. **Nothing from the installation record goes in verbatim.** The record is
   private. Take at most three generic facts from it, and only if relevant:
   model (e.g. SL-P 12), firmware version string, and the layout in one
   phrase (e.g. "one mixed circuit, hot-water tank, no buffer"). Never
   settings values, dates, event history, or the record's open questions.
3. **No identifiers.** No names, addresses, phone numbers, email addresses,
   serial numbers, installer or company names, file paths, or usernames. If
   the user's own words contain any, remove them and say so.
4. **Say that the issue is public.** Once, plainly, before asking for the yes.
5. **The user can edit.** If they change the text, use their version, still
   subject to rules 2 and 3.

## What goes in the issue

Build the body from the conversation. Keep it under 300 words. Sections:

- **What I asked** — the user's question, verbatim if it contains no
  identifiers, otherwise paraphrased.
- **What the plugin answered** — two or three sentences summarising the
  answer, including any anchors it cited (e.g. `[SL-P BA 2008, Kap. 7, S. 3]`).
- **What was wrong or missing** — the user's view, in their words where
  possible.
- **What the right answer would have been** — only if the user knows; say
  "unknown" otherwise. A page reference to the manual, if they have one, is
  the most useful thing they can give.
- **Boiler** — model and firmware if known from the record or the user; else
  "not stated".
- **Plugin version** — from `.claude-plugin/plugin.json` next to this skill.
- **Where it ran** — Claude Code or Cowork, if known.

Title: one line, under 80 characters, starting with the label word, e.g.
`wrong-answer: F19 remedy omitted the Saugintervall link`.

Labels, pick one primary:

| Label | When |
|---|---|
| `wrong-answer` | The answer was factually wrong or cited the wrong place |
| `missing-coverage` | The documents in the plugin do not cover the question |
| `safety` | The plugin suggested something unsafe, or missed a danger signal |
| `usability` | Right answer, but too long, unclear, wrong language, wrong mode |
| `other` | Anything else |

Add `safety` as a second label whenever safety is involved, even if the
primary is different.

## Reports about things outside the plugin's scope

If the problem is that the plugin does not cover another manufacturer, another
Lindner & Sommerauer product line, or a topic the main skill lists as out of
scope, say so first: that is by design, not a fault. Then ask whether the user
still wants to file it as a coverage request. Such requests are useful to the
maintainer as a signal of demand, so file it if they say yes, labelled
`missing-coverage`, with one sentence noting it is outside the current scope.

## How to post

Try, in this order, and tell the user which one you are using:

1. **GitHub CLI**, if a shell is available and `gh auth status` succeeds:

   ```
   gh issue create --repo savnik/lindner-sommerauer-pellet-expert --title "<title>" --label "<label>" --body-file <tempfile>
   ```

   Write the body to a temporary file first; never pass it inline. Report the
   issue URL back.

2. **Pre-filled link**, otherwise (no shell, no `gh`, not logged in, or the
   user prefers it). Build a URL of the form

   ```
   https://github.com/savnik/lindner-sommerauer-pellet-expert/issues/new?title=<url-encoded title>&labels=<label>&body=<url-encoded body>
   ```

   and give it to the user to open. They submit it themselves from their own
   GitHub account. Keep the body short enough that the link works; if it is
   long, put the body in the message for them to paste instead. Tell them a
   GitHub account is needed, and that the issue will carry their GitHub name.

Never post from any account other than the user's own. Never create labels,
edit other issues, or do anything on the repository beyond creating this one
issue.

## After posting

Offer one line to the user's installation record, if they keep one, under
Events: the date, "reported to plugin maintainer: <title>", and the issue
number. Only with their yes, like every record write.

## If the user is reporting a safety problem

Handle the safety situation first, as the main skill's Safety section says.
The report can wait. Do not delay "people out, technician called" for an
issue form.
