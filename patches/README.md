# Patches

This directory will contain the ordered series of patches that Brumel applies on top of the pinned Chromium tag ([`config/upstream.json`](../config/upstream.json)). **No patches exist yet** — Brumel is in pre-development. These conventions apply from the first patch.

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

## Rules

1. **Minimal.** Modify upstream files only to add hooks; put logic in added files under `//brumel`.
2. **One purpose per patch.** Split unrelated changes.
3. **No reformatting** or drive-by cleanups of upstream code.
4. **License.** Patches modifying Chromium files are BSD-3-Clause ([ADR-0004](../docs/architecture/adr/0004-licensing.md)). Added Brumel files are MPL-2.0.
5. **Security.** No patch may weaken the sandbox, Site Isolation, V8 sandbox, CFI or other mitigations ([SECURITY.md](../SECURITY.md)).
6. **Traceability.** Reference the catalog feature ID and, where relevant, the ADR.
7. **Refresh, don't hand-edit.** After resolving conflicts in a checkout, regenerate patches with the refresh tooling (planned) so context lines stay accurate.
8. **Delete when upstream catches up.** Remove patches made obsolete by upstream changes.
9. **Review.** Every patch is reviewed individually, including on rebase pull requests.
