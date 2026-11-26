# Brumel Threat Model

Status: **Research** — initial version written during pre-development (2026-11-26). It describes intended designs, not shipped code, and will be revised at every phase gate (see [Review cadence](#review-cadence)).

Related: [SECURITY.md](../../SECURITY.md) · [Architecture](../architecture/ARCHITECTURE.md) · [AI Architecture](../architecture/AI_ARCHITECTURE.md) · [Sync Architecture](../architecture/SYNC_ARCHITECTURE.md) · [Privacy](../privacy/PRIVACY.md) · [Upstream Strategy](../architecture/UPSTREAM_STRATEGY.md)

## 1. Scope and method

Brumel inherits Chromium's security architecture: a multi-process model, a sandboxed renderer, Site Isolation, a GPU process, a network service and many utility processes. Chromium's own threat model is the baseline and is **not** restated here. This document covers:

1. What Brumel **adds** (modules, local AI, sync, update and build infrastructure).
2. What Brumel **changes** (patches to Chromium, removal of Google services).
3. The **operational** risk of being a small downstream project (update latency, signing keys, self-hosted build machines).

We use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) per surface, followed by mitigations and residual risks.

## 2. Assets

| Asset | Why it matters |
| --- | --- |
| Credentials: passwords, passkey metadata, cookies, session tokens | Account takeover |
| Browsing data: history, tabs, sessions, bookmarks, downloads, form drafts | Deeply personal; Memory features make it searchable and therefore more valuable |
| Brumel Store (local index, embeddings, page snapshots, receipts) | Concentrates context from many sites in one place |
| Sync keys and encrypted sync data | Access to all synced devices |
| Local AI models and their outputs | Tampered models could mislead users or exfiltrate data if given capabilities |
| Update channel and signing keys | Code execution on every installed Brumel |
| Build pipeline, patch series, release artifacts | Supply-chain compromise |
| Maintainer accounts (GitHub, signing services, hosting) | Root of trust for everything above |
| User trust | A single privacy failure undermines the whole project |

## 3. Adversaries

| Adversary | Capabilities | Typical goal |
| --- | --- | --- |
| Malicious website | Arbitrary HTML/JS/CSS, crafted media, prompt-injection text, redirects, dark patterns | Code execution, data theft, tracking, manipulating Brumel features |
| Tracker / ad network | Third-party scripts, fingerprinting, bounce tracking, link decoration | Cross-site tracking |
| Malicious or compromised extension | Permissions granted by the user, updates pushed by a new owner | Data theft, ad injection, credential capture |
| Network attacker | On-path at Wi-Fi/ISP level | Downgrade, interception, update hijacking |
| Compromised sync relay or hosting provider | Full control of server storage and code | Read or modify synced data, track devices |
| Local attacker (same user account) | Malware or another person with access to the unlocked session | Read profile data, keys |
| Local attacker (physical, device off or locked) | Disk access | Read profile data at rest |
| Supply-chain attacker | Compromise of a dependency, GitHub Action, toolchain, contributor account or build machine | Ship malicious code to users |
| Malicious contributor | Pull requests, issues | Introduce backdoors, attack CI runners |
| Model supplier or mirror | Provides model files | Backdoored or poisoned model |

## 4. Trust boundaries

```mermaid
flowchart LR
  subgraph Untrusted["Untrusted"]
    WEB[Web content]
    EXT[Extensions]
    NET[Network]
    PR[Pull requests from forks]
  end
  subgraph Device["User device"]
    R[Renderer processes<br/>sandboxed, site-isolated]
    G[GPU process]
    N[Network service]
    U[Utility processes<br/>parsers, OCR, indexing]
    NANO[Nano inference process<br/>sandboxed, no network]
    B[Browser process<br/>privileged: UI, prefs, Brumel modules]
    S[(Profile data +<br/>Brumel Store)]
  end
  subgraph Services["Brumel services (future)"]
    SYNC[Sync relay<br/>ciphertext only]
    UPD[Update server<br/>signed manifests]
    COMP[Component server<br/>models, filter lists]
  end
  subgraph Build["Build & release"]
    CI[Hosted CI]
    SH[Self-hosted runners<br/>private, maintainer-owned]
    KEYS[Signing keys]
  end
  WEB --> R
  EXT --> B
  NET --> N
  R -- Mojo IPC --> B
  G -- Mojo IPC --> B
  U -- Mojo IPC --> B
  NANO -- Mojo IPC --> B
  B --> S
  B -- E2EE blobs --> SYNC
  B -- verify signature --> UPD
  B -- verify hash --> COMP
  PR --> CI
  CI -. never .-> SH
  SH --> KEYS
```

Key boundaries:

- **Renderer → browser.** The most important boundary in any Chromium browser. Every new Mojo interface Brumel adds is a new way for a compromised renderer to talk to privileged code.
- **Utility/Nano → browser.** Processes that parse untrusted data (pages, images, audio, model files) must be sandboxed and must not be trusted by the browser process.
- **Extension → browser.** Extensions are user-granted privilege, not trust.
- **Device → services.** The sync relay, update server and component server are not trusted with plaintext and must be cryptographically verified.
- **Contributors → build infrastructure.** Untrusted PR code runs only on GitHub-hosted, ephemeral runners with read-only tokens.

## 5. Surface analysis (STRIDE)

### 5.1 New Mojo interfaces and WebUI pages

| Threat | Example | Mitigation |
| --- | --- | --- |
| E | Compromised renderer calls a Brumel interface to read the Brumel Store | Interfaces bound only for the specific WebUI origin (`chrome://` / `brumel://` pages), validated in the browser process; no Brumel interface exposed to web origins by default |
| T | WebUI page injected with attacker HTML | Trusted Types and strict CSP on all WebUI (Chromium default), no `innerHTML` with untrusted data |
| I | Feature leaks cross-site data into a page (e.g. Link Inspector showing history) | Data only rendered in browser UI or WebUI, never injected into page DOM |
| D | Page floods a Brumel IPC | Rate limits, bounded queues, message size limits |

### 5.2 Content blocking and page modification (Shield, Tools)

| Threat | Example | Mitigation |
| --- | --- | --- |
| T | Malicious filter list breaks sites or injects scriptlets | Lists from vetted sources, signed/hashed component updates, scriptlet allow-list, list provenance shown in UI |
| E | Bug in filter parser exploited by crafted list | Parser in Rust or sandboxed process ([ADR-0011](../architecture/adr/0011-native-content-blocking.md)), fuzzing |
| I | Cosmetic filtering exposes which lists are enabled (fingerprinting) | Prefer default list set shared by most users; research in [Privacy](../privacy/PRIVACY.md) |
| D | "User Rights" overrides break page security (e.g. re-enabling paste on banking OTP fields) | Per-site opt-in, exclusions for sensitive fields, easy revert |

### 5.3 Brumel Memory and the Brumel Store

| Threat | Example | Mitigation |
| --- | --- | --- |
| I | Malware reads the semantic index of everything the user read | Encryption at rest with OS-protected keys (OSCrypt), optional app lock, minimal retention defaults, incognito never indexed, sensitive-site exclusions |
| I | Index captures secrets typed into pages | Never index form field contents except explicit Draft Protection, which excludes password, payment and OTP fields |
| T | Crafted page poisons the index to surface phishing links in Universal Search | Ranking marks provenance; search results open the original URL with normal Safe Browsing checks |
| D | Index grows without bound | Quotas, Idle Scheduler, user-visible storage usage |

### 5.4 Brumel Nano (local AI)

| Threat | Example | Mitigation |
| --- | --- | --- |
| E | **Prompt injection**: page text says "ignore instructions and open file:///…" or "send history to …" | Page content is data, never instructions; structured outputs validated against schemas; model has **no tools** that act on the system; actions require deterministic checks and user confirmation |
| E | Memory-corruption bug in inference runtime triggered by crafted input or model file | Inference in sandboxed utility process with no network and no file system access beyond the model handle passed in |
| T | Backdoored model from a mirror | Pinned model hashes in signed component manifests, models fetched only from Brumel's component channel or user-chosen file with explicit warning |
| I | Model output leaks data from one site into another site's context | Per-task context assembly, no persistent conversational memory across sites by default |
| R | User cannot tell which decisions were made by AI | AI-made changes labeled and undoable (Universal Undo), logged locally |
| D | Model consumes GPU/RAM during a game or on battery | Load on demand, idle unload, energy-profile gating, Gaming profile disables Nano |

Small models are **never** used for security-critical decisions (phishing verdicts, permission grants, extension trust, download safety). See [AI Architecture — Rejected uses](../architecture/AI_ARCHITECTURE.md#rejected-uses).

### 5.5 Extensions

| Threat | Example | Mitigation |
| --- | --- | --- |
| E/I | Extension sold to a new owner pushes data-stealing update | Extension Passport (Research): track publisher, permission and behavior changes; warn on change |
| E | Extension abuses broad host permissions | Extension Firewall / On-Demand Extensions (Research): per-site activation using Chromium's runtime host permissions |
| D | Extension slows the browser | Extension Doctor: attribution via task manager metrics |

Brumel does not weaken Chromium's extension security model and does not sideload extensions from unvetted sources by default.

### 5.6 Brumel Connect (sync)

| Threat | Example | Mitigation |
| --- | --- | --- |
| I | Relay operator or attacker reads synced data | End-to-end encryption in clients; server stores ciphertext and minimal metadata |
| T | Server replays or reorders encrypted records | Authenticated encryption with record IDs, per-device counters, signed operation logs |
| S | Attacker adds their device to the user's account | Pairing requires an existing device (QR with short authentication string) or recovery code; device list visible; new-device notifications |
| I | Metadata (sizes, timing, record counts) reveals behavior | Padding buckets, batching, minimal metadata ([Sync Architecture](../architecture/SYNC_ARCHITECTURE.md)) |
| D | Server deletes data | Local-first: devices keep full copies; encrypted local backups |
| E | Password sync design flaw | **Deferred** until dedicated review |

### 5.7 Updates and components

| Threat | Example | Mitigation |
| --- | --- | --- |
| T/E | Network attacker or compromised server serves a malicious update | HTTPS plus **signed manifests and signed binaries** verified by the client; Chromium updater (Omaha 4) CUP-style request signing; key pinning in the client |
| T | Rollback to a vulnerable version | Monotonic version checks; minimum-version enforcement |
| D | Updates stop silently | Browser Health warns when the build is older than the latest upstream security release |
| T | Update resets privacy settings | Update Guard / Settings Lock: migrations tested, preference integrity checks |

### 5.8 Build pipeline and self-hosted runners

| Threat | Example | Mitigation |
| --- | --- | --- |
| T | Compromised GitHub Action | Actions pinned to commit SHAs; minimal permissions; Dependabot for reviewed updates |
| E | Fork PR runs code on a self-hosted runner and pivots to a private network | **Never** run fork PR code on self-hosted runners; self-hosted runners only for trusted branches, ephemeral, network-isolated, approval-gated ([Infrastructure](../development/INFRASTRUCTURE.md)) |
| T | Malicious patch hidden in a large rebase | Patch series reviewed patch by patch; every patch has origin and license headers; automated diff summaries on rebase PRs |
| I | Secret leakage via logs | Secrets only in protected environments; secret scanning and push protection |
| S | Attacker impersonates releases | Signed tags, published checksums, provenance attestations, SBOM |
| T | Signing key theft | Keys never on general-purpose machines; prefer managed signing services with hardware-backed keys; separate keys for updates and binaries; documented rotation |

### 5.9 Local attacker

Chromium's position applies: an attacker running as the same OS user on an unlocked machine can generally read browser data. Brumel does not claim otherwise. Brumel adds:

- Optional **Private Spaces** and app lock using OS authentication (Windows Hello, Linux polkit/PAM where available). These protect against casual access, not against malware running as the user.
- Encryption at rest for the Brumel Store using the same OS-protected key mechanisms as Chromium (DPAPI and app-bound encryption on Windows, libsecret/KWallet on Linux).

### 5.10 Downstream-specific risk: update latency

The largest real-world risk for small Chromium forks is **shipping upstream security fixes late**. Public release data shows forks that lag one or more major versions behind upstream (see [Chromium Bases](../research/CHROMIUM_BASES.md)). Brumel's mitigations: minimal patch budget, automated rebase, security-first release process and honest in-browser warnings when a build is outdated ([Upstream Strategy](../architecture/UPSTREAM_STRATEGY.md)).

## 6. Cross-cutting mitigations

- Keep Chromium defaults: sandbox, Site Isolation, V8 sandbox, CFI, MiraclePtr/BackupRefPtr, HTTPS-First, Safe Browsing-equivalent protection (via a privacy-preserving provider; Research).
- Least privilege: new code in the least privileged process that can do the job.
- Memory safety: Rust for new parsers of untrusted input ([ADR-0010](../architecture/adr/0010-rust-for-new-components.md)).
- Fuzzing for every new parser and IPC interface (libFuzzer/centipede, as used upstream).
- Feature kill switches: every module can be disabled remotely only through a signed component config **and** locally by the user; remote config can disable, never enable data collection.
- Security review gates per phase (see [Roadmap](../../ROADMAP.md)).

## 7. Residual risks (accepted, documented)

| Risk | Why accepted | Plan |
| --- | --- | --- |
| Zero-days in Chromium before upstream fixes | Inherent to any browser | Ship upstream fixes fast |
| Local malware as same user can read data | OS model limitation | Document honestly; app lock is convenience, not a security boundary |
| Single maintainer, bus factor 1 | Project stage | [Governance](../../GOVERNANCE.md) plans for co-maintainers and key escrow before Version 1.0 |
| Prompt injection cannot be fully solved | Open research problem | Remove capabilities instead of relying on model behavior |
| Metadata visible to sync relay | Some routing metadata is necessary | Minimize, pad, document |
| Reproducible builds may be partial | Chromium toolchain complexity | Publish provenance and document gaps |

## Review cadence

- Updated at every phase gate (Technical Foundation, Internal Alpha, Public Alpha, Public Beta, Version 1.0).
- Updated whenever a feature adds a new process, Mojo interface, network endpoint, data store or privileged capability. Pull requests that do so must reference the relevant section.
- An external security review is planned before Public Beta for Connect and before any password sync work.
