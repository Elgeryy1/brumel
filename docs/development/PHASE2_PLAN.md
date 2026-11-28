<!-- SPDX-License-Identifier: MPL-2.0 -->
# Phase 2 plan — Internal Alpha, first feature round

Status: **Planned**. Nothing in this plan is implemented. Work starts when [Phase 1](PHASE1_PLAN.md) has a branded, de-Googled build that starts and updates. Like the roadmap, this plan has **no dates**.

Goal of the phase ([ROADMAP](../../ROADMAP.md#phase-2--internal-alpha)): a browser the maintainer can use every day, without regressions against Chromium. This file chooses the **first round** of Brumel features inside that phase.

Related: [Feature catalog](../product/FEATURES.md) · [Interface design](../design/INTERFACE.md) · [Milestone: Internal Alpha](https://github.com/Elgeryy1/brumel/milestone/3)

## How the round was chosen

Most P0 entries in phase 2 are Chromium features (bookmarks, history, downloads, DevTools, PDF, printing). For those, the work is to **check that they still work** in a de-Googled build, not to build them. The first round adds what makes Brumel different, in this order:

1. **Cheap secure defaults first.** Upstream features turned on by default: a clear gain for almost no patch weight.
2. **The slogan next.** "Less noise. More control.": Clean Web and visible memory and battery control.
3. **The visible face.** Tabs and the New Tab page, built on the approved design direction.
4. **One decision before anyone else uses Brumel.** Safe Browsing (CORE-012).

Each feature gets its screen designed and approved just before it is built, so Views (C++) code is not written twice.

## Round 1

| # | Work | Catalog | Depends on | Issue |
|---|---|---|---|---|
| 1 | Secure defaults: HTTPS-First and DNS over HTTPS on by default | CORE-047, CORE-046 (SHD-024, SHD-023) | Phase 1 build | [#92](https://github.com/Elgeryy1/brumel/issues/92) |
| 2 | Clean Web: native ad and tracker blocking | SHD-001 | CORE-005 module system | [#93](https://github.com/Elgeryy1/brumel/issues/93) |
| 3 | Clean Web companions: pop-ups, autoplay, notification prompts | SHD-002, SHD-003, SHD-005 | SHD-001, CORE-045 | [#94](https://github.com/Elgeryy1/brumel/issues/94) |
| 4 | Tracking parameter stripping | SHD-007 | SHD-001 update channel | [#95](https://github.com/Elgeryy1/brumel/issues/95) |
| 5 | Smart tab suspension, built on upstream tab discarding | ENG-019 | CORE-005 | [#96](https://github.com/Elgeryy1/brumel/issues/96) |
| 6 | Performance profiles: Performance, Balanced, Battery Saver | ENG-033 | ENG-019, ENG-024, ENG-008 (open question) | [#97](https://github.com/Elgeryy1/brumel/issues/97) |
| 7 | Horizontal and vertical tabs, reusing upstream if available | WRK-001 | UI-001 | [#98](https://github.com/Elgeryy1/brumel/issues/98) |
| 8 | Quiet New Tab page | UI-022 | UI-001, UI-018 | [#99](https://github.com/Elgeryy1/brumel/issues/99) |
| 9 | Decide the Safe Browsing strategy (owner decision, ADR) | CORE-012 | CORE-006 | [#100](https://github.com/Elgeryy1/brumel/issues/100) |
| 10 | Verify parity without a Google account: passwords, profiles, import | CORE-023, CORE-026, CORE-044 | Phase 1 build | [#101](https://github.com/Elgeryy1/brumel/issues/101) |

Item 1 is a phase 1 entry in the catalog and stays in the Technical Foundation milestone; it is listed here because it is the first user-visible change.

## Not in round 1

| Work | Why it waits |
|---|---|
| Brumel Store and local index (MEM-014), Idle Scheduler (ENG-045) | Large, and their benefit is not visible to the first user. |
| Startup work (ENG-021, ENG-030, ENG-043), resource monitor (ENG-031) | Need the benchmark harness ([#71](https://github.com/Elgeryy1/brumel/issues/71)) to show a measured gain. |
| Local data encryption (SHD-020), Settings Lock (SHD-018) | Need a security design review first. |

## Open questions

- **ENG-033 depends on ENG-008** (Smart Preload, Public Alpha) in the catalog. Either the first profiles ship without preload tuning, or ENG-008 moves earlier. Decide in [#97](https://github.com/Elgeryy1/brumel/issues/97) and update the catalog.
- **Safe Browsing without a Google key** is unverified ([DEGOOGLING_AUDIT.md](../privacy/DEGOOGLING_AUDIT.md)). No build goes to another person until [#100](https://github.com/Elgeryy1/brumel/issues/100) is decided. Removing the protection is not an option ([AGENTS.md](../../AGENTS.md), golden rule 2).
- **Vertical tabs upstream.** Whether Chromium at the current pin ships its own vertical tabs is unverified; [#98](https://github.com/Elgeryy1/brumel/issues/98) checks it first.
