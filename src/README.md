# src/ — Brumel-added sources

Files here are Brumel's **own** sources (MPL-2.0). `scripts/overlay.py sync` mirrors this
directory into a Chromium checkout as `//brumel`. Changes to upstream Chromium files never
live here; they are patches in [`../patches/`](../patches/README.md).

Layout and rules: [MODULE_SYSTEM.md](../docs/architecture/MODULE_SYSTEM.md) and
[ARCHITECTURE.md §3](../docs/architecture/ARCHITECTURE.md#3-brumel-layers-mapped-to-the-chromium-tree).

Status: **Planned** — no browser code yet. `branding/BRANDING` holds the product name, company and copyright that `config/gn/_common.gn` passes to the build ([ADR-0015](../docs/architecture/adr/0015-branding-without-string-patches.md)). The module system skeleton (CORE-005) comes
first, after the build spike.

- Every source file starts with `SPDX-License-Identifier: MPL-2.0` (`overlay.py check`
  enforces it).
- No symlinks and no Windows-reserved file names (`con`, `nul`, `aux`, …).
