# Privacy policy

Applies to the `pellet-expert` plugin and its `lindner-sommerauer`, `logbog`
and `feedback` skills.
Last updated 2026-11-15 (logbook skill added).

## What the plugin collects

Nothing on its own. The plugin contains no code that runs by itself, no hooks,
no analytics and no telemetry. It consists of instructions and reference text
that Claude reads locally, and one small local script
(`skills/logbog/scripts/logbog.py`). The script runs only when the logbook
skill calls it to compute figures, reads only the logbook file it is given,
writes nothing, uses no network and sends nothing.

The one way anything leaves your machine is the `feedback` skill, which you
invoke to report a problem with the plugin. It drafts a public GitHub issue,
shows you the complete text, and posts it only when you say yes, from your own
GitHub account. It is instructed to leave out names, addresses, serial numbers,
installer names, file paths and the contents of your installation record. You
can edit the text before it is posted, or decline.

## What it stores, and where

At your request, and only after you confirm each addition, the skill can write
an installation record: a plain Markdown file at `pellet-installations/<label>.md`
in the folder you are working in. The record is meant to hold technical facts
about your heating system (model, firmware, settings, events). The skill is
instructed not to record names, addresses, phone numbers, serial numbers or
installer names, and to leave them out if you supply them.

The file stays on your computer. The plugin never uploads, syncs or transmits
it. You can read, edit or delete it at any time.

The `logbog` skill can, in the same way, keep a logbook next to it at
`pellet-installations/logbog/<label>.md`: maintenance done, a maintenance plan,
counter readings and pellet fills. The same rules apply: only after you
confirm the exact rows, no names, addresses, phone numbers, serial numbers or
installer names ("by" is recorded only as owner or technician), never
uploaded. Deleting the two files removes everything the plugin has stored.

## What the maintainer receives

Nothing from the plugin. The maintainer has no access to your conversations,
your files, your installation record or your logbook. If you open an issue on GitHub, what
you write there is public and governed by GitHub's terms.

## Your conversations with Claude

Your conversations are handled by Anthropic under the terms and privacy policy
of the Claude product you use, not by this plugin. This plugin adds no
processing of its own.

## Reference material

The plugin's reference files are scrubbed transcriptions of manufacturer
documents. They contain no personal data, and the skill is instructed not to
speculate about where the source copies came from.

## Contact

Open an issue at https://github.com/savnik/lindner-sommerauer-pellet-expert/issues
