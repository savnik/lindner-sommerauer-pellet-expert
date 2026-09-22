# Privacy policy

Applies to the `pellet-expert` plugin and its `lindner-sommerauer` skill.
Last updated 2026-09-22.

## What the plugin collects

Nothing. The plugin contains no code that runs on its own, no hooks, no
network calls, no analytics and no telemetry. It consists of instructions and
reference text that Claude reads locally.

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
