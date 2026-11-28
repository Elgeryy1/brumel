# Changelog

All notable changes to Brumel are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Brumel has **no released versions yet**. A versioning scheme will be defined
before the first public build (see [ROADMAP.md](ROADMAP.md)), and it is expected to
follow the Chromium milestone it is based on.

## [Unreleased]

Phase 0 — Pre-development. No browser code or binaries exist yet.

### Added (Phase 1 — Technical Foundation, in progress)

- Build tooling, not yet validated against a real Chromium checkout:
  `scripts/fetch.py` (pinned fetch with depot_tools), `scripts/patches.py`
  (series check, stats, apply and refresh; ADR-0013) and `scripts/build.py`
  (GN profiles with a security guard). All of them print a plan unless run with
  `--execute`.
- GN argument profiles `dev`, `release` and `minimal` in `config/gn/`.
- Phase 1 plan: `docs/development/PHASE1_PLAN.md`.
- Phase 2 plan: `docs/development/PHASE2_PLAN.md`, the first Internal Alpha
  feature round (secure defaults, Clean Web, tab suspension, performance
  profiles, tabs, New Tab page) and issues #92 to #101.
- CI checks for the patch series and the GN profiles.
- `scripts/overlay.py`: checks Brumel's own sources in `src/` and mirrors them
  into a checkout as `//brumel`.
- Prototype benchmark harness `scripts/bench/harness.py` for stock browsers
  (startup, tab load, memory, idle CPU). It produces no Brumel results.
- `config/upstream.json` records the Chromium commit of the pin
  (`chromium.revision`), taken from the first verified fetch (ADR-0014, point 7).
- Branding without string patches (ADR-0015): `src/branding/BRANDING` reaches
  the checkout through the overlay and `branding_file_path`; `scripts/rebrand.py`
  replaces the product name in Chromium's strings and renames their
  translations with the checkout's GRIT, keeping Chromium attribution. Not yet
  built.
- First patch, `brumel/branding/0001-windows-install-mode.patch`: the Windows
  install mode gets its own user data directory (`%LOCALAPPDATA%\Brumel`),
  app and ProgIDs, launch scheme and COM class IDs, so it does not collide with
  an installed Chromium. The sandbox AppContainer SID prefix is unchanged.
  Applies to the pin; not yet built.
- De-Googling audit (`docs/privacy/DEGOOGLING_AUDIT.md`, CORE-006) and 15
  ungoogled-chromium patches in the series: crash reporter, Gaia, GCM, domain
  reliability, network time, Google host detection, autofill server, RLZ,
  update pings and others. Safe Browsing is kept; a GPL-3.0 Bromite patch is
  left out. Applies to the pin; not yet built.
- Build fix `brumel/fixes/0001-limit-blink-bindings-parallelism.patch`: Blink's
  bindings generators run one at a time with at most 8 workers each. Unlimited,
  they exhausted 32 GB of RAM and hung the spike machine. Build-only.
- `scripts/patches.py` applies and refreshes patches that touch nested DEPS
  repositories (`v8/`, `third_party/devtools-frontend/src/` and others), one
  commit per repository with the same trailer (ADR-0013, amended). Found in the
  build spike: these patches failed to apply before.
- `scripts/build.py build --jobs N` limits parallel compile jobs, for machines
  with little free memory.
- Measured build spike numbers in `docs/development/BUILDING.md`: unmodified
  Chromium 158 `release` built in 1 h 54 min on an 8-core Linux machine, plus
  `dev` full (1 h 55 min) and incremental (16 s) times. They replace the
  planning assumptions.
- First branded, de-Googled build (Linux, `dev` profile): the 17-patch series,
  overlay and rebrand apply cleanly, and the browser starts as "Brumel" with
  the sandbox on. `BUILDING.md` documents the AppArmor profile Ubuntu needs
  instead of `--no-sandbox`.
- Scheduled `Upstream check` workflow: keeps one "Upstream update available" issue
  in sync with Chromium stable and ungoogled-chromium tags (CORE-003).

### Added

- Public repository, project identity and provisional slogan ("Less noise. More control.").
- Product documentation: vision, master feature catalog with stable IDs, feature
  matrix, product requirements.
- Architecture documentation: architecture overview, Architecture Decision Records,
  upstream (Chromium) maintenance strategy, compatibility, local AI and sync
  architectures.
- Security and privacy documentation: security policy and model, threat model,
  privacy principles.
- Development documentation: build strategy, infrastructure plan, benchmark
  methodology.
- Provisional brand identity: five logo proposals in SVG with light, dark and
  monochrome variants, favicon, GitHub banner and social preview. **Not final.**
- Community foundations: contributing guide, code of conduct, governance, issue
  forms, discussion templates, launch plan and post drafts.
- Project management: GitHub Project "Brumel — Development", milestones per phase,
  labels, foundation issues and module epics.
- Repository tooling: documentation and catalog validator, catalog renderer, upstream
  version checker, tests, CI workflow.
- Licensing: MPL-2.0 for Brumel-original files, BSD-3-Clause for patches to
  Chromium-derived files.
