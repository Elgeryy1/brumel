# Community

Brumel is built in public. The project is in **Pre-development**: there is no browser to
download yet, but the design, the roadmap and the decisions are open from the very first
commit. This document explains where conversations happen, how to get involved and the rules
we hold ourselves to.

See also [CONTRIBUTING.md](../../CONTRIBUTING.md), [GOVERNANCE.md](../../GOVERNANCE.md),
the [Code of Conduct](../../CODE_OF_CONDUCT.md) and the [launch plan](LAUNCH_PLAN.md).

## Principles

1. **Transparency over polish.** We publish plans, trade-offs, failed experiments and
   real measurements, including the ones that are unflattering.
2. **No invented numbers.** Every number we share (RAM, battery, startup time) comes from
   the reproducible methodology in [BENCHMARKS.md](../benchmarks/BENCHMARKS.md), and we
   link the raw data. Targets are always labelled as hypotheses.
3. **No artificial growth.** No bought stars, followers, upvotes or reviews. No sockpuppets.
   No "star this repo to unlock…" gimmicks. No coordinated voting on Reddit, Hacker News or
   Product Hunt.
4. **Respect for people's time and attention.** That is the product's promise too.
5. **Credit generously.** Upstream projects (Chromium, ungoogled-chromium, Brave's open-source
   components, Helium and others) are credited whenever we learn from or reuse their work.

## Where things happen

| Channel | Purpose | Status |
|---|---|---|
| [GitHub Issues](https://github.com/Elgeryy1/brumel/issues) | Bugs (once there is software), concrete tasks, epics, feature proposals tied to the catalog | Active |
| [GitHub Discussions](https://github.com/Elgeryy1/brumel/discussions) | Ideas, questions, design feedback, polls, show-and-tell | Active |
| [GitHub Projects](https://github.com/users/Elgeryy1/projects/2) — "Brumel — Development" | Public board: roadmap, backlog, research, release planning | Active |
| [Security advisories](https://github.com/Elgeryy1/brumel/security) | **Private** vulnerability reports (see [SECURITY.md](../../SECURITY.md)) | Active |
| Devlogs ([`docs/community/devlog/`](devlog/)) | Long-form progress notes | Active |
| Reddit (r/browsers, r/chromium, r/privacy when relevant) | Announcements of real milestones, feedback threads | Planned |
| Hacker News | "Show HN" only once something runnable exists | Planned |
| YouTube / TikTok | Short demos of features that **actually work**, plus a devlog series | Planned |
| X and Bluesky | Short progress updates, links to devlogs | Planned |
| Product Hunt | Only at Public Beta or later | Deferred |
| Discord / Matrix | Real-time chat for testers, once a tester group exists | Deferred |

Official accounts on social platforms will be listed here once they exist. Until then, treat
any account claiming to be Brumel as unofficial.

## How to help today (Pre-development)

There is no code to compile yet, but there is plenty of meaningful work:

- **Review the plan.** Read the [vision](../product/VISION.md), the
  [feature catalog](../product/FEATURES.md) and the [architecture](../architecture/ARCHITECTURE.md),
  and challenge assumptions in Discussions.
- **Bring evidence.** Many catalog entries are marked `Research`. A well-sourced comment
  ("this is how Vivaldi/Edge/Brave handle it", "this upstream Chromium API makes it feasible
  or infeasible") is extremely valuable. See [RESEARCH.md](../research/RESEARCH.md).
- **Security and privacy review.** Read the [threat model](../security/THREAT_MODEL.md) and
  [privacy principles](../privacy/PRIVACY.md) and point out gaps.
- **Design feedback.** Comment on the [provisional logo proposals](../../assets/branding/README.md).
- **Chromium experience.** If you have built or patched Chromium before, your input on the
  [upstream strategy](../architecture/UPSTREAM_STRATEGY.md) and
  [build plan](../development/BUILDING.md) is especially welcome.
- **Translations** of documentation are welcome later. English is the source language.

## Labels for newcomers

| Label | Meaning |
|---|---|
| `good first issue` | Small, well-scoped, with context and a clear "done" definition. A maintainer commits to reviewing it. |
| `help wanted` | We would like outside help. It may need more experience. |
| `type:research` | Investigation tasks: compare, measure, read upstream code, write findings |
| `needs-triage` | Not reviewed yet |

Guidance for writing and picking good first issues lives in
[docs/development/GOOD_FIRST_ISSUES.md](../development/GOOD_FIRST_ISSUES.md).

## Feature requests

1. Search the [feature catalog](../product/FEATURES.md). Your idea may already have a stable ID
   (for example `MEM-012`).
2. If it is there, comment on the related epic issue with your use case. If it is not, open a
   **Feature request** issue or start a thread in **Discussions → Ideas**.
3. Accepted ideas get a catalog ID and a status (`Research`, `Planned`, `Deferred`, …).
   Rejected ideas stay in the catalog with the reason, so they are never silently dropped.

## Recognition

- Every contributor is credited in release notes and the [CHANGELOG](../../CHANGELOG.md).
- Research and design contributions count as contributions. They are credited in the
  relevant document or ADR.
- Security reporters are credited in advisories unless they prefer to stay anonymous.
- We will add an all-contributors style list once there is more than a handful of people.

## Moderation

The [Code of Conduct](../../CODE_OF_CONDUCT.md) applies to every project space, including
discussions on external platforms when you are acting on behalf of the project. Moderators
may lock threads that turn into browser flame wars. Comparing browsers is welcome, and
tribalism is not.

## Communication rules for maintainers

- Do not present Planned features as available. Always state the status.
- Do not publish benchmark claims without the raw data and the method.
- Disclose any affiliation or sponsorship.
- Posts are drafted in the repository ([`posts/`](posts/)) and published manually. Nothing is
  auto-posted.
