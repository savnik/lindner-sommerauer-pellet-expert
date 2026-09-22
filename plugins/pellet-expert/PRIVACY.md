# Privacy policy

Applies to the `pellet-expert` plugin and its `lindner-sommerauer` skill.
Last updated 2026-09-22 (feedback skill added).

## What the plugin collects

Nothing on its own. The plugin contains no code that runs by itself, no hooks,
no analytics and no telemetry. It consists of instructions and reference text
that Claude reads locally.

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
it. You can read, edit or delete it at any time; deleting the file removes
everything the plugin has stored.

## What the maintainer receives

Nothing from the plugin. The maintainer has no access to your conversations,
your files or your installation record. If you open an issue on GitHub, what
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
