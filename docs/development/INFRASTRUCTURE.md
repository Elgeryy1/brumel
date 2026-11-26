# Infrastructure

Status: **Planned** — no Brumel service is deployed. This document lists the services the project will need, free or low-cost options, and the policies that protect users and the maintainer's own machines. **Any paid service requires explicit approval from the project owner before it is contracted.** Prices and free-tier limits change often; every figure marked *verify* must be checked before a decision.

Related: [Building](BUILDING.md) · [Upstream Strategy](../architecture/UPSTREAM_STRATEGY.md) · [Sync Architecture](../architecture/SYNC_ARCHITECTURE.md) · [Threat Model §5.8](../security/THREAT_MODEL.md)

## 1. Services needed by phase

| Service | Needed from | Purpose |
| --- | --- | --- |
| Source hosting, issues, discussions, projects | Phase 0 | GitHub (free for public repositories) |
| Documentation CI (link checks, catalog validation) | Phase 0 | GitHub-hosted runners |
| Website | Phase 0–1 | GitHub Pages (free) |
| Upstream monitoring bot | Phase 1 | Scheduled GitHub Actions on hosted runners |
| Chromium build runners | Phase 1 | Full builds and tests |
| Build cache / remote execution | Phase 1–2 | Faster rebuilds (Research) |
| Artifact storage | Phase 2 | Internal builds, symbols, test results |
| Symbol server | Phase 2 | Symbolizing crash reports |
| Crash report collection (opt-in) | Phase 3 | Stability; self-hostable crash server (Research: Crashpad-compatible backends) |
| Code signing | Phase 3 | Windows Authenticode; Linux repository signing |
| Update server | Phase 3 | Signed update manifests ([ADR-0012](../architecture/adr/0012-update-system.md)) |
| Component server | Phase 3–4 | Filter lists, dictionaries, Nano models (static, signed) |
| Download hosting / CDN | Phase 3 | Installers and packages |
| Sync relay | Phase 4 | Brumel Connect encrypted relay |
| TURN server | Phase 4 | WebRTC fallback for device mesh |
| Community chat | When testers exist | Discord or Matrix |

## 2. Options and costs

| Need | Free / low-cost options | Cost notes |
| --- | --- | --- |
| CI for docs and scripts | GitHub-hosted runners | Free for public repositories |
| Chromium builds | Maintainer-owned private machines as self-hosted runners | No direct cost; electricity and time |
| Chromium builds (alternative) | GitHub larger runners, cloud VMs (spot/preemptible) | Paid per minute/hour; requires owner approval |
| Static website | GitHub Pages | Free |
| Release downloads | GitHub Releases | Free for public repositories (file size limits apply — verify; Chromium installers fit) |
| Update manifests, components | GitHub Pages / Releases initially; object storage + CDN later (e.g. Cloudflare R2, which has no egress fees — verify) | Free tiers likely sufficient early; verify |
| Sync relay | Supabase Free (PostgreSQL, auth, storage) | Free tier with quotas and inactivity pausing — verify; self-host alternative |
| TURN | Self-hosted coturn on a small VPS, or a provider's free tier | Small VPS has a monthly cost; requires approval |
| Windows code signing | SignPath Foundation (free code signing for qualifying open-source projects — verify eligibility); Azure Trusted Signing (low monthly fee — verify current name, price and eligibility); traditional OV/EV certificates (yearly cost) | Required before public binaries; requires approval for paid options |
| Linux signing | GPG keys for apt/rpm repositories; Sigstore (cosign) for artifacts and provenance | Free |
| Domain | Not needed yet; `github.io` URL suffices | Requires approval; see [Name Check](../research/NAME_CHECK.md) |

### Why hosted runners cannot build Chromium

GitHub's standard hosted runners for public repositories have limited CPU, RAM and especially **disk space**, and a **maximum job duration of 6 hours** (verify current limits). A full Chromium build needs far more disk than a standard runner provides and typically exceeds the time limit. Hosted runners remain ideal for documentation, scripts, upstream checks and small tests; full builds need self-hosted or paid larger runners.

## 3. Self-hosted runner policy

Self-hosted runners execute code on machines the project controls. On a **public** repository, misconfiguration lets anyone run code on those machines via a pull request. Brumel's rules:

1. **Private and maintainer-owned.** Runners are machines owned by the maintainer, never shared community machines, and never public runners.
2. **Never run code from untrusted pull requests.** Workflows that target self-hosted runners trigger only on pushes to protected branches, tags, or `workflow_dispatch` by maintainers — **never** on `pull_request` or `pull_request_target` from forks.
3. **Runner groups restricted** to specific workflows and branches.
4. **Ephemeral execution.** Each job runs in a fresh, disposable environment (VM or container recreated per job, e.g. `--ephemeral` runners) with no persistent credentials. Caches are read-mostly and integrity-checked.
5. **Network isolation.** Runners run in an isolated network segment (dedicated VM/VLAN) with **no access to the maintainer's private network**, storage or other services; outbound access limited to what builds need.
6. **No exposure.** Runners connect outbound to GitHub only; no inbound ports are opened to the internet.
7. **Approval gates.** Release jobs use protected GitHub environments requiring maintainer approval.
8. **No signing keys on runners.** Release signing uses a separate, minimal, approval-gated step (preferably a managed signing service); build runners never hold long-term signing keys.
9. **Least-privilege tokens.** `GITHUB_TOKEN` permissions set per job; no personal access tokens on runners.
10. **Documented and reviewed.** Any change to runner configuration is reviewed against this policy.

Setting up runners on the maintainer's machines will happen only in Phase 1 and only with the owner's explicit authorization. No machine will be modified or exposed without it.

## 4. Build capacity plan (Phase 1)

- Use the maintainer's two reference machines (see [Benchmarks §7](../benchmarks/BENCHMARKS.md)) — one primarily Windows, one Linux — as initial build machines, inside isolated VMs.
- Measure full and incremental build times; decide whether a shared compilation cache (e.g. a self-hosted remote cache compatible with Siso/reclient protocols — Research) is worth it.
- If capacity is insufficient, prepare a cost estimate for cloud build capacity and request owner approval.

## 5. Operational security

- Two-factor authentication on all project accounts; hardware security keys preferred.
- Branch protection / rulesets on `main`; signed release tags.
- Secrets only in GitHub environments with required reviewers.
- Secret scanning and push protection enabled.
- Dependabot for GitHub Actions and future dependencies.
- Recovery plan for maintainer accounts and signing keys (key escrow or co-maintainer access before Version 1.0, see [Governance](../../GOVERNANCE.md)).

## 6. Sustainability

The project currently has no funding. Before Public Beta, the project will publish an infrastructure cost estimate and options (donations via GitHub Sponsors or Open Collective, grants for open-source privacy software). No paid service is contracted without the owner's approval, and no essential feature will depend on a paid subscription for users.
