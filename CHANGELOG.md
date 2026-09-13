# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - Unreleased

### Added

- Reference content from the SL-P 8/12/15/25 (Modell 2008) Betriebsanleitung,
  ingested with the `ingest-document` skill: hydraulics, components, technical
  data, commissioning and room-unit notes in `system-integration.md`; all
  controller menus, parameter lists, service parameters and error messages
  F2–F167 in `parameters.md`. Coverage manifests filled; 21 uncertain readings
  logged in `verification.md`.
- Marketplace and plugin manifests.
- Skill skeleton `lindner-sommerauer` with section headers and empty
  reference stubs carrying coverage manifests.
- Development skill `ingest-document`.
- Eval sets: out-of-scope, safety, personal-data (written); integration and
  manual-reasoning (stubs).
