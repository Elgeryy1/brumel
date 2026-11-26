# CLAUDE.md

Claude Code: the shared rules for all AI agents live in AGENTS.md and are imported
here.

@AGENTS.md

## Claude-specific notes

- Read the relevant document before editing it, and keep cross-document consistency:
  feature IDs, phase names, status labels and decisions (ADRs) must match everywhere.
- The feature catalog (`docs/product/catalog/features.json`) is the source of truth.
  After editing it, run `python3 scripts/catalog/render_features.py`, then
  `python3 scripts/validate_docs.py`.
- Phase names (also GitHub milestones): Pre-development, Technical Foundation,
  Internal Alpha, Public Alpha, Public Beta, Version 1.0, Future Releases.
- Do not run long Chromium downloads or builds unless the owner asks. They take
  hours and tens of gigabytes.
- Use `gh` for GitHub operations. Do not change repository settings, the project
  board or visibility unless asked.
- When reporting results, separate what was verified from what was assumed.
