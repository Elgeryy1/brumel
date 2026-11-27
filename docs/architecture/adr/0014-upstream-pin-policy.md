# ADR-0014: Upstream pin policy

- Status: Accepted (provisional)
- Date: 2026-11-27
- Deciders: @Elgeryy1
- Related: [Upstream Strategy](../UPSTREAM_STRATEGY.md), [ADR-0002](0002-chromium-base-selection.md), [ADR-0013](0013-git-backed-patch-tooling.md), [`config/upstream.json`](../../../config/upstream.json), issues [#65](https://github.com/Elgeryy1/brumel/issues/65) and [#80](https://github.com/Elgeryy1/brumel/issues/80)

## Context

Chrome stable does not move on every platform on the same day. On 2026-11-26, Chromium Dash reported 159.0.8154.34 as Windows stable while Linux stable was still 158.0.8127.88. ungoogled-chromium tags a new version some days after upstream, and its newest tag was `158.0.8127.88-1`. Brumel needs a rule for three questions:

1. One pin for all platforms, or one per platform?
2. How long may Brumel wait for ungoogled-chromium before it moves on its own?
3. What happens when an upstream release fixes a vulnerability that is being exploited?

## Decision

1. **One pin for every platform.** `config/upstream.json` holds a single Chromium version, used for Windows and Linux. One series, one rebase, one set of test results.
2. **Target.** The target version is the newest version that is stable on at least one Brumel platform (for example Windows 159 while Linux is still 158).
3. **Prefer an ungoogled-chromium match.** Brumel moves to the target when ungoogled-chromium has a `<version>-<revision>` tag for it. The scheduled [Upstream check](../../../.github/workflows/upstream-check.yml) shows that in its tracking issue.
4. **Bounded wait.** If ungoogled-chromium has no matching tag:
   - **7 days** after the target became stable, Brumel moves anyway for a security respin within the same major.
   - **14 days** after, it moves anyway for a new major.

   When it moves anyway, it carries the previous ungoogled-chromium patches forward, refreshes them with `patches.py refresh`, and records the deviation in the release notes.
5. **Security fast path.** If the upstream release notes report a vulnerability *exploited in the wild*, or the release fixes Critical-severity issues, Brumel does not wait for ungoogled-chromium. It moves as soon as the series applies and builds. This follows the 72-hour goal in [Upstream Strategy](../UPSTREAM_STRATEGY.md#3-release-rhythm).
6. **Never pin backwards** to a lower version than a previous Brumel build, except to revert a broken pin that was never released.
7. **Record the commit.** After the first verified fetch of a pin, its commit goes into `chromium.revision`. `scripts/fetch.py` then refuses a checkout whose tag points elsewhere.
8. **Phase 1 exception.** During the build spike ([#61](https://github.com/Elgeryy1/brumel/issues/61)) the pin stays on 158.0.8127.88 so that the measurements use a fixed, ungoogled-matched version. Moving to the next stable is the first rebase drill (step 5 of the [Phase 1 plan](../../development/PHASE1_PLAN.md)).

Until Brumel ships builds, the windows in points 4 and 5 are goals used to practise the process, not commitments to users.

## Consequences

- Positive: a single series keeps the patch budget and rebase cost low. Users on every platform get the same browser version.
- Positive: ungoogled-chromium alignment saves work in the common case, but it never blocks a security fix for long.
- Negative: on the platform that is still on the older stable, Brumel can be one version ahead of Chrome. This is acceptable: the newer version is stable upstream on another platform.
- Negative: carrying ungoogled-chromium patches forward alone costs maintainer time, which is exactly what the 7 and 14 day windows bound.

## Alternatives considered

- **Per-platform pins.** These would need two patch series in flight, two sets of tests and two rebases. Rejected: this doubles the maintenance cost for a single maintainer.
- **Always wait for ungoogled-chromium.** Simple, but it ties Brumel's security delay to another project's availability. Rejected.
- **Follow upstream only and drop ungoogled-chromium.** This is possible later (ADR-0002 allows it per patch), but today it would mean redoing de-Googling work that ungoogled-chromium already maintains.

## Revisit when

- Brumel ships public builds and has real data on release delay.
- ungoogled-chromium's tagging delay or direction changes significantly.
- A third platform (macOS, Android) is added.
