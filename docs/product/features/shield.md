<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Shield — privacy and security

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

39 entries. Epics in this module:

- **EP-SHD-01** Native content blocking (Clean Web) — phase 2 (Internal Alpha), P0
- **EP-SHD-02** Permissions and extension control — phase 3 (Public Alpha), P1
- **EP-SHD-03** Transparency: Glass Box, Privacy Receipt and telemetry — phase 3 (Public Alpha), P1
- **EP-SHD-04** Local data, credential and session protection — phase 2 (Internal Alpha), P1
- **EP-SHD-05** Web safety tools and advanced privacy — phase 3 (Public Alpha), P2

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [SHD-001](#shd-001) | Clean Web native content blocking | Flagship | Planned | P0 | 2 |
| [SHD-002](#shd-002) | Pop-up blocking | Essential | Planned | P0 | 2 |
| [SHD-003](#shd-003) | Autoplay blocking | Essential | Planned | P1 | 2 |
| [SHD-004](#shd-004) | Automated optional-cookie rejection | Flagship | Research | P1 | 3 |
| [SHD-005](#shd-005) | Notification prompt blocking | Essential | Planned | P1 | 2 |
| [SHD-006](#shd-006) | Fingerprinting protection | Flagship | Research | P1 | 3 |
| [SHD-007](#shd-007) | Tracking parameter stripping | Essential | Planned | P1 | 2 |
| [SHD-008](#shd-008) | Malicious redirect protection | Secondary | Planned | P2 | 3 |
| [SHD-009](#shd-009) | Smart Back | Secondary | Planned | P2 | 3 |
| [SHD-010](#shd-010) | Self Repair | Secondary | Research | P2 | 3 |
| [SHD-011](#shd-011) | Permission Timeline | Secondary | Planned | P2 | 3 |
| [SHD-012](#shd-012) | One-Time Permissions | Essential | Planned | P1 | 3 |
| [SHD-013](#shd-013) | Extension Firewall | Flagship | Planned | P1 | 3 |
| [SHD-014](#shd-014) | Privacy Receipt | Secondary | Planned | P2 | 3 |
| [SHD-015](#shd-015) | Smart Cleanup | Secondary | Planned | P2 | 3 |
| [SHD-016](#shd-016) | Link Inspector | Secondary | Planned | P2 | 3 |
| [SHD-017](#shd-017) | Clipboard Guard | Secondary | Planned | P2 | 3 |
| [SHD-018](#shd-018) | Settings Lock *(→ ENG-016)* | Essential | Planned | P1 | 2 |
| [SHD-019](#shd-019) | Biometric lock | Secondary | Planned | P2 | 4 |
| [SHD-020](#shd-020) | Local data encryption | Essential | Planned | P1 | 2 |
| [SHD-021](#shd-021) | End-to-end encrypted sync *(→ CON-020)* | Essential | Research | P0 | 4 |
| [SHD-022](#shd-022) | Credential protection | Essential | Planned | P1 | 3 |
| [SHD-023](#shd-023) | DNS over HTTPS (Shield) *(→ CORE-046)* | Essential | Planned | P0 | 1 |
| [SHD-024](#shd-024) | HTTPS-only mode (Shield) *(→ CORE-047)* | Essential | Planned | P0 | 1 |
| [SHD-025](#shd-025) | Session isolation *(→ WRK-010)* | Flagship | Planned | P1 | 4 |
| [SHD-026](#shd-026) | Phishing protection (Shield) *(→ CORE-050)* | Essential | Planned | P0 | 2 |
| [SHD-027](#shd-027) | Optional, auditable telemetry | Essential | Planned | P1 | 3 |
| [SHD-028](#shd-028) | Advanced private mode | Secondary | Research | P2 | 4 |
| [SHD-029](#shd-029) | Tor integration | Deferred | Deferred | P3 | 6 |
| [SHD-030](#shd-030) | Dark Pattern Radar | Experimental | Research | P3 | 4 |
| [SHD-031](#shd-031) | User Rights | Secondary | Planned | P2 | 3 |
| [SHD-032](#shd-032) | Guaranteed Exit | Secondary | Planned | P2 | 3 |
| [SHD-033](#shd-033) | Screen Share Shield | Secondary | Research | P2 | 4 |
| [SHD-034](#shd-034) | Glass Box | Flagship | Planned | P1 | 3 |
| [SHD-035](#shd-035) | Extension Passport | Flagship | Planned | P1 | 3 |
| [SHD-036](#shd-036) | Credential Sentinel | Experimental | Research | P2 | 4 |
| [SHD-037](#shd-037) | Agent Clean Room | Deferred | Research | P3 | 6 |
| [SHD-038](#shd-038) | Verified Downloads | Secondary | Research | P2 | 4 |
| [SHD-039](#shd-039) | Hardened Sessions | Experimental | Research | P2 | 4 |

<a id="shd-001"></a>

## SHD-001 — Clean Web native content blocking

`Flagship` · `Planned` · **P0** · Impact Critical · Complexity L · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-SHD-01 (Native content blocking (Clean Web))

Native ad and tracker blocking (candidate engine: adblock-rust) with standard filter lists, cosmetic filtering and per-site toggles.

- **Problem:** Ads and trackers slow pages, leak data and enable malvertising; extension blockers are limited under Manifest V3.
- **Use case:** A user opens a news site and sees no ads or trackers, with a one-click toggle if the site breaks.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-005](core.md#core-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Opera, Vivaldi, Firefox (ETP)
- **Evidence:** Competitor precedent: Brave Shields; adblock-rust is MPL-2.0.
- **Acceptance criteria:**
  - Blocks EasyList/EasyPrivacy-class rules
  - Per-site disable
  - Measured page-load and memory impact
  - Filter list licenses tracked
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Filter lists carry their own licenses (some GPL or CC BY-SA) and update channels; blocking always causes some site breakage and sites may use anti-adblock measures.

<a id="shd-002"></a>

## SHD-002 — Pop-up blocking

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-SHD-01 (Native content blocking (Clean Web))

Chromium pop-up blocker plus stricter blocking of pop-unders and click-hijacking new windows.

- **Problem:** Abusive pop-unders and new-window redirects remain common on low-quality sites.
- **Use case:** A click on a streaming site does not spawn a hidden pop-under.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-001](#shd-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Pop-under test suite blocked
  - Per-site allow
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Distinguishing legitimate new windows (OAuth, payments) from pop-unders is heuristic; stricter blocking risks breaking login flows.

<a id="shd-003"></a>

## SHD-003 — Autoplay blocking

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-SHD-01 (Native content blocking (Clean Web))

Block audible and optionally all autoplay video by default with per-site exceptions.

- **Problem:** Autoplaying video wastes data, battery and attention.
- **Use case:** A user opens a news article; the video does not play until clicked.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-045](core.md#core-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Default blocks audible autoplay
  - Option to block all
  - Per-site exceptions
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Blocking all autoplay breaks some video-first sites and background previews; muted autoplay is allowed by default upstream and changing that has compatibility cost.

<a id="shd-004"></a>

## SHD-004 — Automated optional-cookie rejection

`Flagship` · `Research` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-01 (Native content blocking (Clean Web))

Automatically reject optional cookies in consent banners where reliable (CMP APIs, rules), otherwise hide banners conservatively.

- **Problem:** Consent banners waste time and nudge users into accepting tracking.
- **Use case:** A user visits a site and its consent banner is answered 'reject optional' automatically.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-001](#shd-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave (Cookiecrumbler), Firefox (cookie banner reduction), Consent-O-Matic
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Uses rejection, never blanket acceptance
  - Rule source and licenses documented
  - Breakage reporting per site
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Legal effect of automated rejection varies; reliability differs per CMP.

<a id="shd-005"></a>

## SHD-005 — Notification prompt blocking

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-SHD-01 (Native content blocking (Clean Web))

Quiet or block notification permission prompts by default, with explicit opt-in per site.

- **Problem:** Notification prompts are spammy and used for scams.
- **Use case:** A user is never interrupted by a notification prompt unless they opted to allow prompts for that site.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-045](core.md#core-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Quiet UI default
  - Abusive-site handling
  - Per-site allow
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Blocking prompts may hide notifications users actually want (chat, calendar); per-site opt-in must be easy to find.

<a id="shd-006"></a>

## SHD-006 — Fingerprinting protection

`Flagship` · `Research` · **P1** · Impact High · Complexity L · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-01 (Native content blocking (Clean Web))

Reduce fingerprinting surface (farbling/randomization or normalization of high-entropy APIs) while preserving compatibility.

- **Problem:** Fingerprinting tracks users without cookies.
- **Use case:** A tracker script cannot obtain a stable canvas/WebGL/audio fingerprint across sites.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-001](#shd-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — patches deep in Blink increase rebase cost.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox (resistFingerprinting), Tor Browser, Safari
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Measured with public fingerprinting test suites
  - Compatibility regressions tracked
  - Strict mode optional
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Patches in Blink are expensive to maintain; start with low-risk APIs.

<a id="shd-007"></a>

## SHD-007 — Tracking parameter stripping

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-SHD-01 (Native content blocking (Clean Web))

Remove known tracking parameters (utm_*, fbclid, gclid, etc.) from navigations and copied links.

- **Problem:** Shared links carry tracking identifiers.
- **Use case:** A user copies a link and the fbclid parameter is removed.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-001](#shd-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Curated list with update channel
  - Copy link clean
  - Per-site exceptions
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Parameter lists need maintenance; stripping can break links that misuse tracking-like parameters for function (e.g. affiliate or campaign landing pages).

<a id="shd-008"></a>

## SHD-008 — Malicious redirect protection

`Secondary` · `Planned` · **P2** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

Block or confirm suspicious redirect chains, bounce tracking and redirect-based malvertising.

- **Problem:** Redirect chains send users to scams or track them.
- **Use case:** Clicking a shortened link that bounces through five trackers lands directly or asks first.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-001](#shd-001), [SHD-016](#shd-016)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Known bounce trackers debounced
  - Suspicious chains interstitial
  - Logs visible in Link Inspector
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Some legitimate flows (SSO, payment 3-D Secure) are redirect chains; aggressive interstitials would break them, so only known bounce trackers are debounced by default.

<a id="shd-009"></a>

## SHD-009 — Smart Back

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

Protect the Back button from history manipulation (history stuffing, back-button hijacking).

- **Problem:** Some sites trap users by inserting fake history entries.
- **Use case:** Pressing Back on a spammy site actually leaves the site.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Chromium has partial history manipulation intervention; Brumel extends it (to be verified).
- **Acceptance criteria:**
  - Skips entries created without user activation
  - Long-press shows real history
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Distinguishing manipulative history entries from legitimate single-page-app navigation is heuristic; upstream interventions already exist and must not be duplicated inconsistently.

<a id="shd-010"></a>

## SHD-010 — Self Repair

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

When a page breaks, guided diagnosis that toggles blocking, extensions, fingerprinting protection and identity to find the cause.

- **Problem:** Privacy features break sites and users do not know which one.
- **Use case:** A checkout page fails; Self Repair finds fingerprinting protection caused it and offers a site exception.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-001](#shd-001), [SHD-006](#shd-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Step-by-step bisect with user consent
  - Report breakage optionally (anonymized)
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Automated bisecting can only test Brumel-side factors (blocking, extensions, protections); site bugs or server issues will still look like breakage.

<a id="shd-011"></a>

## SHD-011 — Permission Timeline

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-02 (Permissions and extension control)

History of when each site used camera, microphone, location, clipboard, notifications and other permissions.

- **Problem:** Users cannot audit which sites actually used sensitive permissions.
- **Use case:** A user sees a site accessed location at 3 a.m. and revokes it.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-045](core.md#core-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Local log with retention
  - Revoke from timeline
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Chromium does not log every permission use (e.g. continuous location watching) at fine granularity; the timeline may show grants and use sessions rather than each access.

<a id="shd-012"></a>

## SHD-012 — One-Time Permissions

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-02 (Permissions and extension control)

Grant permissions only for the current visit or a limited time.

- **Problem:** Permanent grants accumulate for sites used once.
- **Use case:** A user allows camera for one video call; it is revoked when the tab closes.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-045](core.md#core-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Chrome (one-time permissions), Firefox, Safari
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Allow once / for N hours
  - Default for sensitive permissions configurable
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Chromium already supports one-time grants for some permissions; extending to all permission types requires patching permission UI code that changes often upstream.

<a id="shd-013"></a>

## SHD-013 — Extension Firewall

`Flagship` · `Planned` · **P1** · Impact High · Complexity L · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-02 (Permissions and extension control)

Control which sites, network destinations and APIs each extension can access, beyond the standard permission model.

- **Problem:** Extensions often request access to all sites and can exfiltrate data.
- **Use case:** A user restricts an extension to two sites and blocks its access to a tracking endpoint.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-022](core.md#core-022), [SHD-034](#shd-034)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — must be enforced in the browser/network service, not in the renderer.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Per-extension site and network rules
  - Blocked requests visible
  - No extension can bypass via the browser process
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Extensions with debugger, proxy or native-messaging permissions can bypass site restrictions; Extension Firewall reduces but cannot eliminate extension risk.

<a id="shd-014"></a>

## SHD-014 — Privacy Receipt

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-03 (Transparency: Glass Box, Privacy Receipt and telemetry)

Per-site and periodic summary of what was blocked, which permissions were used and which connections the browser made.

- **Problem:** Privacy protection is invisible, so users cannot judge it.
- **Use case:** A user sees that a recipe site attempted 37 tracker requests, all blocked.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-001](#shd-001), [SHD-034](#shd-034)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Numbers are actual counts, not estimates
  - Local only
  - No gamified exaggeration
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Counts reflect what Brumel blocked or observed; they say nothing about data collected server-side or through first-party tracking that was not blocked.

<a id="shd-015"></a>

## SHD-015 — Smart Cleanup

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

Selective clearing of cookies/storage/cache while keeping chosen logins and sessions.

- **Problem:** 'Clear browsing data' forces users to choose between privacy and staying logged in.
- **Use case:** A user clears all site data except their email and bank sessions.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-030](core.md#core-030), [MEM-020](memory.md#mem-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Keep-list for sites
  - Preview before clearing
  - Universal Undo where possible
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Keeping some sites' cookies while deleting others can leave cross-site state through first-party partitions; results must be explained, not promised as 'clean'.

<a id="shd-016"></a>

## SHD-016 — Link Inspector

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

Show the real destination, redirect chain and known reputation of a link before opening.

- **Problem:** Shortened and disguised links hide scams.
- **Use case:** A user hovers a shortened link and sees it resolves to a lookalike banking domain.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-050](core.md#core-050)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Resolution happens only on user request (avoids pinging trackers)
  - Punycode/lookalike warnings
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Resolving redirects requires visiting intermediate URLs, which may itself track the user or trigger actions; resolution is on request only.

<a id="shd-017"></a>

## SHD-017 — Clipboard Guard

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-04 (Local data, credential and session protection)

Notify or block when pages read or overwrite the clipboard, especially crypto addresses and code-paste attacks.

- **Problem:** Malicious pages hijack the clipboard (e.g. swapping wallet addresses or 'paste this command' scams).
- **Use case:** A page tries to replace the copied text with a terminal command and Brumel warns.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-045](core.md#core-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Low — mitigation.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Clipboard writes without user gesture blocked or flagged
  - Command-paste scam warning
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Detecting malicious clipboard writes is heuristic; legitimate 'copy' buttons write without explicit selection and must keep working.

<a id="shd-018"></a>

## SHD-018 — Settings Lock

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-ENG-04 (Diagnostics: resource monitor, Browser Health and benchmark)

Tracked together with ENG-016 (Update Guard).

- **Problem:** Browser updates sometimes reset settings or re-enable features users turned off.
- **Use case:** Preserve user preferences after updates and against extension changes.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-016](engine.md#eng-016)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of ENG-016
  - Use case verified: Preserve user preferences after updates and against extension changes.
- **Origin:** D · **Duplicate of:** [ENG-016](engine.md#eng-016)
- **Limitations / notes:** Technical duplicate merged into ENG-016; kept as its own entry to preserve the use case and traceability.

<a id="shd-019"></a>

## SHD-019 — Biometric lock

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Trust · Epic EP-SHD-04 (Local data, credential and session protection)

Lock the browser, private spaces or password reveal behind OS authentication (Windows Hello, polkit/PAM).

- **Problem:** Shared or unattended computers expose browser data.
- **Use case:** A user requires Windows Hello to reveal saved passwords and open the Finance space.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-023](core.md#core-023)
- **Platforms:** Windows Planned · Linux Research · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Uses OS APIs only
  - No biometric data handled by Brumel
  - Timeout policies
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Windows Hello and PAM/polkit offer different guarantees; on Linux biometric support depends on distribution setup and may be unavailable.

<a id="shd-020"></a>

## SHD-020 — Local data encryption

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-SHD-04 (Local data, credential and session protection)

Encrypt sensitive Brumel Store data at rest using OS-protected keys (OSCrypt) and optional user passphrase.

- **Problem:** Profile files can be copied by malware or other users.
- **Use case:** Copying a profile folder to another machine does not reveal archived tabs or drafts.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Sensitive tables encrypted
  - Key handling documented in threat model
  - Performance overhead measured
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Encryption at rest cannot protect against malware running as the same user.

<a id="shd-021"></a>

## SHD-021 — End-to-end encrypted sync

`Essential` · `Research` · **P0** · Impact Critical · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Tracked together with CON-020 (Client-side E2EE layer).

- **Problem:** Server breaches or operators should never expose synced data.
- **Use case:** Sync protected so the server cannot read user data.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-020](connect.md#con-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** Critical.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Covered by the acceptance criteria of CON-020
  - Use case verified: Sync protected so the server cannot read user data.
- **Origin:** D · **Duplicate of:** [CON-020](connect.md#con-020)
- **Limitations / notes:** Technical duplicate merged into CON-020; kept as its own entry to preserve the use case and traceability.

<a id="shd-022"></a>

## SHD-022 — Credential protection

`Essential` · `Planned` · **P1** · Impact Critical · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-04 (Local data, credential and session protection)

Harden the password store: reauthentication for reveal/export, breach checks via privacy-preserving k-anonymity, phishing-resistant autofill.

- **Problem:** Stored passwords are the most valuable data in a browser.
- **Use case:** A user is warned when a saved password appears in a known breach, without sending the password anywhere.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-023](core.md#core-023), [SHD-019](#shd-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — breach-check proxy or third-party service (licensing to verify).
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Breach checks use k-anonymity
  - Autofill only on exact origin match
  - Reveal requires OS auth
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Breach-check services have their own terms and availability; reauthentication relies on OS facilities that may be weak or absent on some systems.

<a id="shd-023"></a>

## SHD-023 — DNS over HTTPS (Shield)

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-06 (Security baseline: sandbox, site isolation, HTTPS and DNS)

Tracked together with CORE-046 (Secure DNS (DNS over HTTPS)).

- **Problem:** Plain DNS leaks browsing to the network.
- **Use case:** Encrypted DNS presented as part of Shield settings.
- **Segments:** All users
- **Dependencies:** [CORE-046](core.md#core-046)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of CORE-046
  - Use case verified: Encrypted DNS presented as part of Shield settings.
- **Origin:** D · **Duplicate of:** [CORE-046](core.md#core-046)
- **Limitations / notes:** Technical duplicate merged into CORE-046; kept as its own entry to preserve the use case and traceability.

<a id="shd-024"></a>

## SHD-024 — HTTPS-only mode (Shield)

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 1 (Technical Foundation) · Pillar Foundation · Epic EP-CORE-06 (Security baseline: sandbox, site isolation, HTTPS and DNS)

Tracked together with CORE-047 (HTTPS-First / HTTPS-Only).

- **Problem:** HTTP connections can be intercepted.
- **Use case:** Force HTTPS everywhere from Shield settings.
- **Segments:** All users
- **Dependencies:** [CORE-047](core.md#core-047)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of CORE-047
  - Use case verified: Force HTTPS everywhere from Shield settings.
- **Origin:** D · **Duplicate of:** [CORE-047](core.md#core-047)
- **Limitations / notes:** Technical duplicate merged into CORE-047; kept as its own entry to preserve the use case and traceability.

<a id="shd-025"></a>

## SHD-025 — Session isolation

`Flagship` · `Planned` · **P1** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-02 (Workspaces, identities and routing)

Tracked together with WRK-010 (Multi Identity).

- **Problem:** Using two accounts of the same site requires separate profiles or windows.
- **Use case:** Isolate sessions/cookies between identities.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-010](workspace.md#wrk-010)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Medium — partitioning must not leak across identities.
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Firefox (Containers), Vivaldi, Arc
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of WRK-010
  - Use case verified: Isolate sessions/cookies between identities.
- **Origin:** D · **Duplicate of:** [WRK-010](workspace.md#wrk-010)
- **Limitations / notes:** Technical duplicate merged into WRK-010; kept as its own entry to preserve the use case and traceability.

<a id="shd-026"></a>

## SHD-026 — Phishing protection (Shield)

`Essential` · `Planned` · **P0** · Impact Critical · Complexity M · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-05 (Google-service replacements, DRM, codecs and Cast)

Tracked together with CORE-050 (Phishing and malware protection).

- **Problem:** Phishing is one of the most common ways users are harmed.
- **Use case:** Phishing warnings presented within Shield.
- **Segments:** All users
- **Dependencies:** [CORE-050](core.md#core-050)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of CORE-050
  - Use case verified: Phishing warnings presented within Shield.
- **Origin:** D · **Duplicate of:** [CORE-050](core.md#core-050)
- **Limitations / notes:** Technical duplicate merged into CORE-050; kept as its own entry to preserve the use case and traceability.

<a id="shd-027"></a>

## SHD-027 — Optional, auditable telemetry

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-03 (Transparency: Glass Box, Privacy Receipt and telemetry)

Telemetry is off by default; if a user opts in, every metric is documented, aggregated, visible locally before sending and open source server-side.

- **Problem:** Users cannot verify what browsers report about them.
- **Use case:** A user opts in and can see each report's exact payload before it is sent.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-034](#shd-034)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — collection endpoint.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Medium — even aggregated metrics need minimization.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Off by default
  - Public metric dictionary
  - Local viewer of pending payloads
  - No unique long-lived IDs
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Even minimal, aggregated metrics can be sensitive in small populations; with few opt-in users, data may be too sparse to be useful.

<a id="shd-028"></a>

## SHD-028 — Advanced private mode

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

Private windows with stricter defaults: fingerprinting strict mode, no extensions, aggressive storage partitioning, optional proxy.

- **Problem:** Standard incognito only prevents local history, which users misunderstand.
- **Use case:** A journalist opens an advanced private window with stricter protections and clear limits explained.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-027](core.md#core-027), [SHD-006](#shd-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Clear explanation of what is and is not protected
  - No claims of anonymity
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Chromium-based private windows cannot match Tor Browser's anonymity; a proxy or VPN changes the IP but not fingerprinting surface.

<a id="shd-029"></a>

## SHD-029 — Tor integration

`Deferred` · `Deferred` · **P3** · Impact Medium · Complexity XL · Phase 6 (Future) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

Optional Tor-routed private windows, as long-term research.

- **Problem:** Some users need network-level anonymity.
- **Use case:** A user opens a Tor window for an onion service.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-028](#shd-028)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** High — Chromium-based Tor windows leak more fingerprinting surface than Tor Browser.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave (Tor windows), Tor Browser
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Not before a dedicated threat model
  - Never claims equivalence with Tor Browser
- **Origin:** D · **Duplicate of:** —
- **Limitations / notes:** Deferred: high risk of giving users a false sense of anonymity.

<a id="shd-030"></a>

## SHD-030 — Dark Pattern Radar

`Experimental` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

Rule-based detection of likely manipulative patterns (fake countdowns, pre-checked add-ons, hidden costs) with cautious, explainable warnings.

- **Problem:** Manipulative design costs users money and consent.
- **Use case:** At checkout, Brumel flags that a paid insurance add-on was pre-selected.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-001](#shd-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Deterministic-first · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Warnings are hedged ('possible') and explain the rule
  - Low false-positive rate measured on test set
  - No AI-only verdicts
- **Origin:** R52-16 · **Duplicate of:** —
- **Limitations / notes:** High false-positive risk; legal care needed when naming sites.

<a id="shd-031"></a>

## SHD-031 — User Rights

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Clean Web · Epic EP-SHD-01 (Native content blocking (Clean Web))

Restore copy, paste, text selection, right-click and keyboard shortcuts blocked by pages, with per-site exceptions.

- **Problem:** Sites block pasting into password fields or copying text, harming usability and security.
- **Use case:** A user pastes a generated password into a field that blocked paste.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Per-site toggle
  - Exceptions for web apps that need key capture (games, remote desktops)
- **Origin:** R52-20 · **Duplicate of:** —
- **Limitations / notes:** Some web apps legitimately capture keys or block copy (games, remote desktops, exam tools); overriding globally breaks them, so it is per-site.

<a id="shd-032"></a>

## SHD-032 — Guaranteed Exit

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Clean Web · Epic EP-SHD-01 (Native content blocking (Clean Web))

Reserved browser gesture/shortcut that pages cannot intercept to close or leave locking pages (fullscreen scams, dialog loops).

- **Problem:** Tech-support scams trap users in fullscreen pages with dialog loops.
- **Use case:** A user presses the reserved shortcut and the scam page closes immediately.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Shortcut cannot be captured by pages
  - Documented and discoverable
  - Works in fullscreen
- **Origin:** R52-24 · **Duplicate of:** —
- **Limitations / notes:** The reserved shortcut must be learnable by the users most at risk of scams, who are the least likely to know it; OS-level fullscreen tricks may still confuse users.

<a id="shd-033"></a>

## SHD-033 — Screen Share Shield

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Trust · Epic EP-SHD-04 (Local data, credential and session protection)

Hide sensitive browser UI and marked content (passwords, notifications, other tabs) during screen sharing where technically possible.

- **Problem:** Screen sharing leaks notifications, tabs and personal data.
- **Use case:** During a meeting, a user's notifications and other tabs are hidden from the shared screen.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Applies when Brumel captures (getDisplayMedia)
  - OS-level capture limits documented
- **Origin:** R52-37 · **Duplicate of:** —
- **Limitations / notes:** Cannot protect against OS-level capture by other apps.

<a id="shd-034"></a>

## SHD-034 — Glass Box

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-03 (Transparency: Glass Box, Privacy Receipt and telemetry)

Transparent log of every network connection the browser itself initiates (updates, components, filter lists, sync), separate from page traffic.

- **Problem:** Users cannot verify browsers' 'no phoning home' claims.
- **Use case:** A user opens Glass Box after first run and sees every background request with purpose and destination.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-006](core.md#core-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Project principle; similar to Chromium's net-export but user-facing.
- **Acceptance criteria:**
  - Every browser-initiated request is tagged with a purpose
  - Unknown requests flagged as bugs
  - Exportable log
- **Origin:** R52-34 · **Duplicate of:** —
- **Limitations / notes:** Network requests made by the OS, extensions or third-party software on the user's behalf are outside its scope; it logs what Brumel's browser process initiates.

<a id="shd-035"></a>

## SHD-035 — Extension Passport

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-SHD-02 (Permissions and extension control)

Track extension identity changes: new permissions, ownership/publisher changes, sudden behavior changes; pause updates pending user approval.

- **Problem:** Popular extensions get sold and turned into malware through silent updates.
- **Use case:** An extension update adds 'read all sites' and a new publisher; Brumel pauses it and asks the user.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-022](core.md#core-022)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Permission diffs shown on update
  - Publisher change detection where data exists
  - User approval to re-enable
- **Origin:** R52-42 · **Duplicate of:** —
- **Limitations / notes:** Chrome Web Store publisher data availability is limited; partially heuristic.

<a id="shd-036"></a>

## SHD-036 — Credential Sentinel

`Experimental` · `Research` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Trust · Epic EP-SHD-04 (Local data, credential and session protection)

Warn when a saved credential is about to be submitted to a domain other than where it was saved (phishing, lookalikes).

- **Problem:** Users type their passwords into phishing sites that look identical.
- **Use case:** Typing the bank password into a lookalike domain triggers a warning.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-022](#shd-022)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — must not leak password hashes.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Chrome (password protection, Google-only), Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Detection without storing plaintext beyond the password manager
  - Low false positives on SSO flows
- **Origin:** R52-43 · **Duplicate of:** —
- **Limitations / notes:** Legitimate cross-domain credential use (SSO, shared logins across country domains) causes false positives; detection must be tuned with real flows.

<a id="shd-037"></a>

## SHD-037 — Agent Clean Room

`Deferred` · `Research` · **P3** · Impact High · Complexity XL · Phase 6 (Future) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

Capability-based isolation architecture for any future agent/automation: least-privilege grants, confirmation for side effects, isolated profiles, audit logs.

- **Problem:** AI agents acting in a browser are vulnerable to prompt injection from web content.
- **Use case:** A future agent may fill a form only in a sandboxed identity, with every submit confirmed by the user.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [SHD-013](#shd-013), [NANO-007](nano.md#nano-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** High — the gate for DEV-012, DEV-013 and NANO-029 alternatives.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Threat model reviewed before any agent ships
  - Web content never grants capabilities
  - All actions logged and reversible where possible
- **Origin:** R52-44 · **Duplicate of:** —
- **Limitations / notes:** Research only; no agents are enabled without it.

<a id="shd-038"></a>

## SHD-038 — Verified Downloads

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Trust · Epic EP-SHD-05 (Web safety tools and advanced privacy)

Compare downloaded installers against publisher-provided hashes, signatures or manifests where available.

- **Problem:** Users download tampered installers from mirrors and fake sites.
- **Use case:** Downloading a popular open-source installer shows 'matches the official SHA-256 from the project's site'.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-031](core.md#core-031)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — optional curated manifest index.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Only claims verification when a trusted source exists
  - Shows signature status on Windows
- **Origin:** R52-45 · **Duplicate of:** —
- **Limitations / notes:** Most publishers do not offer machine-readable hashes; verification will only be possible for a minority of downloads and must never imply safety otherwise.

<a id="shd-039"></a>

## SHD-039 — Hardened Sessions

`Experimental` · `Research` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Trust · Epic EP-SHD-04 (Local data, credential and session protection)

Bind session cookies to the device (Device Bound Session Credentials, TPM-backed where available) to reduce cookie theft.

- **Problem:** Infostealer malware steals session cookies to bypass passwords and 2FA.
- **Use case:** A stolen cookie from a DBSC-enabled site cannot be replayed on another machine.
- **Segments:** Privacy-conscious users, Everyday users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — native implementations should reduce page work; must be measured. · **Infrastructure cost:** Low — filter list and metadata hosting/mirroring.
- **Security risk:** Medium — runs on untrusted web content; parsers must be memory-safe or sandboxed.
- **Privacy risk:** Low — designed to reduce data exposure.
- **Competitors / precedents:** Brave, Firefox, Safari, Vivaldi, Edge
- **Evidence:** Competitor precedent: Brave Shields, Firefox ETP, Safari ITP.
- **Acceptance criteria:**
  - Follows the DBSC standard as implemented upstream
  - Documented site support
- **Origin:** R52-47 · **Duplicate of:** —
- **Limitations / notes:** Requires site adoption and upstream support; Brumel follows upstream rather than inventing a protocol.
