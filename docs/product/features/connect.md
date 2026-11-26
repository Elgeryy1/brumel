<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Connect — continuity between devices

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

28 entries. Epics in this module:

- **EP-CON-01** E2EE sync core and infrastructure — phase 4 (Public Beta), P1
- **EP-CON-02** Synced data types — phase 4 (Public Beta), P1
- **EP-CON-03** Device mesh, sharing and pairing — phase 4 (Public Beta), P2

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [CON-001](#con-001) | Smart Continuity | Flagship | Research | P1 | 4 |
| [CON-002](#con-002) | Device Mesh | Experimental | Research | P2 | 4 |
| [CON-003](#con-003) | Quick Share | Secondary | Research | P2 | 4 |
| [CON-004](#con-004) | Send tab to device | Essential | Research | P1 | 4 |
| [CON-005](#con-005) | Bookmark sync | Essential | Research | P1 | 4 |
| [CON-006](#con-006) | Workspace sync | Flagship | Research | P1 | 4 |
| [CON-007](#con-007) | Preferences sync | Essential | Research | P2 | 4 |
| [CON-008](#con-008) | Rules sync | Secondary | Research | P2 | 4 |
| [CON-009](#con-009) | Optional history sync | Secondary | Research | P2 | 4 |
| [CON-010](#con-010) | Optional extension sync | Secondary | Research | P3 | 4 |
| [CON-011](#con-011) | Clipboard sync | Experimental | Research | P3 | 4 |
| [CON-012](#con-012) | Reading continuity | Secondary | Research | P3 | 4 |
| [CON-013](#con-013) | QR pairing | Essential | Research | P1 | 4 |
| [CON-014](#con-014) | Incremental sync | Essential | Research | P1 | 4 |
| [CON-015](#con-015) | Conflict management | Essential | Research | P1 | 4 |
| [CON-016](#con-016) | Offline operation | Essential | Research | P0 | 4 |
| [CON-017](#con-017) | Encrypted backups (remote) | Secondary | Research | P2 | 4 |
| [CON-018](#con-018) | Self-hosting | Flagship | Research | P1 | 4 |
| [CON-019](#con-019) | Password sync | Deferred | Deferred | P2 | 5 |
| [CON-020](#con-020) | Client-side E2EE layer | Essential | Research | P0 | 4 |
| [CON-021](#con-021) | Hosted relay candidate (Supabase Free / PostgreSQL) | Experimental | Research | P2 | 4 |
| [CON-022](#con-022) | WebRTC transport | Experimental | Research | P2 | 4 |
| [CON-023](#con-023) | Encrypted blob relay | Essential | Research | P1 | 4 |
| [CON-024](#con-024) | Docker self-hosted server *(→ CON-018)* | Flagship | Research | P1 | 4 |
| [CON-025](#con-025) | No-account local mode guarantee | Essential | Planned | P0 | 2 |
| [CON-026](#con-026) | Mobile Upload | Secondary | Research | P2 | 4 |
| [CON-027](#con-027) | Pocket Profile | Experimental | Research | P3 | 6 |
| [CON-028](#con-028) | Trusted Remote Help | Experimental | Research | P3 | 6 |

<a id="con-001"></a>

## CON-001 — Smart Continuity

`Flagship` · `Research` · **P1** · Impact High · Complexity XL · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Optional, end-to-end encrypted multi-device sync of Brumel data with local-first operation.

- **Problem:** Users want continuity without giving a company readable access to their data.
- **Use case:** A user opens their laptop and finds the workspaces they organized on their desktop.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-020](#con-020), [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - E2EE by design (CON-020)
  - Works offline and syncs later
  - Browser fully functional without sync or account
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** E2EE prevents server-side features (web access to data, server-side search, account recovery without key); losing all devices and the recovery key loses data.

<a id="con-002"></a>

## CON-002 — Device Mesh

`Experimental` · `Research` · **P2** · Impact Medium · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-03 (Device mesh, sharing and pairing)

Direct device-to-device sync over WebRTC/LAN when devices can reach each other, relay as fallback.

- **Problem:** Routing all sync through a server adds cost and metadata exposure.
- **Use case:** Two devices on the same network sync directly without the relay.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-022](#con-022), [CON-013](#con-013)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Mutual authentication of paired devices
  - NAT traversal documented
  - Relay fallback
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Direct connections fail behind symmetric NAT and corporate networks; local discovery (mDNS) can be blocked or raise privacy concerns.

<a id="con-003"></a>

## CON-003 — Quick Share

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-03 (Device mesh, sharing and pairing)

Send links, text and small files between paired devices, encrypted.

- **Problem:** Users email themselves links and files.
- **Use case:** A user sends a PDF from desktop to laptop in two clicks.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-002](#con-002), [CON-023](#con-023)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - E2EE
  - Size limits documented
  - Works via mesh or relay
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** File size is limited by relay capacity and cost; both devices may need to be online at the same time for mesh transfers.

<a id="con-004"></a>

## CON-004 — Send tab to device

`Essential` · `Research` · **P1** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-03 (Device mesh, sharing and pairing)

Send the current tab to another paired device.

- **Problem:** Moving a page between devices is clumsy.
- **Use case:** A user sends a recipe tab to their laptop in the kitchen.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-001](#con-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - E2EE
  - Notification on target
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Requires paired devices with Brumel installed; Android/iOS targets are not available until mobile clients exist.

<a id="con-005"></a>

## CON-005 — Bookmark sync

`Essential` · `Research` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-02 (Synced data types)

E2EE sync of bookmarks.

- **Problem:** Bookmarks differ across devices.
- **Use case:** A bookmark added on desktop appears on laptop.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-001](#con-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Conflict-safe merge
  - E2EE
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Bookmark merge semantics (order, folders, duplicates) are tricky; import from other browsers before first sync can create duplicates.

<a id="con-006"></a>

## CON-006 — Workspace sync

`Flagship` · `Research` · **P1** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-02 (Synced data types)

E2EE sync of workspaces, folders and tab lists.

- **Problem:** Workspace organization is lost when switching devices.
- **Use case:** A user continues the 'Thesis' workspace on another device.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-001](#con-001), [WRK-004](workspace.md#wrk-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Unloaded tabs sync as metadata only
  - Conflict handling (CON-015)
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Workspace data references tabs and identities that may not exist on the other device; heavy workspaces mean larger sync payloads.

<a id="con-007"></a>

## CON-007 — Preferences sync

`Essential` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-02 (Synced data types)

E2EE sync of selected settings with device-specific exclusions.

- **Problem:** Reconfiguring each device is tedious.
- **Use case:** A user's Shield settings apply on all devices.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-001](#con-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Per-setting sync scope
  - Device-specific settings excluded
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Many settings are device-specific (GPU, paths, display); syncing the wrong ones causes problems, so scopes must be curated.

<a id="con-008"></a>

## CON-008 — Rules sync

`Secondary` · `Research` · **P2** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-02 (Synced data types)

E2EE sync of routing, profile and download rules.

- **Problem:** Rules must be recreated per device.
- **Use case:** Smart Router rules apply on both computers.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-001](#con-001), [WRK-030](workspace.md#wrk-030)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Rules versioned
  - Conflicts shown
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Rules may reference device-specific paths or identities; conflicting rule edits need manual resolution.

<a id="con-009"></a>

## CON-009 — Optional history sync

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-02 (Synced data types)

Opt-in E2EE history sync with retention limits.

- **Problem:** History search fails on another device.
- **Use case:** A user finds on laptop a page visited on desktop.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-001](#con-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** High — history is sensitive; opt-in.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Off by default
  - Retention configurable
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** History is high-volume and highly sensitive; syncing it increases metadata exposure (sizes, timing) even with E2EE.

<a id="con-010"></a>

## CON-010 — Optional extension sync

`Secondary` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-02 (Synced data types)

Sync the list of installed compatible extensions (not their data).

- **Problem:** Reinstalling extensions per device is tedious.
- **Use case:** A new device offers to install the same extensions.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-001](#con-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Install requires confirmation per device
  - Extension data not synced
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Extension data and settings are not synced, so extensions need reconfiguration; extension availability can differ by platform.

<a id="con-011"></a>

## CON-011 — Clipboard sync

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-03 (Device mesh, sharing and pairing)

Explicit, authorized clipboard sharing between paired devices.

- **Problem:** Copying between devices requires workarounds.
- **Use case:** A user copies a code on phone and pastes it on desktop.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-003](#con-003)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** High — clipboard often contains secrets.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Explicit per-use action or time-limited authorization
  - E2EE
  - No background clipboard reading
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Clipboards frequently contain passwords and codes; even authorized sync risks leaking secrets to a compromised paired device.

<a id="con-012"></a>

## CON-012 — Reading continuity

`Secondary` · `Research` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-02 (Synced data types)

Sync reading position for queued articles.

- **Problem:** Users lose their place across devices.
- **Use case:** A user continues an article at the same paragraph on another device.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-001](#con-001), [MEM-009](memory.md#mem-009)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Position sync for Reading Queue items
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Reading positions depend on identical page layout; different screen sizes and dynamic pages make positions approximate.

<a id="con-013"></a>

## CON-013 — QR pairing

`Essential` · `Research` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-03 (Device mesh, sharing and pairing)

Pair devices by scanning a QR code that carries a one-time key exchange.

- **Problem:** Typing sync codes is error-prone; account-based pairing requires trusting a server.
- **Use case:** A user pairs a laptop by scanning a QR from the desktop.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-020](#con-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Authenticated key exchange
  - Pairing revocable
  - No account required
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Requires a camera on one device or a manual code fallback; QR pairing in person is secure only if the screen is not observed.

<a id="con-014"></a>

## CON-014 — Incremental sync

`Essential` · `Research` · **P1** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Operation/delta-based sync instead of full snapshots.

- **Problem:** Full syncs waste bandwidth and battery.
- **Use case:** Changing one bookmark sends a small encrypted operation.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-020](#con-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Delta sizes measured
  - Resumable
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Operation logs grow and need compaction; schema changes across Brumel versions must stay backward compatible.

<a id="con-015"></a>

## CON-015 — Conflict management

`Essential` · `Research` · **P1** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Deterministic merge (CRDT or operation log) with visible conflict resolution where needed.

- **Problem:** Naive last-write-wins loses data.
- **Use case:** Two devices edit the same workspace offline and both changes survive.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-014](#con-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Merge rules documented per data type
  - Property tests
  - No silent loss
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Some conflicts have no correct automatic answer (concurrent renames); CRDTs add storage overhead and complexity.

<a id="con-016"></a>

## CON-016 — Offline operation

`Essential` · `Research` · **P0** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

All synced features work offline; sync is eventual.

- **Problem:** Cloud-first sync breaks without connectivity.
- **Use case:** A user organizes tabs on a plane; changes sync on landing.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-014](#con-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - No feature requires connectivity to work locally
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Long offline periods increase conflict likelihood and payload sizes on reconnect.

<a id="con-017"></a>

## CON-017 — Encrypted backups (remote)

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Optional E2EE backup snapshots stored on the relay or a user-chosen storage.

- **Problem:** Device loss without backup loses everything.
- **Use case:** A user restores to a new device using their recovery key.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-020](#con-020), [MEM-011](memory.md#mem-011)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Recovery key flow tested
  - Server cannot decrypt
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Remote backups depend on the relay's storage quota and availability; recovery-key loss means no recovery.

<a id="con-018"></a>

## CON-018 — Self-hosting

`Flagship` · `Research` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Official self-hostable sync server (Docker) and documented protocol.

- **Problem:** Users should not depend on the project's servers.
- **Use case:** A self-hoster runs the sync server on their own machine.
- **Segments:** Self-hosters
- **Dependencies:** [CON-023](#con-023)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** None for the project; user-provided.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Docker image and docs
  - Same protocol as hosted relay
  - No dependency on the maintainer's personal infrastructure
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Self-hosters must maintain security updates of their server; the project cannot support every deployment environment.

<a id="con-019"></a>

## CON-019 — Password sync

`Deferred` · `Deferred` · **P2** · Impact High · Complexity L · Phase 5 (Version 1.0) · Pillar Memory · Epic EP-CON-02 (Synced data types)

Sync of saved passwords and passkeys metadata, only after a dedicated security review.

- **Problem:** Users expect passwords on all devices, but a flawed design would expose the most sensitive data.
- **Use case:** A user's new laptop has their passwords after pairing.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-001](#con-001), [SHD-022](shield.md#shd-022)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** Critical.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Independent security review completed
  - Separate key hierarchy
  - Opt-in
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Deferred until a dedicated review; users can use dedicated password managers meanwhile.

<a id="con-020"></a>

## CON-020 — Client-side E2EE layer

`Essential` · `Research` · **P0** · Impact Critical · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Key hierarchy, encryption and authentication performed in clients; servers only store opaque ciphertext and minimal metadata.

- **Problem:** Server breaches or operators should never expose synced data.
- **Use case:** Even with full database access, a relay operator cannot read bookmarks.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CORE-005](core.md#core-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** Critical.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Uses audited primitives/libraries
  - Key rotation and device revocation
  - Threat model and external review before beta
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Cryptographic design errors are easy to make; external review is required before beta, and E2EE does not hide metadata such as timing and payload size.

<a id="con-021"></a>

## CON-021 — Hosted relay candidate (Supabase Free / PostgreSQL)

`Experimental` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Evaluate Supabase Free (PostgreSQL + storage) as the initial hosted relay for encrypted blobs, with exit plan.

- **Problem:** A small project needs low-cost hosting without lock-in.
- **Use case:** Early testers sync through a free-tier relay; data remains encrypted.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-020](#con-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Low initially; grows with users.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Free-tier limits documented
  - Migration path to self-hosted server
  - No plaintext stored
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Free tiers have quotas and terms that can change.

<a id="con-022"></a>

## CON-022 — WebRTC transport

`Experimental` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-03 (Device mesh, sharing and pairing)

WebRTC data channels for device mesh with STUN/TURN considerations.

- **Problem:** P2P needs NAT traversal.
- **Use case:** Two devices connect directly through NAT.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-020](#con-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Low/Medium — TURN servers if needed.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - TURN fallback cost documented
  - Data still E2EE at application level
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** TURN relays are needed for many networks and cost bandwidth; WebRTC adds a large, security-sensitive dependency already present in Chromium.

<a id="con-023"></a>

## CON-023 — Encrypted blob relay

`Essential` · `Research` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Minimal server API storing and forwarding encrypted blobs and ops.

- **Problem:** Complex servers increase attack surface and cost.
- **Use case:** The relay stores only ciphertext with sizes and timestamps.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-020](#con-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - API documented
  - Rate limited
  - Metadata minimized
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** A relay is a central service with operational cost and abuse potential (storage misuse); rate limits and quotas may frustrate heavy users.

<a id="con-024"></a>

## CON-024 — Docker self-hosted server

`Flagship` · `Research` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Tracked together with CON-018 (Self-hosting).

- **Problem:** Users should not depend on the project's servers.
- **Use case:** Run the sync server with Docker on personal infrastructure.
- **Segments:** Self-hosters
- **Dependencies:** [CON-018](#con-018)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** None for the project; user-provided.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Covered by the acceptance criteria of CON-018
  - Use case verified: Run the sync server with Docker on personal infrastructure.
- **Origin:** F · **Duplicate of:** [CON-018](#con-018)
- **Limitations / notes:** Technical duplicate merged into CON-018; kept as its own entry to preserve the use case and traceability.

<a id="con-025"></a>

## CON-025 — No-account local mode guarantee

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-CORE-03 (Module system and feature registry)

Brumel works completely with no account and no sync; Connect is never required.

- **Problem:** Many browsers push accounts for basic features.
- **Use case:** A user never creates an account and loses no core functionality.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CORE-005](core.md#core-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - No core feature gated behind an account
  - First run never requires sign-in
- **Origin:** F · **Duplicate of:** —
- **Limitations / notes:** Some optional features (sync, cloud AI, crash reporting) inherently need a service; the guarantee covers core features, not everything.

<a id="con-026"></a>

## CON-026 — Mobile Upload

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-CON-03 (Device mesh, sharing and pairing)

Upload a file from a phone to a desktop file picker by scanning a QR code, using a temporary E2EE channel and the phone's web browser.

- **Problem:** Moving a photo from phone to a desktop upload form is surprisingly hard.
- **Use case:** A user scans a QR on a desktop upload dialog and picks a photo from their phone.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-022](#con-022), [CON-023](#con-023)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Low — relay bandwidth.
- **Security risk:** High — key management and server compromise must not expose data.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - No app install required
  - One-time E2EE session
  - Expires automatically
- **Origin:** R52-40 · **Duplicate of:** —
- **Limitations / notes:** Requires both devices online and a relay or local connection; large videos will be slow or limited by relay size caps.

<a id="con-027"></a>

## CON-027 — Pocket Profile

`Experimental` · `Research` · **P3** · Impact Medium · Complexity L · Phase 6 (Future) · Pillar Memory · Epic EP-CON-01 (E2EE sync core and infrastructure)

Encrypted portable profile on a USB drive, subject to feasibility and security review.

- **Problem:** Users on shared or borrowed computers want their environment safely.
- **Use case:** A user runs Brumel with their encrypted profile from a USB drive and leaves no trace.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-020](#con-020), [SHD-020](shield.md#shd-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — host machines may be compromised.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - Encryption with passphrase
  - Clear limits on host trust (keyloggers)
  - Feasibility study first
- **Origin:** R52-32 · **Duplicate of:** —
- **Limitations / notes:** Moved to Future: depends on portable build and security review.

<a id="con-028"></a>

## CON-028 — Trusted Remote Help

`Experimental` · `Research` · **P3** · Impact Medium · Complexity L · Phase 6 (Future) · Pillar Trust · Epic EP-CON-03 (Device mesh, sharing and pairing)

Limited, consent-based visual assistance between paired devices/contacts (view-only tab sharing with pointer).

- **Problem:** Helping family members with browser problems requires risky remote-desktop tools.
- **Use case:** A user shows one tab view-only to a relative and both see the pointer.
- **Segments:** Multi-device users, Self-hosters, Privacy-conscious users
- **Dependencies:** [CON-002](#con-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — incremental sync, batched network activity. · **Infrastructure cost:** Medium — relay/storage costs grow with users; self-hosting must be possible.
- **Security risk:** High — social-engineering target; strict design required.
- **Privacy risk:** Medium — metadata (timing, sizes, device count) visible to relay even with E2EE.
- **Competitors / precedents:** Chrome, Firefox, Brave, Vivaldi, Edge
- **Evidence:** Competitor precedent: Firefox Sync and Brave Sync (E2EE designs).
- **Acceptance criteria:**
  - View-only by default
  - Per-session consent
  - Never exposes other tabs or passwords
- **Origin:** R52-46 · **Duplicate of:** —
- **Limitations / notes:** Remote help is a classic scam vector; even view-only sharing can expose sensitive data on the shared tab, so sessions need explicit, repeated consent.
