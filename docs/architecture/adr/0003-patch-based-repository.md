# ADR-0003: Patch-based repository; Chromium source never committed

- Status: Accepted
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [Upstream Strategy](../UPSTREAM_STRATEGY.md), [`patches/README.md`](../../../patches/README.md), [Building](../../development/BUILDING.md)

## Context

A Chromium checkout with dependencies is very large (tens of gigabytes including history and third-party code) and moves daily. Committing it to this repository would make the repository unusable, obscure what Brumel actually changes and make rebases painful. Successful downstream projects (ungoogled-chromium, Helium, Brave) keep their changes separate from upstream source.

## Decision

- This repository contains only Brumel's **patches, added files, configuration, scripts and documentation**.
- The upstream version is pinned in [`config/upstream.json`](../../../config/upstream.json).
- Build scripts (Planned) fetch the pinned Chromium tag with depot_tools/gclient, apply the patch series in the order of `patches/series`, copy Brumel's added files into `//brumel` in the checkout, and build.
- Every patch has a header describing purpose, origin, module, related feature ID, upstreamability and SPDX license.

## Consequences

- Positive: small, reviewable repository; Brumel's diff against upstream is explicit and measurable; rebases are a well-defined operation.
- Negative: contributors need the full Chromium toolchain to build; patch conflicts must be resolved manually on rebases.
- Neutral: tooling (scripts and CI) becomes a core part of the project.

## Alternatives considered

- **Full fork of chromium/src in a Git repository**: easier local development, but enormous, hard to audit and to rebase. Rejected for this repository; developers may keep local Git branches inside their checkout.
- **Git submodule of chromium/src**: still requires hosting/fetching the full tree; does not solve the review problem. Rejected.

## Revisit when

The patch series grows to a size where a full fork with automated rebasing becomes cheaper to maintain.
