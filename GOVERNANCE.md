# Governance

This document explains who owns Brumel, how decisions are made and how
responsibility is expected to grow as the project matures.

## Independence

Brumel is a **personal, independent open-source project** created and owned by
**Gerard Alvear** ([@Elgeryy1](https://github.com/Elgeryy1)). It is not a product of
any company and has no corporate affiliation, sponsor or investor. If that ever
changes, it will be disclosed here and announced publicly before it takes effect.

## Current model: founder-led (Pre-development to Public Alpha)

During the early phases Brumel follows a **founder-led** model, sometimes called a
"benevolent dictator" model. The project lead:

- sets product direction, scope and priorities;
- has final say on architecture decisions, releases and security policy;
- owns the name, brand assets and GitHub organization or account resources;
- acts as the default security responder until a security team exists.

The aim is speed and coherence while the foundations are laid. A browser project
cannot afford early fragmentation of its security and upstream-maintenance
practices.

## How decisions are made

| Decision type | Process | Record |
|---|---|---|
| Small changes (docs fixes, typos, scripts) | Pull request + review | PR history |
| Feature scope or priority | Issue or Discussion referencing the catalog ID | [Feature catalog](docs/product/FEATURES.md) |
| Architecture, dependencies, security-relevant design | Proposal (issue or Discussion labeled `type:research`), then an Architecture Decision Record | [ADRs](docs/architecture/adr/README.md) |
| Licensing, trademarks, paid services, irreversible actions | Project lead only | ADR or this file |
| Security incidents | Private handling according to [SECURITY.md](SECURITY.md) | Advisory after disclosure |

Principles:

1. **Write it down.** Significant decisions get an ADR with context,
   alternatives and consequences.
2. **Evidence over opinion.** Performance and privacy claims need data, and features
   need a real problem statement.
3. **Lazy consensus for routine work.** If no maintainer objects within a reasonable
   time on a well-described proposal, it may proceed.
4. **Security wins ties.** When usability, performance and security conflict, the
   default is the safer option, and the trade-off is documented.

## Roles

| Role | Responsibilities | How it is earned |
|---|---|---|
| **Contributor** | Anyone who opens issues, takes part in discussions, or submits PRs | Participate under the [Code of Conduct](CODE_OF_CONDUCT.md) |
| **Triager** | Labels, deduplicates and routes issues; maintains the project board | Sustained helpful participation; invited by a maintainer |
| **Committer** | Reviews and merges PRs in specific areas (for example docs, a module) | Track record of quality contributions in that area; nominated by a maintainer, approved by the project lead |
| **Maintainer** | Owns modules, the release process or upstream rebases; mentors committers | Long-term reliability and judgment; appointed by the project lead |
| **Security responder** | Handles private vulnerability reports, coordinates fixes and disclosure | Trusted maintainer with relevant expertise; appointed by the project lead |
| **Project lead** | Overall direction, final decisions, owner of name and assets | Currently Gerard Alvear |

Roles may be stepped down from at any time. Inactive members (roughly six months
without activity) may be moved to emeritus status, with thanks.

Module ownership will be reflected in [`.github/CODEOWNERS`](.github/CODEOWNERS) as
maintainers join.

## Conflict resolution

1. Discuss on the relevant issue or PR, focusing on evidence and trade-offs.
2. If unresolved, a maintainer summarizes the options and proposes a decision.
3. If still unresolved, the project lead decides and records the reasoning.

Code of Conduct matters follow the enforcement process in
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and are handled privately.

## Name, brand and trademarks

- "Brumel" and "Brumel Browser", and the Brumel logos, are owned by the project lead.
- Brand assets are **provisional** (see [assets/branding/](assets/branding/README.md)).
  A preliminary name check is in [NAME_CHECK.md](docs/research/NAME_CHECK.md). It is
  **not** legal clearance.
- The open-source license covers the code, not the brand. Forks are welcome but must
  use a different name and logo, so users are never confused about who builds the
  software they install. A formal trademark policy will be published before Public
  Alpha.

## Money and services

The project does not currently accept donations, pay for services or run paid
infrastructure. Any future funding, sponsorship or paid service will be decided by
the project lead, documented here and reported transparently.

## Evolving the governance

The founder-led model is a starting point. Planned evolution:

1. **Public Alpha:** name the first committers and triagers. Publish a trademark
   policy and a dedicated security contact.
2. **Public Beta:** a maintainer group with module owners. Security responders
   other than the project lead. Documented release managers.
3. **Version 1.0 and beyond:** consider a steering group with documented voting
   rules, and consider moving the project to a neutral home (for example a GitHub
   organization or a foundation) if the community has grown enough to justify it.

Changes to this document are made by pull request and approved by the project lead.
