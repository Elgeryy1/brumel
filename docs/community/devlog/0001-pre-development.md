# Devlog #0001: Day zero, pre-development

*2026-11-26 · Gerard Alvear (@Elgeryy1)*

Brumel officially exists as a public project. There is **no browser yet**: no build, no
binary, no Chromium checkout. This devlog records what was done today and why it was done
in this order.

## Why start with documents instead of code?

Chromium is one of the largest open-source codebases in the world. Forks fail less often
because of missing features than because of **maintenance**: falling behind on security
updates, patches that are painful to rebase, or a build nobody else can reproduce. So the
first deliverable is a project that is set up to be maintained:

- a pinned-upstream, patch-based strategy rather than a full source copy;
- an explicit security model and threat model before any feature work;
- a feature catalog in which every idea gets a stable ID and an honest status;
- licensing decided before code is written.

## What was done today

- **Repository** created and published, with Issues, Discussions and a public project board.
- **Documentation** covering the product (vision, feature catalog, feature matrix,
  requirements), the architecture (overall architecture, local AI, sync, upstream strategy,
  compatibility, ADRs), security and privacy (security policy, threat model, privacy
  principles), development (building, infrastructure, benchmarks) and community.
- **Base decision (provisional).** Chromium upstream stable tags plus our own patch series,
  selectively importing ungoogled-chromium patches. We will not fork Brave, Thorium or
  Helium. The reasoning is in [CHROMIUM_BASES.md](../../research/CHROMIUM_BASES.md). This will
  be validated by a first build spike in Phase 1.
- **License (approved).** MPL-2.0 for Brumel's own files and BSD-3-Clause for patches to
  Chromium files, with third-party licences preserved. The reasoning is in
  [LICENSING.md](../../legal/LICENSING.md).
- **Provisional visual identity.** Five logo explorations. "Haze", a disk dissolving into mist,
  is used provisionally. See [branding](../../../assets/branding/README.md).
- **Preliminary name check.** No browser called Brumel was found in a superficial search.
  That is not legal clearance; see [NAME_CHECK.md](../../research/NAME_CHECK.md).

## What was deliberately *not* done

- No Chromium download or compilation, because that is Phase 1.
- No performance claims. The RAM and energy reduction targets in the docs are **hypotheses**
  until the [benchmark methodology](../../benchmarks/BENCHMARKS.md) produces data.
- No paid services, domains or servers.

## What's next

1. Finish triaging the catalog into the Phase 1 and Phase 2 scope.
2. Prepare the Phase 1 build spike: pinned upstream, fetch and patch scripts, first branded
   build on Windows and Linux.
3. Collect feedback on the plan and the logo in
   [Discussions](https://github.com/Elgeryy1/brumel/discussions).

If you have experience maintaining a Chromium fork, I'd love to hear from you.
