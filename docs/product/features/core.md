<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Core — Chromium parity, build, update and distribution

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

51 entries. Epics in this module:

- **EP-CORE-01** Reproducible build, upstream tracking and supply chain — phase 1 (Technical Foundation), P0
- **EP-CORE-02** Branding, packaging and signed updates — phase 1 (Technical Foundation), P0
- **EP-CORE-03** Module system and feature registry — phase 1 (Technical Foundation), P0
- **EP-CORE-04** Chromium feature parity — phase 2 (Internal Alpha), P0
- **EP-CORE-05** Google-service replacements, DRM, codecs and Cast — phase 2 (Internal Alpha), P1
- **EP-CORE-06** Security baseline: sandbox, site isolation, HTTPS and DNS — phase 1 (Technical Foundation), P0

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [CORE-001](#core-001) | Reproducible upstream fetch | Essential | Planned | P0 | 1 |
| [CORE-002](#core-002) | Patch series system | Essential | Planned | P0 | 1 |
| [CORE-003](#core-003) | Upstream release tracking automation | Essential | Planned | P0 | 1 |
| [CORE-004](#core-004) | Brumel branding | Essential | Planned | P0 | 1 |
| [CORE-005](#core-005) | Module system and feature registry | Essential | Planned | P0 | 1 |
| [CORE-006](#core-006) | De-Googling and Google API audit | Essential | Planned | P0 | 1 |
| [CORE-007](#core-007) | CI build and release signing pipeline | Essential | Planned | P0 | 1 |
| [CORE-008](#core-008) | SBOM and dependency governance | Essential | Planned | P1 | 1 |
| [CORE-009](#core-009) | Windows installer packaging | Essential | Planned | P0 | 1 |
| [CORE-010](#core-010) | Linux packaging | Essential | Planned | P1 | 1 |
| [CORE-011](#core-011) | Crash reporting without Google | Secondary | Research | P1 | 2 |
| [CORE-012](#core-012) | Safe Browsing service strategy | Essential | Research | P0 | 2 |
| [CORE-013](#core-013) | Translation backend replacement | Secondary | Research | P2 | 4 |
| [CORE-014](#core-014) | Spellcheck dictionary hosting | Essential | Planned | P1 | 2 |
| [CORE-020](#core-020) | Modern web navigation | Essential | Planned | P0 | 2 |
| [CORE-021](#core-021) | Web standards compatibility | Essential | Planned | P0 | 2 |
| [CORE-022](#core-022) | Chrome Web Store and extensions | Essential | Planned | P0 | 2 |
| [CORE-023](#core-023) | Password manager | Essential | Planned | P0 | 2 |
| [CORE-024](#core-024) | Passkeys | Essential | Planned | P1 | 2 |
| [CORE-025](#core-025) | Autofill | Essential | Planned | P1 | 2 |
| [CORE-026](#core-026) | User profiles | Essential | Planned | P0 | 2 |
| [CORE-027](#core-027) | Incognito mode | Essential | Planned | P0 | 2 |
| [CORE-028](#core-028) | Guest mode | Essential | Planned | P2 | 2 |
| [CORE-029](#core-029) | Bookmarks | Essential | Planned | P0 | 2 |
| [CORE-030](#core-030) | History | Essential | Planned | P0 | 2 |
| [CORE-031](#core-031) | Downloads | Essential | Planned | P0 | 2 |
| [CORE-032](#core-032) | Tab groups | Essential | Planned | P1 | 2 |
| [CORE-033](#core-033) | Pinned tabs | Essential | Planned | P1 | 2 |
| [CORE-034](#core-034) | Page translation | Essential | Planned | P2 | 4 |
| [CORE-035](#core-035) | DevTools | Essential | Planned | P0 | 2 |
| [CORE-036](#core-036) | Progressive Web Apps | Essential | Planned | P1 | 2 |
| [CORE-037](#core-037) | PDF viewer | Essential | Planned | P0 | 2 |
| [CORE-038](#core-038) | Printing | Essential | Planned | P0 | 2 |
| [CORE-039](#core-039) | Spellcheck | Essential | Planned | P1 | 2 |
| [CORE-040](#core-040) | Graphics acceleration | Essential | Planned | P0 | 2 |
| [CORE-041](#core-041) | Hardware media decoding | Essential | Planned | P0 | 2 |
| [CORE-042](#core-042) | Picture-in-Picture | Essential | Planned | P1 | 2 |
| [CORE-043](#core-043) | Screenshots | Essential | Planned | P2 | 2 |
| [CORE-044](#core-044) | Data import and export | Essential | Planned | P0 | 2 |
| [CORE-045](#core-045) | Permission management | Essential | Planned | P0 | 2 |
| [CORE-046](#core-046) | Secure DNS (DNS over HTTPS) | Essential | Planned | P0 | 1 |
| [CORE-047](#core-047) | HTTPS-First / HTTPS-Only | Essential | Planned | P0 | 1 |
| [CORE-048](#core-048) | Sandboxing | Essential | Planned | P0 | 1 |
| [CORE-049](#core-049) | Site isolation | Essential | Planned | P0 | 1 |
| [CORE-050](#core-050) | Phishing and malware protection | Essential | Planned | P0 | 2 |
| [CORE-051](#core-051) | Signed automatic updates | Essential | Planned | P0 | 1 |
| [CORE-052](#core-052) | Chromecast / Cast | Essential | Planned | P3 | 4 |
| [CORE-053](#core-053) | DRM (Widevine) | Essential | Research | P1 | 3 |
| [CORE-054](#core-054) | Proprietary codecs | Essential | Research | P1 | 2 |
| [CORE-055](#core-055) | Disable sandbox or site isolation to reduce memory | Rejected | Rejected | P3 | 0 |
| [CORE-056](#core-056) | Electron-based browser shell | Rejected | Rejected | P3 | 0 |

<a id="core-001"></a>

## CORE-001 — Reproducible upstream fetch

`Essential` · `Planned` · **P0** · Impact Critical · Complexity L · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-01 (Reproducible build, upstream tracking and supply chain)

Scripted, pinned retrieval of Chromium source and dependencies at the revision recorded in config/upstream.json.

- **Problem:** Ad-hoc checkouts make builds unreproducible and security updates slow.
- **Use case:** A contributor runs one script and gets a byte-identical source tree for the pinned Chromium version.
- **Segments:** Maintainers, Contributors
- **Dependencies:** —
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Build-time only: ~100+ GB disk and long first fetch. · **Infrastructure cost:** None
- **Security risk:** High — fetch integrity is a supply-chain boundary.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - Fetch script reproduces the pinned revision on Windows and Linux
  - Source tree hash is recorded and verified
  - No Chromium source is committed to the Brumel repository
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Chromium's depot_tools/gclient pulls hundreds of dependencies whose own pins change per release; exact byte-reproducibility of the tree is achievable, reproducible binaries are a separate, harder goal.

<a id="core-002"></a>

## CORE-002 — Patch series system

`Essential` · `Planned` · **P0** · Impact Critical · Complexity M · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-01 (Reproducible build, upstream tracking and supply chain)

Ordered, categorized patch series applied on top of pinned upstream, with tooling to apply, refresh and validate patches.

- **Problem:** Long-lived forks with merged history are expensive to rebase onto every Chromium release.
- **Use case:** On a new Chromium stable, the maintainer refreshes the series and sees exactly which patches failed.
- **Segments:** Maintainers, Contributors
- **Dependencies:** [CORE-001](#core-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - Patches apply cleanly to the pinned revision in CI
  - Each patch has a header with purpose, owner and upstream status
  - A refresh tool reports conflicting patches
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Patches touching hot upstream files (tab strip, settings, network) will conflict on most major rebases; the series must stay small or rebase cost will exceed one maintainer's capacity.

<a id="core-003"></a>

## CORE-003 — Upstream release tracking automation

`Essential` · `Planned` · **P0** · Impact Critical · Complexity M · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-01 (Reproducible build, upstream tracking and supply chain)

Automation that detects new Chromium stable and security releases and opens a rebase task with the version delta.

- **Problem:** Missing an upstream security release leaves users exposed to known, often exploited, vulnerabilities.
- **Use case:** A Chromium security release is published; within hours an issue with the new version and changelog link appears.
- **Segments:** Maintainers, Contributors
- **Dependencies:** [CORE-002](#core-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** Low — scheduled CI job.
- **Security risk:** High — update latency is the main security metric of a fork.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - New stable versions are detected automatically
  - An issue/PR is opened with version and release notes
  - Time from upstream release to detection is logged
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Detection is only the first step: actual update latency is bounded by full rebuild time (hours per platform) and test capacity, which automation cannot remove.

<a id="core-004"></a>

## CORE-004 — Brumel branding

`Essential` · `Planned` · **P0** · Impact High · Complexity M · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-02 (Branding, packaging and signed updates)

Product name, icons, strings, installer assets and internal page branding replaced through patches and resource overrides.

- **Problem:** A build that still says Chromium/Chrome confuses users and may misuse Google trademarks.
- **Use case:** The first internal build launches as Brumel with its own icon, name and about page.
- **Segments:** All users
- **Dependencies:** [CORE-002](#core-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - No Google/Chrome trademarks appear in user-visible UI
  - About page shows Brumel and the Chromium version
  - Branding is applied via patches/resources, not manual edits
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Some Chrome/Google strings and icons live in generated resources and component manifests; complete removal needs audits on every rebase, and Chromium's own name must remain in attributions.

<a id="core-005"></a>

## CORE-005 — Module system and feature registry

`Essential` · `Planned` · **P0** · Impact Critical · Complexity L · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-03 (Module system and feature registry)

Registry that declares every Brumel module, its prefs, flags, services and background work, so disabled modules create no services, timers or processes.

- **Problem:** Feature-rich browsers keep optional features running, consuming memory and expanding attack surface.
- **Use case:** A user disables Brumel Nano; its services are never constructed and no model process starts.
- **Segments:** All users
- **Dependencies:** [CORE-002](#core-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Product principle; to be validated by measuring disabled-module overhead.
- **Acceptance criteria:**
  - Each module can be fully disabled via settings and policy
  - A test asserts disabled modules create no KeyedServices, timers or processes
  - Module state is visible in an internal page
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Chromium services are not designed to be absent; some upstream code paths assume their existence, so certain modules may only be disabled behaviorally rather than fully unconstructed.

<a id="core-006"></a>

## CORE-006 — De-Googling and Google API audit

`Essential` · `Planned` · **P0** · Impact High · Complexity M · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-01 (Reproducible build, upstream tracking and supply chain)

Audit and removal/replacement of Google service endpoints and API keys, reusing ungoogled-chromium patches where suitable.

- **Problem:** Chromium builds contact Google services by default; third-party builds may not use several private Google APIs.
- **Use case:** The Glass Box view of a fresh profile shows no unexpected requests to Google endpoints.
- **Segments:** Maintainers, Contributors
- **Dependencies:** [CORE-002](#core-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — reduces data flow to third parties.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: ungoogled-chromium, Helium.
- **Acceptance criteria:**
  - Network capture of a fresh profile documents every outbound request
  - Each remaining Google endpoint is justified or removed
  - Imported ungoogled-chromium patches keep their attribution
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Removing Google endpoints also removes functionality (Safe Browsing, translate, spellcheck, component updates) that must be replaced elsewhere; ungoogled-chromium patches lag upstream by days to weeks.

<a id="core-007"></a>

## CORE-007 — CI build and release signing pipeline

`Essential` · `Planned` · **P0** · Impact Critical · Complexity XL · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-01 (Reproducible build, upstream tracking and supply chain)

CI that builds, tests and signs release artifacts on trusted runners, separated from untrusted pull request jobs.

- **Problem:** Chromium builds are too heavy for free hosted runners, and signing keys on shared machines are a supply-chain risk.
- **Use case:** A tagged release produces signed Windows and Linux artifacts from a trusted runner with recorded provenance.
- **Segments:** Maintainers, Contributors
- **Dependencies:** [CORE-001](#core-001), [CORE-002](#core-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** Medium — self-hosted build machines or paid runners; signing certificate costs.
- **Security risk:** Critical path — signing keys must be isolated (HSM or offline where possible).
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - Untrusted PR code never runs on runners with signing access
  - Release artifacts are signed and hashes published
  - Build provenance is recorded
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Free hosted runners cannot build Chromium within time and disk limits; trusted self-hosted or paid runners are needed, and code-signing certificates cost money every year.

<a id="core-008"></a>

## CORE-008 — SBOM and dependency governance

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-01 (Reproducible build, upstream tracking and supply chain)

Software bill of materials for each release, license inventory and dependency update policy.

- **Problem:** Users and auditors cannot verify what third-party code ships in a browser build.
- **Use case:** A security researcher downloads the SBOM of a release and checks it for a vulnerable library.
- **Segments:** Maintainers, Contributors
- **Dependencies:** [CORE-007](#core-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - Each release publishes an SBOM in SPDX or CycloneDX
  - THIRD_PARTY_NOTICES is generated from the build
  - New dependencies require license review
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Chromium vendors hundreds of third_party components with heterogeneous metadata; a complete, accurate SBOM requires tooling work and will initially be best-effort.

<a id="core-009"></a>

## CORE-009 — Windows installer packaging

`Essential` · `Planned` · **P0** · Impact High · Complexity M · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-02 (Branding, packaging and signed updates)

Signed Windows installer (per-user and system-wide) with clean uninstall and no bundled software.

- **Problem:** Unsigned installers trigger SmartScreen warnings and teach users unsafe habits.
- **Use case:** A user installs Brumel without admin rights and uninstalls it leaving no residue except opt-in profile data.
- **Segments:** Everyday users
- **Dependencies:** [CORE-004](#core-004), [CORE-007](#core-007)
- **Platforms:** Windows Planned · Linux N/A · macOS N/A · Android N/A
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** Medium — code-signing certificate cost.
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - Installer is Authenticode-signed
  - Per-user install works without admin
  - Uninstall removes binaries and offers to keep or delete profile data
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** SmartScreen reputation for a new publisher builds slowly even with a valid certificate, so early signed installers may still show warnings.

<a id="core-010"></a>

## CORE-010 — Linux packaging

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-02 (Branding, packaging and signed updates)

Signed packages for major distributions (deb/rpm) and a candidate Flatpak, with repository-based updates.

- **Problem:** Linux users expect distribution-native updates and sandboxed packaging options.
- **Use case:** A Debian/Ubuntu user adds the signed repository and receives updates through apt.
- **Segments:** Everyday users
- **Dependencies:** [CORE-004](#core-004), [CORE-007](#core-007)
- **Platforms:** Windows N/A · Linux Planned · macOS N/A · Android N/A
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** Low — static hosting for repositories.
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - Signed deb and rpm packages are produced
  - Repository metadata is signed
  - Flatpak viability is documented
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Each distribution and packaging format (deb, rpm, Flatpak) adds testing and maintenance; Flatpak's sandbox conflicts with Chromium's own sandbox and needs zypak-style workarounds.

<a id="core-011"></a>

## CORE-011 — Crash reporting without Google

`Secondary` · `Research` · **P1** · Impact Medium · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Opt-in Crashpad reports sent to a Brumel-controlled or self-hostable backend, with minidump scrubbing.

- **Problem:** Without crash data a small team cannot fix stability issues; sending crashes to Google is not acceptable.
- **Use case:** A tester opts in; a crash is uploaded with a local receipt and can be referenced in a bug report.
- **Segments:** Maintainers, Contributors
- **Dependencies:** [CORE-006](#core-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** Low/Medium — crash backend hosting.
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Medium — minidumps can contain page data; scrubbing and consent required.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - Crash upload is off by default and opt-in
  - Users can view and delete pending reports
  - Backend can be self-hosted
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Minidumps can include page memory; even with scrubbing, crash reports are sensitive, and a self-hosted backend adds an operational service to maintain.

<a id="core-012"></a>

## CORE-012 — Safe Browsing service strategy

`Essential` · `Research` · **P0** · Impact Critical · Complexity L · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Decide and implement how phishing/malware protection works without Google's commercial-restricted APIs (proxy, alternative lists, or licensed access).

- **Problem:** Removing Safe Browsing protects privacy but leaves users exposed to phishing; Google's API terms restrict some uses.
- **Use case:** A user visits a known phishing page and receives a warning without their full URL being sent to a third party.
- **Segments:** All users
- **Dependencies:** [CORE-006](#core-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** Medium — proxy or list hosting.
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: Brave proxies Safe Browsing requests (to be verified in detail).
- **Acceptance criteria:**
  - Legal/terms review documented
  - Protection works with privacy-preserving lookups
  - Fallback behavior when the service is unavailable is defined
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Google's Safe Browsing API terms restrict commercial and redistribution use; any privacy-preserving proxy or alternative list still requires a service with ongoing cost and may have lower coverage.

<a id="core-013"></a>

## CORE-013 — Translation backend replacement

`Secondary` · `Research` · **P2** · Impact Medium · Complexity L · Phase 4 (Public Beta) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Replace Chrome's private Google Translate endpoint with local translation models or a user-selected, self-hostable service.

- **Problem:** Chromium's translate UI depends on a Google endpoint that third-party builds should not rely on.
- **Use case:** A user translates a page locally without sending its content to any server.
- **Segments:** Everyday users
- **Dependencies:** [CORE-006](#core-006), [NANO-019](nano.md#nano-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Optional · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - No default request to Google Translate endpoints
  - Local or user-configured backend works with the existing translate UI
  - Quality evaluated per language pair
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Moved to Phase 4 because it depends on the Nano runtime.

<a id="core-014"></a>

## CORE-014 — Spellcheck dictionary hosting

`Essential` · `Planned` · **P1** · Impact Medium · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Host or mirror Hunspell dictionaries with signed manifests instead of downloading them from Google servers.

- **Problem:** Chromium downloads spellcheck dictionaries from Google infrastructure by default.
- **Use case:** A user adds Spanish spellcheck and the dictionary downloads from a Brumel-controlled, verified source.
- **Segments:** All users
- **Dependencies:** [CORE-006](#core-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** Low — static hosting.
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Established practice: ungoogled-chromium, Brave and Helium use patch-based builds on pinned upstream.
- **Acceptance criteria:**
  - Dictionary downloads use Brumel-controlled URLs
  - Downloads are integrity-checked
  - Dictionary licenses are tracked
- **Origin:** FOUND · **Duplicate of:** —
- **Limitations / notes:** Mirroring dictionaries requires tracking each dictionary's own license (many are GPL/LGPL/MPL) and keeping them updated; Windows native spellcheck may be preferred where available.

<a id="core-020"></a>

## CORE-020 — Modern web navigation

`Essential` · `Planned` · **P0** · Impact Critical · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Blink and V8 rendering with Chromium's navigation stack, kept current with upstream stable.

- **Problem:** A browser that breaks sites is abandoned regardless of features.
- **Use case:** A user opens banking, video and web-app sites with the same behavior as in Chrome.
- **Segments:** All users
- **Dependencies:** [CORE-001](#core-001), [CORE-004](#core-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Top-site smoke tests pass
  - No Brumel patch alters Blink/V8 behavior without an ADR
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Brumel cannot fix site-specific bugs or sites that block non-Chrome user agents; any Blink/V8 patch is avoided because it would compound rebase cost.

<a id="core-021"></a>

## CORE-021 — Web standards compatibility

`Essential` · `Planned` · **P0** · Impact Critical · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Web Platform Tests parity with the matching Chromium version.

- **Problem:** Downstream patches can silently break web APIs.
- **Use case:** A developer tests a site in Brumel and gets Chromium-equivalent results.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - WPT pass rate within an agreed tolerance of the same Chromium version
  - Regressions are tracked as release blockers
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. WPT runs are heavy and will be sampled per release at first; parity is measured against the same Chromium version, not against Chrome's Google-specific behavior.

<a id="core-022"></a>

## CORE-022 — Chrome Web Store and extensions

`Essential` · `Planned` · **P0** · Impact Critical · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Install and update Chromium extensions, including from the Chrome Web Store where its terms allow.

- **Problem:** Users will not switch if their extensions do not work.
- **Use case:** A user installs a password manager extension from the Chrome Web Store.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Medium — extensions are a major privacy risk; see SHD-013.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Top 50 extensions install and update
  - Extension updates work
  - Manifest V2 status documented honestly
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Upstream removed Manifest V2; keeping MV2 would require costly patches and is Research.

<a id="core-023"></a>

## CORE-023 — Password manager

`Essential` · `Planned` · **P0** · Impact Critical · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Chromium's local password manager with OS-protected encryption, without Google account sync.

- **Problem:** Users need a built-in, secure credential store.
- **Use case:** A user saves and autofills credentials, protected by OS encryption.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** High — credentials are the highest-value local data.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Passwords encrypted with OSCrypt
  - Import/export works
  - No cloud sync until CON-019 passes review
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Without Google account sync, passwords stay on one device until CON-019; OS-level encryption does not protect against malware running as the user.

<a id="core-024"></a>

## CORE-024 — Passkeys

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

WebAuthn/passkeys using platform authenticators (e.g. Windows Hello) and security keys.

- **Problem:** Passkeys replace passwords, but Google Password Manager passkey sync is not available to forks.
- **Use case:** A user signs in with a passkey stored in Windows Hello.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Platform and roaming authenticators work
  - Limits of passkey sync documented
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Google-synced passkeys are not available.

<a id="core-025"></a>

## CORE-025 — Autofill

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Addresses and payment-free form autofill stored locally.

- **Problem:** Retyping personal data is slow and error-prone.
- **Use case:** A user fills a shipping form with one click.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Address autofill works offline
  - Data stored encrypted and deletable
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Payment card autofill tied to Google Pay is unavailable; local cards may be supported later only after a security review.

<a id="core-026"></a>

## CORE-026 — User profiles

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Multiple isolated browser profiles with separate data.

- **Problem:** Work and personal browsing must not mix.
- **Use case:** A user keeps separate work and personal profiles.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Profiles isolate cookies, history and extensions
  - Profile picker works without sign-in
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Profiles are heavyweight (separate processes and storage); lighter context separation is the job of Multi Identity (WRK-010).

<a id="core-027"></a>

## CORE-027 — Incognito mode

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Private windows with ephemeral storage.

- **Problem:** Users need sessions that leave no local history.
- **Use case:** A user checks a gift purchase without leaving history.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - No history/cookies persist after closing
  - Brumel Memory never indexes incognito (MEM-018)
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Incognito does not hide activity from networks, employers or sites; extensions allowed in incognito can still observe browsing.

<a id="core-028"></a>

## CORE-028 — Guest mode

`Essential` · `Planned` · **P2** · Impact Medium · Complexity XS · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Temporary guest profile for other people using the device.

- **Problem:** Lending a computer exposes the owner's data.
- **Use case:** A friend browses on the user's laptop without seeing their tabs.
- **Segments:** All users
- **Dependencies:** [CORE-026](#core-026)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Guest sessions are wiped on exit
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Guest mode cannot prevent the device owner or malware from observing a guest session in progress.

<a id="core-029"></a>

## CORE-029 — Bookmarks

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Bookmark manager, bar and import/export.

- **Problem:** Users rely on bookmarks as long-term memory.
- **Use case:** A user imports bookmarks from Chrome and organizes them.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Import from Chrome/Firefox/HTML
  - Export to HTML
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Bookmark sync across devices depends on Connect; import fidelity from other browsers varies (tags, keywords, separators).

<a id="core-030"></a>

## CORE-030 — History

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Local browsing history with search and deletion.

- **Problem:** Users need to find pages again.
- **Use case:** A user finds yesterday's article by title.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - History search works
  - Per-item and range deletion works
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. History is stored unencrypted by upstream design apart from OS disk encryption; Brumel Memory features must not duplicate it unnecessarily.

<a id="core-031"></a>

## CORE-031 — Downloads

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Download manager with dangerous-file warnings.

- **Problem:** Downloads are a core browser task and a malware vector.
- **Use case:** A user downloads and opens a PDF from the downloads page.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Downloads resume after transient failure where servers allow
  - Dangerous file types warn
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Dangerous-file warnings rely on Safe Browsing-type services (CORE-012); without them only file-type heuristics remain.

<a id="core-032"></a>

## CORE-032 — Tab groups

`Essential` · `Planned` · **P1** · Impact Medium · Complexity XS · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Chromium tab groups with colors and names.

- **Problem:** Many open tabs become unmanageable.
- **Use case:** A user groups tabs for a trip.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Tab groups persist across restarts
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Tab group sync relies on Google sync upstream; in Brumel it waits for Connect.

<a id="core-033"></a>

## CORE-033 — Pinned tabs

`Essential` · `Planned` · **P1** · Impact Medium · Complexity XS · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Pinned tabs that persist and stay compact.

- **Problem:** Always-open apps waste tab-strip space.
- **Use case:** A user pins mail and calendar.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Pinned tabs restore on startup
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Pinned tabs still load at startup unless Instant Startup defers them, so they are not free in memory.

<a id="core-034"></a>

## CORE-034 — Page translation

`Essential` · `Planned` · **P2** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Translate UI for foreign-language pages, backed by CORE-013 instead of Google's endpoint.

- **Problem:** Users read content in languages they do not speak.
- **Use case:** A user translates a German news page.
- **Segments:** All users
- **Dependencies:** [CORE-013](#core-013)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Translate UI works with a non-Google backend
  - User can disable translation fully
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** The Chrome translate UI exists in Chromium but its default backend is Google; Brumel needs CORE-013.

<a id="core-035"></a>

## CORE-035 — DevTools

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Chromium DevTools.

- **Problem:** Developers need standard tooling.
- **Use case:** A developer debugs a page with DevTools.
- **Segments:** Developers
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - DevTools works including remote debugging opt-in
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Some DevTools features call Google services (e.g. AI assistance, Lighthouse report uploads) and must be disabled or replaced.

<a id="core-036"></a>

## CORE-036 — Progressive Web Apps

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Install PWAs as standalone app windows.

- **Problem:** Web apps should behave like native apps.
- **Use case:** A user installs a music web app to the taskbar.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - PWA install/uninstall works on Windows and Linux
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Linux desktop integration of PWAs varies by desktop environment; app shortcuts and protocol handlers may behave inconsistently.

<a id="core-037"></a>

## CORE-037 — PDF viewer

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

PDFium-based built-in PDF viewer.

- **Problem:** PDFs must open safely in the browser.
- **Use case:** A user reads an invoice PDF.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - PDF viewer works offline and sandboxed
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. PDFium renders and annotates but is not a full editor; complex forms (XFA) are poorly supported.

<a id="core-038"></a>

## CORE-038 — Printing

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Print and print-to-PDF via system dialogs.

- **Problem:** Users print tickets and documents.
- **Use case:** A user prints a boarding pass.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - System print dialog and save-as-PDF work
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Cloud printing no longer exists; printing quality depends on OS print drivers.

<a id="core-039"></a>

## CORE-039 — Spellcheck

`Essential` · `Planned` · **P1** · Impact Medium · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Hunspell spellcheck (and Windows native spellcheck where available).

- **Problem:** Typos in forms and email.
- **Use case:** A user writes an email with underlined misspellings.
- **Segments:** All users
- **Dependencies:** [CORE-014](#core-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Spellcheck works without Google enhanced spellcheck
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Only languages with Hunspell dictionaries are covered; grammar checking is not included.

<a id="core-040"></a>

## CORE-040 — Graphics acceleration

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

GPU rasterization and compositing via Chromium's GPU process.

- **Problem:** Software rendering wastes CPU and battery.
- **Use case:** A user scrolls a heavy page smoothly.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - GPU acceleration enabled on supported drivers with blocklist respected
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Driver bugs force upstream GPU blocklists, so some machines fall back to software rendering regardless of Brumel settings.

<a id="core-041"></a>

## CORE-041 — Hardware media decoding

`Essential` · `Planned` · **P0** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Hardware video decode (D3D11/VA-API) where drivers support it.

- **Problem:** Software video decoding drains battery.
- **Use case:** A user watches 4K video with low CPU usage.
- **Segments:** All users
- **Dependencies:** [CORE-040](#core-040)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Hardware decode verified on Windows and on Linux VA-API reference drivers
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Linux VA-API support varies by driver and distribution.

<a id="core-042"></a>

## CORE-042 — Picture-in-Picture

`Essential` · `Planned` · **P1** · Impact Medium · Complexity XS · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Standard and Document Picture-in-Picture.

- **Problem:** Users watch video while working.
- **Use case:** A user floats a lecture video.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - PiP works for HTML5 video
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Sites can disable Picture-in-Picture with a standard attribute; Universal PiP (TLS-006) addresses that separately.

<a id="core-043"></a>

## CORE-043 — Screenshots

`Essential` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Capture visible area or region of a page.

- **Problem:** Users need quick captures.
- **Use case:** A user captures part of a page to share.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Region capture saves to file/clipboard
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Region capture covers the visible viewport; full-page capture is TLS-016.

<a id="core-044"></a>

## CORE-044 — Data import and export

`Essential` · `Planned` · **P0** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Import bookmarks, history, passwords and settings from other browsers; export in standard formats.

- **Problem:** Switching browsers is blocked by data lock-in.
- **Use case:** A Chrome user imports everything on first run.
- **Segments:** All users
- **Dependencies:** [CORE-029](#core-029), [CORE-023](#core-023)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Import from Chrome, Edge, Firefox, Brave
  - Export bookmarks (HTML) and passwords (CSV) with warnings
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Importing passwords from other browsers depends on their OS-bound encryption; some browsers (Arc, Safari on Windows) offer limited or no import path.

<a id="core-045"></a>

## CORE-045 — Permission management

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Per-site permissions for camera, microphone, location, notifications, etc.

- **Problem:** Sites over-request permissions.
- **Use case:** A user revokes a site's location permission.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Per-site permissions editable and revocable
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Permission prompts are upstream UI; deep changes (timelines, one-time grants for all types) are separate Shield features with their own patches.

<a id="core-046"></a>

## CORE-046 — Secure DNS (DNS over HTTPS)

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-06 (Security baseline: sandbox, site isolation, HTTPS and DNS)

Chromium's DoH with a curated, non-Google default choice and custom resolvers.

- **Problem:** Plain DNS leaks browsing to the network.
- **Use case:** A user selects a privacy-focused DoH resolver.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - DoH works with custom resolver
  - Default provider choice documented
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. DoH hides DNS from the local network but the resolver operator still sees queries; enterprise or captive-portal networks may block it.

<a id="core-047"></a>

## CORE-047 — HTTPS-First / HTTPS-Only

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-06 (Security baseline: sandbox, site isolation, HTTPS and DNS)

HTTPS upgrades and optional HTTPS-only mode with interstitial.

- **Problem:** HTTP connections can be intercepted.
- **Use case:** A user enables HTTPS-only mode.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - HTTPS-only mode blocks HTTP with clear warning
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. HTTPS-only interstitials will appear for legacy local devices (routers, printers); users need per-site exceptions.

<a id="core-048"></a>

## CORE-048 — Sandboxing

`Essential` · `Planned` · **P0** · Impact Critical · Complexity S · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-06 (Security baseline: sandbox, site isolation, HTTPS and DNS)

Chromium's multi-process sandbox kept fully enabled on all platforms.

- **Problem:** Renderer compromises must not reach the OS.
- **Use case:** A malicious page exploit is contained in the renderer sandbox.
- **Segments:** All users
- **Dependencies:** [CORE-020](#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Critical — non-negotiable.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Sandbox status verified in CI on every platform
  - No patch disables or weakens sandbox
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Some Linux packaging environments (containers, Flatpak) complicate the namespace sandbox; Brumel must not ship a build where it degrades silently.

<a id="core-049"></a>

## CORE-049 — Site isolation

`Essential` · `Planned` · **P0** · Impact Critical · Complexity S · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-06 (Security baseline: sandbox, site isolation, HTTPS and DNS)

Full site-per-process isolation, never relaxed to save memory.

- **Problem:** Cross-site attacks (Spectre-class) require process isolation.
- **Use case:** Two sites never share a renderer process.
- **Segments:** All users
- **Dependencies:** [CORE-048](#core-048)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Critical — non-negotiable.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Site isolation enabled on desktop
  - Regression test asserts it
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Inherited from Chromium; expected with the first build. Site isolation increases process count and memory; Brumel accepts that cost and recovers memory through tab lifecycle instead.

<a id="core-050"></a>

## CORE-050 — Phishing and malware protection

`Essential` · `Planned` · **P0** · Impact Critical · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Warnings for known phishing/malware pages and dangerous downloads, backed by CORE-012.

- **Problem:** Phishing is one of the most common ways users are harmed.
- **Use case:** A user clicking a phishing link from email sees a full-page warning.
- **Segments:** All users
- **Dependencies:** [CORE-012](#core-012)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Known-bad test URLs are blocked
  - Privacy properties of lookups documented
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Not inherited as-is: depends on the Safe Browsing strategy (CORE-012).

<a id="core-051"></a>

## CORE-051 — Signed automatic updates

`Essential` · `Planned` · **P0** · Impact Critical · Complexity L · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-02 (Branding, packaging and signed updates)

Automatic, signed, verifiable updates (Windows: Chromium updater / Omaha 4 protocol; Linux: signed repositories).

- **Problem:** Unpatched browsers are the main real-world risk; Chromium ships without an update service.
- **Use case:** A security fix reaches users automatically within days of upstream.
- **Segments:** All users
- **Dependencies:** [CORE-009](#core-009), [CORE-010](#core-010), [CORE-007](#core-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** Low/Medium — update manifests and binary hosting/CDN.
- **Security risk:** Critical — update channel compromise equals full compromise.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Update metadata and binaries are signed and verified
  - Rollback-safe staged rollout
  - Updates can be paused but never silently disabled
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Also covers the foundation requirement for a signed updater; Chromium itself provides no update service.

<a id="core-052"></a>

## CORE-052 — Chromecast / Cast

`Essential` · `Planned` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Casting to Google Cast devices where technically and legally possible.

- **Problem:** Users cast videos to TVs.
- **Use case:** A user casts a video tab to a TV.
- **Segments:** All users
- **Dependencies:** [CORE-006](#core-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Medium — Cast discovery uses local network.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Feasibility and terms documented
  - If shipped, Cast is opt-in
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Cast depends on Google components; availability in forks varies. Research.

<a id="core-053"></a>

## CORE-053 — DRM (Widevine)

`Essential` · `Research` · **P1** · Impact High · Complexity L · Phase 3 (Public Alpha) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Widevine CDM support for streaming services, subject to a license agreement with Google and VMP signing.

- **Problem:** Without Widevine, major streaming services do not play or play only in low resolution.
- **Use case:** A user streams a subscription video service in HD.
- **Segments:** All users
- **Dependencies:** [CORE-007](#core-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: Brave, Vivaldi, Opera ship Widevine; many small forks cannot.
- **Acceptance criteria:**
  - Licensing path documented
  - If unavailable, limitations are stated clearly to users
  - CDM is a removable, opt-in component
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Requires an agreement with Google; HD playback on Windows/macOS needs VMP signing. Not guaranteed.

<a id="core-054"></a>

## CORE-054 — Proprietary codecs

`Essential` · `Research` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

H.264/AAC (and HEVC where hardware allows) via proprietary_codecs and ffmpeg_branding build flags, after patent/licensing review.

- **Problem:** Many sites still serve H.264/AAC; missing codecs break video playback.
- **Use case:** A user plays an H.264 video on a news site.
- **Segments:** All users
- **Dependencies:** [CORE-001](#core-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Licensing review documented per distribution channel
  - Codec support matrix published
- **Origin:** S8 · **Duplicate of:** —
- **Limitations / notes:** Patent licensing obligations differ by country and distribution channel; legal review required.

<a id="core-055"></a>

## CORE-055 — Disable sandbox or site isolation to reduce memory

`Rejected` · `Rejected` · **P3** · Impact Low · Complexity XS · Phase 0 (Pre-development) · Pillar Foundation · Epic EP-CORE-06 (Security baseline: sandbox, site isolation, HTTPS and DNS)

Proposal pattern: relax sandboxing, site isolation or mitigations to win memory or speed benchmarks.

- **Problem:** Some browsers or guides trade security for lower resource use.
- **Use case:** N/A — rejected. Safe alternative: ENG-019 tab lifecycle and ENG-005 RAM budgets.
- **Segments:** All users
- **Dependencies:** —
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Critical — would expose users to cross-site and sandbox-escape attacks.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Project principle (security over benchmarks).
- **Acceptance criteria:**
  - Never shipped
  - CI asserts sandbox and site isolation are enabled (CORE-048, CORE-049)
- **Origin:** S16 · **Duplicate of:** —
- **Limitations / notes:** Rejected permanently by project principle.

<a id="core-056"></a>

## CORE-056 — Electron-based browser shell

`Rejected` · `Rejected` · **P3** · Impact Low · Complexity XS · Phase 0 (Pre-development) · Pillar Foundation · Epic EP-CORE-03 (Module system and feature registry)

Proposal pattern: build the final browser as an Electron application.

- **Problem:** Electron simplifies UI work but lags upstream security fixes and lacks a full browser security model.
- **Use case:** N/A — rejected. Alternative: native Chromium Views + WebUI (ADR-0005).
- **Segments:** All users
- **Dependencies:** —
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Project principle; ADR-0005.
- **Acceptance criteria:**
  - Never used for the shipping browser
- **Origin:** S3 · **Duplicate of:** —
- **Limitations / notes:** Rejected by ADR-0005.
