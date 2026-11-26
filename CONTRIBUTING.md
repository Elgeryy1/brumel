# Contributing to Brumel

Thank you for your interest in Brumel. This guide covers how to help **today**,
while the project is in **Pre-development**, and the rules that will apply as code
lands.

> **There is nothing to build or run yet.** Brumel has no working browser build, no
> binaries and no releases. If someone offers you a "Brumel download", it is not ours.

## Ways to contribute right now

| Area | Examples | Where |
|---|---|---|
| Product | Challenge a feature, sharpen a problem statement, propose acceptance criteria, report a duplicate | [Feature catalog](docs/product/FEATURES.md), feature request form |
| Research | Check a claim in the feature matrix, collect evidence (studies, bug trackers, user reports), compare Chromium forks | [RESEARCH.md](docs/research/RESEARCH.md), research proposal form |
| Architecture & security | Review ADRs, the threat model, the upstream strategy | [docs/architecture/](docs/architecture/ARCHITECTURE.md), [THREAT_MODEL.md](docs/security/THREAT_MODEL.md) |
| Design | Critique the provisional logo proposals, accessibility of the palette, UI principles | [assets/branding/](assets/branding/README.md), [DESIGN_SYSTEM.md](docs/design/DESIGN_SYSTEM.md) |
| Documentation | Fix unclear wording, broken links, inconsistencies between documents | Any `docs/` file |
| Tooling | Tests and improvements for the repository scripts | [scripts/](scripts/README.md), [tests/](tests/README.md) |

New here? Start with [GOOD_FIRST_ISSUES.md](docs/development/GOOD_FIRST_ISSUES.md).

## Before you start

1. Read the [Vision](docs/product/VISION.md) and the [Roadmap](ROADMAP.md).
2. Search existing [issues](https://github.com/Elgeryy1/brumel/issues) and
   [Discussions](https://github.com/Elgeryy1/brumel/discussions).
3. For anything bigger than a small fix, open an issue or a Discussion first so the
   work can be agreed before you invest time.

## Proposing or changing features

Every feature has a **stable catalog ID** such as `ENG-001` or `SHD-012`. IDs are
never renumbered or reused, and rejected features keep theirs.

- **New idea:** open a *Feature request* and describe the real problem, who has it,
  and a concrete use case. Ideas without a problem statement are usually parked.
- **Changing an existing feature:** reference its ID in the title, for example
  `[WRK-007] Clarify archive retention rules`.
- **Editing the catalog directly:** change
  [`docs/product/catalog/features.json`](docs/product/catalog/features.json) (and
  `epics.json` if needed). Then regenerate the human-readable catalog and validate:

  ```sh
  python3 scripts/catalog/render_features.py
  python3 scripts/validate_docs.py
  ```

  Never edit `docs/product/FEATURES.md` by hand. It is generated, and CI rejects
  stale output.

Use only these status labels: Available, In Development, Planned, Research,
Experimental, Deferred, Rejected. Do not describe planned work as if it exists.

## Research contributions

Evidence matters more than opinion. A good research contribution:

- separates **facts** (with sources and access dates) from **hypotheses**;
- states its method, for example how a measurement was taken and on what;
- uses primary sources where possible (specifications, source code, official docs,
  bug trackers);
- never presents a target ("reduce RAM by 20–40%") as a result.

## Documentation style

- Public documentation is written in **English**.
- Plain, precise language. No hype, no superlatives without evidence.
- Use relative links between documents. Run `python3 scripts/validate_docs.py` to
  check them.
- Headings use sentence case. Use tables for comparisons and lists for steps.
- Mark uncertainty explicitly ("to be validated in Phase 1").

## Commits

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<optional scope>): <summary>

<body: what and why>

Signed-off-by: Your Name <you@example.com>
```

Common types: `feat`, `fix`, `docs`, `chore`, `ci`, `refactor`, `test`, `perf`,
`security`, `build`. Scopes are usually modules: `engine`, `shield`, `nano`,
`catalog`, `brand`, `upstream`.

## Developer Certificate of Origin (DCO)

Brumel uses the [Developer Certificate of Origin 1.1](https://developercertificate.org/)
instead of a Contributor License Agreement. Sign off every commit:

```sh
git commit -s
```

**Why a DCO and not a CLA?** A DCO is a lightweight statement that you have the
right to submit your contribution under the project's license. You keep your
copyright, and the project gets no special right to relicense your work. That
matches a community open-source project better than a CLA, and it is the model used
by the Linux kernel and many others. Note: if you later want to upstream a patch to
Chromium itself, Chromium has its own contributor requirements, which you handle
directly with the Chromium project.

## Licensing of contributions

By contributing you agree that your contribution is licensed as follows (see
[LICENSING.md](docs/legal/LICENSING.md) and
[ADR-0004](docs/architecture/adr/README.md)):

| What you change | License | SPDX header |
|---|---|---|
| New Brumel-original files (code, scripts, docs tooling) | MPL-2.0 | `SPDX-License-Identifier: MPL-2.0` |
| Patches that modify Chromium-derived files (`patches/`) | BSD-3-Clause, the same license as the file being modified | `SPDX-License-Identifier: BSD-3-Clause` in the patch header |
| Third-party material | Its original license. You must update [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). | Unchanged |

Add SPDX headers to new source files, for example:

```python
# SPDX-License-Identifier: MPL-2.0
# Copyright (c) The Brumel Authors
```

## Pull request process

1. Fork the repository and create a topic branch from `main`.
2. Keep pull requests focused: one logical change.
3. Fill in the pull request template, including linked issues and catalog IDs.
4. Make sure CI passes (link check, catalog validation, tests).
5. Expect review comments. A maintainer merges once the change is approved.
6. Large or architectural changes need an
   [ADR](docs/architecture/adr/README.md) or a discussion first.

## Security issues

**Do not open public issues for vulnerabilities.** Follow [SECURITY.md](SECURITY.md)
and use GitHub's private vulnerability reporting. Vulnerabilities in Chromium itself
should be reported to the Chromium project.

## AI-assisted contributions

AI tools are allowed. The rules:

- **You are responsible** for every line you submit. You must understand it, test
  it and be able to explain it in review.
- **Disclose substantial AI generation** in the pull request (for example "most of
  this document was drafted with an AI assistant and then edited").
- Do not submit AI output you cannot verify, especially factual claims, benchmark
  numbers, security reasoning or license statements.
- Make sure AI output does not reproduce code under an incompatible license.

Agents working in this repository must follow [AGENTS.md](AGENTS.md).

## CI and self-hosted infrastructure

Pull requests from forks run **only on GitHub-hosted runners**. Code from untrusted
contributors is never run on maintainer-owned or self-hosted machines. Any future
self-hosted build capacity is used only for trusted, reviewed branches.
[INFRASTRUCTURE.md](docs/development/INFRASTRUCTURE.md) describes this setup.

## Code of Conduct

Everyone taking part in this project agrees to follow the
[Code of Conduct](CODE_OF_CONDUCT.md).
