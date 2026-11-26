# Security Policy

Brumel is in **pre-development**. There is no released build, no installer, no updater and no hosted service yet. This document explains how to report vulnerabilities today, what the project commits to as it grows, and the security principles that every future design must respect.

The detailed analysis lives in the [Threat Model](docs/security/THREAT_MODEL.md).

## Supported versions

| Version | Supported |
| --- | --- |
| Any | No public build exists yet. Nothing is supported. |

When the first public alpha ships, this table will list the supported release channels. Brumel will only support the **latest** build of each channel: browser security depends on staying current with Chromium, so we will not backport fixes to old Brumel versions.

## Reporting a vulnerability

**Do not open a public issue, discussion or pull request for a security problem.**

Report privately through GitHub Private Vulnerability Reporting:

**<https://github.com/Elgeryy1/brumel/security/advisories/new>**

Please include:

- A description of the issue and its impact.
- The affected file, document, workflow, script or (in the future) build, version and platform.
- Steps to reproduce or a proof of concept, kept as small as possible.
- Whether you believe the issue is in Brumel's own code or in upstream Chromium.
- Whether you want to be credited, and under which name.

There is no bug bounty. Brumel is an independent, unfunded project and cannot offer monetary rewards. Credit in the advisory and the changelog is offered to reporters who want it.

### What is in scope today

Even before any browser code exists, the repository has a real attack surface:

- GitHub Actions workflows (for example script injection, excessive token permissions, unpinned actions).
- Scripts under [`scripts/`](scripts/) (for example unsafe parsing of remote data, command injection).
- Documentation that would lead users or contributors into an insecure configuration.
- Leaked secrets or personal data in the repository history.

### What will be in scope later

- Brumel patches applied on top of Chromium (`patches/`).
- Brumel-specific modules (Engine, Workspace, Memory, Shield, Nano, Connect, Tools, Dev).
- The update pipeline, signing, distribution and installers.
- Brumel Connect (sync) clients and the reference relay server.
- Brumel Nano (local AI) component download, sandboxing and data handling.

### Out of scope: upstream Chromium

Brumel is built on Chromium. If a vulnerability also affects **unmodified Chromium** (or Google Chrome), report it to the Chromium project first, because they fix it for every downstream browser at once:

- Chromium security reporting: <https://www.chromium.org/Home/chromium-security/reporting-security-bugs/>

You are welcome to tell us as well, privately, so we can track the fix and ship the patched upstream release quickly. Do not disclose details publicly before Chromium does.

Also out of scope:

- Issues that require a fully compromised device or administrator access, unless Brumel makes the situation meaningfully worse.
- Missing hardening headers on pages that do not exist yet.
- Social-engineering attacks on the maintainer.
- Denial-of-service against GitHub itself.

## Response goals

These are **goals**, not guarantees. Brumel currently has one maintainer.

| Step | Goal |
| --- | --- |
| Acknowledge the report | Within 5 days |
| Initial assessment and severity | Within 14 days |
| Fix or mitigation for critical issues in Brumel code | As fast as possible; target 30 days |
| Ship an upstream Chromium security release after it is published (once releases exist) | Target 7 days for critical/high fixes, measured from upstream stable release |

Severity follows the [Chromium severity guidelines](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/severity-guidelines.md) so that Brumel and upstream speak the same language.

## Disclosure policy

- We follow coordinated disclosure. We aim to publish an advisory once a fix is available, and at most **90 days** after the report, unless the reporter agrees to a different timeline or the issue depends on an unreleased upstream fix.
- Advisories are published through GitHub Security Advisories on this repository, with a CVE when appropriate.
- Reporters are credited unless they ask not to be.
- If an issue is being actively exploited, we may disclose earlier with mitigation guidance.

## Security model summary

These principles are binding for all Brumel designs and patches. A change that violates them will not be merged.

1. **Never weaken Chromium's security architecture.** Brumel does not disable or relax the sandbox, Site Isolation, process separation, the V8 sandbox, Control Flow Integrity, exploit mitigations or certificate verification — not for benchmarks, not for memory savings, not for compatibility shortcuts. Resource savings come from scheduling, discarding, throttling and not running optional features, never from removing isolation.
2. **Stay current with upstream.** Security in a Chromium-based browser is mostly the speed at which upstream fixes reach users. See the [Upstream Strategy](docs/architecture/UPSTREAM_STRATEGY.md).
3. **Optional features are fully off when disabled.** A disabled module must not run code, open connections or hold data in memory. Less running code is less attack surface.
4. **Web content is untrusted, including for AI.** Brumel Nano treats page text, titles, URLs and metadata strictly as data. Model output never triggers privileged actions by itself: every action that changes state, touches files, sends data or executes anything requires a deterministic permission check and, where appropriate, explicit user confirmation. See [AI Architecture](docs/architecture/AI_ARCHITECTURE.md).
5. **Privileged code stays small and separate.** New features run with the least privilege possible: in the renderer or in sandboxed utility processes when they handle untrusted input, and in the browser process only when they must. Parsers of untrusted data are candidates for Rust (see [ADR-0010](docs/architecture/adr/0010-rust-for-new-components.md)).
6. **End-to-end encryption for sync.** Brumel Connect servers store ciphertext. A compromised server must not reveal browsing data. Password sync stays Deferred until a dedicated security review. See [Sync Architecture](docs/architecture/SYNC_ARCHITECTURE.md).
7. **No mandatory telemetry or accounts.** See [Privacy](docs/privacy/PRIVACY.md).

## Supply chain

Planned controls, documented in detail in the [Upstream Strategy](docs/architecture/UPSTREAM_STRATEGY.md), [Building](docs/development/BUILDING.md) and [Infrastructure](docs/development/INFRASTRUCTURE.md) documents:

| Control | Status |
| --- | --- |
| Chromium source is never vendored in this repository; the upstream version is pinned in [`config/upstream.json`](config/upstream.json) | Available (repository policy) |
| GitHub Actions pinned to full commit SHAs, updated by Dependabot | Available |
| Minimal `GITHUB_TOKEN` permissions per workflow | Available |
| Patch series with per-patch origin and license headers | Planned |
| Signed release tags and signed commits for releases | Planned |
| Software Bill of Materials (SBOM, SPDX or CycloneDX) for every release | Planned |
| Code signing for Windows binaries and signed Linux repositories | Planned |
| Signed update manifests verified by the client before installing | Planned |
| Build provenance attestations (SLSA-style) | Planned |
| Reproducible builds | Research — Chromium is large and full bit-for-bit reproducibility is hard; we will document what is and is not reproducible |
| Self-hosted runners never execute code from untrusted pull requests | Planned (policy in [Infrastructure](docs/development/INFRASTRUCTURE.md)) |

## Contact

Security reports: the private advisory form above. For anything else, use [GitHub Discussions](https://github.com/Elgeryy1/brumel/discussions).
