# Phase 1 plan — Technical Foundation

Status: **In Development** — step 1 is done; steps 2, 3 and 5 are in development; steps 4, 6 and 7 are Planned. This plan breaks [Phase 1](../../ROADMAP.md#phase-1--technical-foundation) into ordered steps. Like the roadmap, it has **no dates**: each step starts when the one it depends on is done.

Goal of the phase: a reproducible, rebranded Chromium build from a pinned upstream tag, plus a measured answer to "how much does it cost to keep it up to date?". **No Brumel features are built in this phase.**

Related: [BUILDING.md](BUILDING.md) · [INFRASTRUCTURE.md](INFRASTRUCTURE.md) · [UPSTREAM_STRATEGY.md](../architecture/UPSTREAM_STRATEGY.md) · [Milestone: Technical Foundation](https://github.com/Elgeryy1/brumel/milestone/2)

## Decisions needed before step 2

| Decision | Recommendation | Issue |
|---|---|---|
| Where full builds run | On a maintainer-owned desktop, kept local at first. GitHub-hosted runners cannot build Chromium within their disk and time limits. No self-hosted runner until the process is stable, and never for pull requests from forks. | [#66](https://github.com/Elgeryy1/brumel/issues/66) |
| Which version to pin | **Decided** in [ADR-0014](../architecture/adr/0014-upstream-pin-policy.md): one pin for all platforms, preferring an ungoogled-chromium match with a bounded wait. The spike stays on 158; moving to the next stable is the first rebase drill (step 5). | [#65](https://github.com/Elgeryy1/brumel/issues/65) |
| Code signing | Defer. Internal builds stay unsigned and are never published. | [#67](https://github.com/Elgeryy1/brumel/issues/67) |

## Steps

| # | Step | Output | Status | Issues · catalog |
|---|---|---|---|---|
| 1 | **Repository tooling:** `fetch.py`, `patches.py`, `build.py`, GN profiles, unit tests and CI checks | Commands that fetch, patch and build reproducibly, tested without a checkout | Done (run against Chromium 158 in step 2; fixes in step 2) | [#62](https://github.com/Elgeryy1/brumel/issues/62), [#63](https://github.com/Elgeryy1/brumel/issues/63) · CORE-001, CORE-002 · [ADR-0013](../architecture/adr/0013-git-backed-patch-tooling.md) |
| 2 | **Build spike:** fetch and build unmodified Chromium at the pin on Windows and Linux | Measured disk, peak RAM, full and incremental build time, published in BUILDING.md; tooling fixes | In Development (Linux `release`, `dev` full and incremental measured in BUILDING.md; Windows `release` build not finished) | [#61](https://github.com/Elgeryy1/brumel/issues/61) |
| 3 | **First patches:** branding, a small ungoogled-chromium subset, no Google API keys | A browser called Brumel that starts and browses | In Development (branding approach and string tool, [ADR-0015](../architecture/adr/0015-branding-without-string-patches.md); Windows install-mode patch and 15 ungoogled-chromium patches in the series, [audit](../privacy/DEGOOGLING_AUDIT.md); first branded `dev` build on Linux starts as "Brumel 158.0.8127.88" with the sandbox on; icons, a browsing check and Windows Planned) | [#68](https://github.com/Elgeryy1/brumel/issues/68), [#69](https://github.com/Elgeryy1/brumel/issues/69) · CORE-004, CORE-006 |
| 4 | **Module skeleton:** `//brumel` source overlay, feature registry with flags, a test internal page | Proof that Brumel code can be added without editing Chromium beyond small hooks | Design written ([MODULE_SYSTEM.md](../architecture/MODULE_SYSTEM.md)); implementation Planned | [#70](https://github.com/Elgeryy1/brumel/issues/70) · CORE-005 · [ADR-0006](../architecture/adr/0006-in-process-modules.md) |
| 5 | **Rebase drill:** move the pin to the next stable and measure the rebase; run `check_upstream.py` on a schedule | The first real number for the cost of staying current | In Development (scheduled check done; drill Planned) | [#64](https://github.com/Elgeryy1/brumel/issues/64), [#65](https://github.com/Elgeryy1/brumel/issues/65) · CORE-003 |
| 6 | **Security baseline:** verify sandbox, site isolation and HTTPS-First stay on; publish the de-Googling audit | A published audit and regression checks | Planned | [#72](https://github.com/Elgeryy1/brumel/issues/72), [#69](https://github.com/Elgeryy1/brumel/issues/69) · EP-CORE-06 |
| 7 | **Internal packaging:** Windows installer and Linux `.deb`, unsigned; SBOM | Installable builds for the maintainer only | Planned | [#12](https://github.com/Elgeryy1/brumel/issues/12) · CORE-008, CORE-009, CORE-010 |

**In parallel, independent of Chromium:** the local-model evaluation for Brumel Nano (NANO-006, model licensing in [#59](https://github.com/Elgeryy1/brumel/issues/59)) and the benchmark harness on stock browsers ([#71](https://github.com/Elgeryy1/brumel/issues/71)).

**Out of scope for this phase:** Brumel features (content blocking, tab management, Nano, sync), the signed automatic updater (CORE-051) and any public binaries.

## Step 2 checklist (build spike)

1. Install depot_tools and the platform prerequisites listed in [BUILDING.md](BUILDING.md#2-upstream-toolchain).
2. `python3 scripts/fetch.py --checkout <dir>`: read the plan, then re-run with `--execute`.
3. Record the resolved commit from `<dir>/.brumel/fetch.json` in `config/upstream.json` (`chromium.revision`) through a pull request.
4. `python3 scripts/build.py build --checkout <dir> --profile release --execute`, with an empty series, so this is unmodified Chromium.
5. Record download size, checkout size, peak RAM and wall time; then the time to rebuild after touching one file with the `dev` profile.
6. Replace the planning assumptions in BUILDING.md with the measured values, and note every tooling fix.

## Known follow-ups

- `patches.py refresh` rewrites imported ungoogled-chromium patches in Git's diff format the first time they change ([ADR-0013](../architecture/adr/0013-git-backed-patch-tooling.md)).
- GN arguments in `config/gn/` are taken from upstream documentation and ungoogled-chromium practice. The build spike confirms them for the pinned version.

## Exit criteria (from the roadmap)

- A clean machine reproduces the build from documented scripts and the pinned `config/upstream.json`.
- The patch series applies to two consecutive upstream stable releases, and the rebase time is measured and recorded.
- Builds and update manifests are signed, and the updater refuses unsigned or downgraded payloads. This criterion stays open after step 7 and depends on [#67](https://github.com/Elgeryy1/brumel/issues/67).
- No Google-account, sync or private-API dependency remains enabled by default; the audit is published.
