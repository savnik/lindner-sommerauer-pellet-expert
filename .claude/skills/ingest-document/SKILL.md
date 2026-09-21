---
name: ingest-document
description: "Development skill (not installed for users). Ingest one Lindner & Sommerauer source document (manual page, screenshot, photo, PDF) into the pellet-expert reference files: choose the target file, scrub identifiers, update the coverage manifest, write gaps explicitly, format anchors, and log uncertain readings. Use when asked to ingest, transcribe, or add a manual or document to the references."
---

# Ingest a source document

## First rule: stop, do not resolve

When anything in the source is not certain, you stop and log it. You never
best-guess. This applies to, at minimum:

- a value that is illegible, partially cut off, or could be read two ways
- a menu path that is ambiguous, incomplete, or differs between screenshots
- a parameter whose model or firmware applicability is not stated on the page
- a unit that is missing or implied
- a page whose model designation is not printed on it

For each such case you write one line to `verification.md` (see step 7),
leave a gap marker in the reference file at the place the content would go,
and tell Peter what was skipped and why at the end of the run. You do not
fill the gap from other pages of the same document, from other documents,
or from your own training knowledge. The gap is the deliverable.

## Inputs

- The path to one source document, supplied by Peter. Source PDFs and photos
  live outside the repo tree and are never copied into it.
- The model and firmware the document applies to, as stated by Peter or
  printed on the document. If neither states it, stop (first rule).

## Steps

1. **Read the document once, fully, before writing anything.** Note the
   model, firmware, and section numbers as printed. If the document covers
   more than one model, list them.

2. **Choose the target reference file.** Hydraulics, buffer, return
   temperature, sensors, wiring topology and commissioning sequences go to
   `references/system-integration.md`. Controller menus, parameter names,
   ranges, defaults and service-level settings go to
   `references/parameters.md`. If content does not fit either file, stop and
   say so rather than creating a new file — new files are a plan decision.

3. **Scrub identifiers before writing a single line.** Remove serial
   numbers, customer names, addresses, phone numbers, installer names and
   stamps, dates of installation, file paths, and anything that ties the
   page to a specific installation or person. Photos of a controller screen
   are transcribed, not embedded. If you are unsure whether something is an
   identifier, treat it as one and log it.

4. **Write the content in the reference file's existing structure.** Keep
   the manufacturer's section numbering and terminology. Do not restate in
   your own words where the manual's wording is clear. Do not add
   explanations, context, or advice that is not on the page.

5. **Format every anchor.** Each fact you add gets an anchor that lets the
   skill cite it: document, section, and page as printed. The format is
   `[<short document name>, Kap. <chapter>, S. <page>]` with chapter and page
   as printed, e.g. `[SL-P BA 2008, Kap. 7, S. 3]`. For an unpaginated
   document use `scan S. <n>` and say so in the manifest. Each new document
   gets a short name, declared in the manifest as `source document N`.

6. **Write gaps down explicitly.** Wherever the document is silent, cut off,
   or skipped per the first rule, leave a gap marker in place: a blockquote
   starting with `> GAP:` that says what is missing, why, and which
   `verification.md` line covers it. When a later ingest closes a gap, replace
   the marker with a sentence saying it was closed and by which document. A gap that is
   not written down is indistinguishable from coverage.

7. **Append uncertain readings to `verification.md`** in the skill
   directory (create it if missing). One line each: target file, location,
   what was seen, why it is uncertain, what would resolve it. Never delete
   or edit existing lines in that file.

8. **Update the coverage manifest** at the top of the target file. Add the
   model and firmware if new, and list the sections now covered and the
   sections seen but not covered. Content without a manifest update is
   not finished.

9. **Report.** End with: the target file, sections added, sections skipped
   and why, the number of lines appended to `verification.md`, and
   identifiers scrubbed (by type, never by value).

## Never

- Never fill a gap from memory or from general knowledge of pellet boilers.
- Never merge two documents' values into one entry without both anchors.
- Never mark something as covered because it "should be" in the manual.
- Never touch `SKILL.md` or the eval files — those are separate steps.
