# Scripts

Repository tooling for Brumel. All scripts target **Python 3.10+** and use only the
**standard library**, so they run the same on Windows, Linux and in CI without
installing anything.

> `fetch.py`, `patches.py` and `build.py` can download, change a Chromium checkout and
> build, but **only with `--execute`**. Without it they print their plan and stop. They
> have not yet been run against a real Chromium checkout. See
> [BUILDING.md](../docs/development/BUILDING.md).

| Script | Purpose | Typical use |
|---|---|---|
| [`validate_docs.py`](validate_docs.py) | Checks that relative links and images in every Markdown file resolve. Validates `docs/product/catalog/features.json` and `epics.json` against the catalog schema: IDs, enums, references, epic membership, and coverage of the 52 research proposals. | `python3 scripts/validate_docs.py` (add `--links-only` or `--catalog-only`) |
| [`catalog/render_features.py`](catalog/render_features.py) | Generates the human-readable [FEATURES.md](../docs/product/FEATURES.md) from the JSON catalog. `--check` fails if the committed file is stale. | `python3 scripts/catalog/render_features.py` and, in CI, `--check` |
| [`fetch.py`](fetch.py) | Fetches the Chromium tag pinned in `config/upstream.json` with depot_tools (shallow clone, unmanaged `.gclient`, `gclient sync --no-history`, hooks) and records the resolved commit. Checks disk space, tools and the path first. | `python3 scripts/fetch.py --checkout C:\src\brumel` (add `--execute` to download) |
| [`patches.py`](patches.py) | Validates and measures the patch series. Applies it to a checkout as one commit per patch, and refreshes patch files from those commits ([ADR-0013](../docs/architecture/adr/0013-git-backed-patch-tooling.md)). | `python3 scripts/patches.py check`; `apply` / `refresh --checkout DIR` |
| [`build.py`](build.py) | Composes `args.gn` from the profiles in [`config/gn/`](../config/gn/dev.gn), rejects insecure settings, runs `gn gen` and `autoninja`. | `python3 scripts/build.py check`; `build --checkout DIR --profile dev` |
| [`overlay.py`](overlay.py) | Validates Brumel's own sources in [`src/`](../src/README.md) (SPDX headers, no symlinks, no Windows-reserved names) and mirrors them into a checkout as `//brumel`, excluded from the checkout's Git. | `python3 scripts/overlay.py check`; `sync --checkout DIR` |
| [`bench/harness.py`](bench/harness.py) | Prototype benchmark harness for stock Chromium-based browsers: startup, tab load, memory and idle CPU with N tabs, on a synthetic corpus served on 127.0.0.1 ([BENCHMARKS.md §6.1](../docs/benchmarks/BENCHMARKS.md#61-prototype-harness-in-development)). | `python3 scripts/bench/harness.py --list --output x.json`; `--browser chrome --tabs 1,10,25 --runs 10 --output results.json` |
| [`brumeltools/`](brumeltools/__init__.py) | Shared helpers: upstream pin loading, printable command plans, Git calls. | Imported by the scripts above |
| [`upstream/check_upstream.py`](upstream/check_upstream.py) | Compares the pinned Chromium version in [`config/upstream.json`](../config/upstream.json) with the current upstream stable release. Reports only and never downloads source. | `python3 scripts/upstream/check_upstream.py` |
| [`upstream/render_issue.py`](upstream/render_issue.py) | Renders the body of the "Upstream update available" issue from `check_upstream.py --json` and the ungoogled-chromium tag list. It validates every version string first. Used by the scheduled [Upstream check](../.github/workflows/upstream-check.yml) workflow. | `python3 scripts/upstream/render_issue.py check.json --ungoogled-tags tags.json` |

## Conventions

- Every script starts with an SPDX header (`SPDX-License-Identifier: MPL-2.0`).
- Scripts exit with a non-zero status on failure so CI can rely on them.
- Network access is allowed only where the script's purpose requires it, such as
  checking upstream versions. Nothing is sent except the request itself.
- Tests live in [`tests/`](../tests/README.md).
