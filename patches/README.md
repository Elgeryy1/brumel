# Patches

This directory will contain the ordered series of patches that Brumel applies on top of the pinned Chromium tag ([`config/upstream.json`](../config/upstream.json)). The series holds 15 selected ungoogled-chromium patches ([why these](../docs/privacy/DEGOOGLING_AUDIT.md#selection-of-ungoogled-chromium-patches)) and one branding patch. All of them apply to the pin in order, but they have **not yet been built**. Brumel is in pre-development.

Background: [ADR-0003](../docs/architecture/adr/0003-patch-based-repository.md) · [Upstream Strategy](../docs/architecture/UPSTREAM_STRATEGY.md) · [Licensing](../docs/architecture/adr/0004-licensing.md)

## Layout

```text
patches/
├── series                      # application order (created with the first patch)
├── upstream-ungoogled/         # patches imported from ungoogled-chromium
│   └── <original path>.patch   # keep upstream file names for traceability
└── brumel/
    ├── branding/
    ├── core/                   # hooks: factory registration, build wiring, settings entry points
    ├── degoogle/               # Brumel-specific removals/replacements beyond ungoogled
    ├── engine/
    ├── workspace/
    ├── memory/
    ├── shield/
    ├── nano/
    ├── connect/
    ├── tools/
    ├── ui/
    ├── dev/
    └── fixes/                  # bug fixes, ideally upstreamable
```

Brumel-**added** files (new modules, services, WebUI) do not live here; they live in the planned `src/` tree and are copied into `//brumel` in the checkout.

## Series file

`series` lists patch paths relative to `patches/`, one per line, in application order. Lines starting with `#` are comments. Group by category:

```text
# --- ungoogled-chromium (158.0.8127.88-1) ---
upstream-ungoogled/core/ungoogled-chromium/disable-crash-reporter.patch
# --- branding ---
brumel/branding/0001-product-name-and-icons.patch
# --- core hooks ---
brumel/core/0001-register-brumel-keyed-services.patch
```

## Naming

`brumel/<area>/NNNN-short-kebab-description.patch` — `NNNN` is the order within the area, never reused.

## Required header

Every Brumel patch begins with a header before the diff:

```text
Description: One or two sentences explaining what and why.
Origin: brumel | ungoogled-chromium:<path> | upstream:<CL or commit>
Module: core | engine | workspace | memory | shield | nano | connect | tools | ui | dev | branding | degoogle | fixes
Feature: <catalog ID, e.g. ENG-012> (or "n/a")
Upstreamable: yes | maybe | no
SPDX-License-Identifier: BSD-3-Clause
```

Imported patches keep their original header and license; add an `Origin:` line if missing.

A patch whose added lines mention switches or arguments that weaken a security boundary (for example `--no-sandbox`, `kDisableSiteIsolation`, `is_cfi = false`) must also carry a `Security-Note:` line explaining why it does not weaken security. `patches.py check` enforces this.

## Tooling

[`scripts/patches.py`](../scripts/patches.py) implements these conventions ([ADR-0013](../docs/architecture/adr/0013-git-backed-patch-tooling.md)):

| Command | What it does |
|---|---|
| `check` | Validates `series` and every header rule on this page. Runs in CI. |
| `list` / `stats` | Prints the series, or the patch budget: patches, modified upstream files, changed lines. |
| `apply --checkout DIR` | Records `refs/brumel/base`, then applies each patch as one commit with a `Brumel-Patch: <path>` trailer. Resumable. |
| `refresh --checkout DIR` | Regenerates patch files from those commits after you resolve conflicts, and keeps their headers. A commit with a new trailer becomes a new patch. |

`apply` and `refresh` print a plan and change nothing unless you pass `--execute`.

### Updating a patch after a conflict

1. `python3 scripts/patches.py apply --checkout DIR --3way --execute` stops at the patch that fails.
2. Resolve the conflict in the checkout, `git add` the files, then commit with the trailer:
   `git commit -m "<patch path>" -m "Brumel-Patch: <patch path>"`.
3. Run `apply` again to continue with the rest of the series.
4. `python3 scripts/patches.py refresh --checkout DIR --execute` writes the updated patch files.

To add a new patch, commit your change in the checkout with a new trailer (for example `Brumel-Patch: brumel/core/0002-register-services.patch`) and run `refresh`. Then fill in the generated header: `check` fails while the `Description` is still `TODO`.

## Rules

1. **Minimal.** Modify upstream files only to add hooks; put logic in added files under `//brumel`.
2. **One purpose per patch.** Split unrelated changes.
3. **No reformatting** or drive-by cleanups of upstream code.
4. **License.** Patches modifying Chromium files are BSD-3-Clause ([ADR-0004](../docs/architecture/adr/0004-licensing.md)). Added Brumel files are MPL-2.0.
5. **Security.** No patch may weaken the sandbox, Site Isolation, V8 sandbox, CFI or other mitigations ([SECURITY.md](../SECURITY.md)).
6. **Traceability.** Reference the catalog feature ID and, where relevant, the ADR.
7. **Refresh, don't hand-edit.** After resolving conflicts in a checkout, regenerate patches with `patches.py refresh` so context lines stay accurate.
8. **Delete when upstream catches up.** Remove patches made obsolete by upstream changes.
9. **Review.** Every patch is reviewed individually, including on rebase pull requests.
