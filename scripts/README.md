# Scripts

Repository tooling for Brumel. All scripts target **Python 3.10+** and use only the
**standard library**, so they run the same on Windows, Linux and in CI without
installing anything.

> These scripts do **not** download or build Chromium. Fetch and build tooling will
> be added in Phase 1 (Technical Foundation). See
> [BUILDING.md](../docs/development/BUILDING.md).

| Script | Purpose | Typical use |
|---|---|---|
| [`validate_docs.py`](validate_docs.py) | Checks that relative links and images in every Markdown file resolve. Validates `docs/product/catalog/features.json` and `epics.json` against the catalog schema: IDs, enums, references, epic membership, and coverage of the 52 research proposals. | `python3 scripts/validate_docs.py` (add `--links-only` or `--catalog-only`) |
| [`catalog/render_features.py`](catalog/render_features.py) | Generates the human-readable [FEATURES.md](../docs/product/FEATURES.md) from the JSON catalog. `--check` fails if the committed file is stale. | `python3 scripts/catalog/render_features.py` and, in CI, `--check` |
| [`upstream/check_upstream.py`](upstream/check_upstream.py) | Compares the pinned Chromium version in [`config/upstream.json`](../config/upstream.json) with the current upstream stable release. Reports only and never downloads source. | `python3 scripts/upstream/check_upstream.py` |

## Conventions

- Every script starts with an SPDX header (`SPDX-License-Identifier: MPL-2.0`).
- Scripts exit with a non-zero status on failure so CI can rely on them.
- Network access is allowed only where the script's purpose requires it, such as
  checking upstream versions. Nothing is sent except the request itself.
- Tests live in [`tests/`](../tests/README.md).
