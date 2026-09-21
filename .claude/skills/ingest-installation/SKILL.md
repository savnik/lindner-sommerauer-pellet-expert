---
name: ingest-installation
description: "Development skill (not installed for users). Build or extend a private installation record from the owner's own papers: annotated manual scans, commissioning sheets, photos of the controller display, notes. Use when asked to create, fill or update an installation record from documents. Counterpart of ingest-document: that skill keeps installation detail out of the public references; this one gives it a private home."
---

# Build an installation record from the owner's papers

## First rule: stop, do not resolve

Handwriting is the main source here and it is often ambiguous. A digit that
could be 3 or 8, a value written between two display boxes, a crossed-out
number with another beside it, a tick whose meaning is unknown: none of these
is resolved by you. Each goes under **Open questions** in the record with
every plausible reading and what would settle it (usually: read it off the
display). A wrong setpoint in a record is worse than a missing one, because
the expert skill will trust it.

## Second rule: the output never enters this repo

The record is written to a path Peter gives, outside the repo tree. If no path
is given, stop and ask. Never write it under the repo, never stage it, never
quote its contents in a commit message, changelog, reference file or eval.
`pellet-installations/` is git-ignored as a backstop, not as permission.

## Inputs

- One or more source documents, outside the repo tree.
- The output path and the record label (a nickname, not a name or address).
- An existing record at that path, if any. Extend it; never start over.

## Steps

1. **Read every page fully before writing.** Separate printed content from
   everything added by hand or filled into a form.
2. **Start from the template** at
   `plugins/pellet-expert/skills/lindner-sommerauer/templates/installation-record.md`.
   Keep its section order and its source codes.
3. **Leave identifiers out.** No names, addresses, phone numbers, serial
   numbers, installer or company names, signatures. They are not needed to
   answer a heating question. Report which types you left out.
4. **Transcribe handwritten values into "Settings as found".** Menu and
   parameter names exactly as printed on the page next to the annotation.
   Source code `P`. Date: the date written on the page if there is one,
   otherwise "undated" and an Open question. A value written on paper years
   ago is evidence of what was once set, not of what is set now; say so in
   the Note column.
5. **Identity and layout** come only from what the papers state. A circled
   model number is `P`. A layout you deduce from which menu items are ticked
   is `I`, and goes in with that code or not at all.
6. **Do not copy printed manual content into the record.** Defaults, ranges
   and explanations live in the public references. The record holds only what
   is particular to this installation.
7. **Compare, do not correct.** Where a found value lies outside the printed
   range, or differs from the factory value for the stated model, add an Open
   question saying so. Do not change the value and do not advise.
8. **Report.** Record path, sections filled, number of rows by source code,
   number of Open questions, identifier types left out, pages that yielded
   nothing.

## Never

- Never guess at handwriting.
- Never write the record, or anything derived from it, into the repo.
- Never touch the public reference files from this skill. If a paper reveals a
  gap or error in them, tell Peter; fixing it is an `ingest-document` job with
  a document anchor.
