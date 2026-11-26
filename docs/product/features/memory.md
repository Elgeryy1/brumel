<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Memory — memory and recovery

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

30 entries. Epics in this module:

- **EP-MEM-01** Brumel Store and local index — phase 2 (Internal Alpha), P0
- **EP-MEM-02** Browser Time Machine, Zero Loss and data portability — phase 3 (Public Alpha), P1
- **EP-MEM-03** Draft, form and login protection — phase 3 (Public Alpha), P1
- **EP-MEM-04** Recall, vaults and page history — phase 3 (Public Alpha), P2

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [MEM-001](#mem-001) | Browser Time Machine | Flagship | Planned | P1 | 3 |
| [MEM-002](#mem-002) | Smart Memory | Flagship | Research | P2 | 4 |
| [MEM-003](#mem-003) | Offline Vault | Secondary | Planned | P2 | 4 |
| [MEM-004](#mem-004) | Draft Protection | Flagship | Planned | P1 | 3 |
| [MEM-005](#mem-005) | Download Vault | Secondary | Planned | P2 | 3 |
| [MEM-006](#mem-006) | Zero Loss | Flagship | Planned | P1 | 3 |
| [MEM-007](#mem-007) | Session and workspace history *(→ MEM-001)* | Flagship | Planned | P1 | 3 |
| [MEM-008](#mem-008) | Restore closed windows *(→ MEM-006)* | Flagship | Planned | P1 | 3 |
| [MEM-009](#mem-009) | Reading position recovery | Secondary | Planned | P2 | 3 |
| [MEM-010](#mem-010) | Media playback position recovery | Secondary | Research | P3 | 4 |
| [MEM-011](#mem-011) | Local backups | Essential | Planned | P1 | 3 |
| [MEM-012](#mem-012) | Settings history | Secondary | Planned | P2 | 3 |
| [MEM-013](#mem-013) | Non-destructive restore | Essential | Planned | P1 | 3 |
| [MEM-014](#mem-014) | Brumel Store and local index | Essential | Planned | P0 | 2 |
| [MEM-015](#mem-015) | Semantic and text search *(→ MEM-002)* | Flagship | Research | P2 | 4 |
| [MEM-016](#mem-016) | Memory export and import *(→ MEM-030)* | Essential | Planned | P1 | 3 |
| [MEM-017](#mem-017) | Configurable local activity journal | Experimental | Research | P3 | 4 |
| [MEM-018](#mem-018) | Incognito and sensitive-site exclusion | Essential | Planned | P0 | 2 |
| [MEM-019](#mem-019) | Resume Cards | Flagship | Research | P2 | 4 |
| [MEM-020](#mem-020) | Universal Undo | Flagship | Planned | P1 | 3 |
| [MEM-021](#mem-021) | Copy with Source | Secondary | Planned | P2 | 3 |
| [MEM-022](#mem-022) | Page Change History | Secondary | Research | P3 | 4 |
| [MEM-023](#mem-023) | Page Watchers | Flagship | Research | P2 | 4 |
| [MEM-024](#mem-024) | Dead Link Recovery | Secondary | Research | P3 | 4 |
| [MEM-025](#mem-025) | Receipt Vault | Secondary | Research | P2 | 4 |
| [MEM-026](#mem-026) | Already Searched | Secondary | Research | P3 | 4 |
| [MEM-027](#mem-027) | Video Search | Experimental | Research | P3 | 4 |
| [MEM-028](#mem-028) | Session Guardian | Secondary | Research | P2 | 3 |
| [MEM-029](#mem-029) | Login Memory | Flagship | Planned | P2 | 3 |
| [MEM-030](#mem-030) | Exit Freedom | Essential | Planned | P1 | 3 |

<a id="mem-001"></a>

## MEM-001 — Browser Time Machine

`Flagship` · `Planned` · **P1** · Impact Critical · Complexity L · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Browse and restore earlier states of sessions, windows and workspaces from a local timeline.

- **Problem:** Users lose tab sets through accidental closes, bad merges or crashes and have no way back.
- **Use case:** A user restores the set of 25 tabs they had open last Tuesday afternoon.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-023](workspace.md#wrk-023), [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Snapshots at configurable intervals
  - Restore is non-destructive (MEM-013)
  - Storage cap and pruning
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Snapshots grow storage over time; restoring old states restores URLs, not the logged-in or server-side state of those pages.

<a id="mem-002"></a>

## MEM-002 — Smart Memory

`Flagship` · `Research` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Local semantic + full-text search over pages the user has visited and allowed to be indexed.

- **Problem:** Users remember what a page was about but not its title or URL.
- **Use case:** A user searches 'that article about heat pumps and subsidies' and finds it.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014), [NANO-004](nano.md#nano-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Optional · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — content index; encrypted, excludable and deletable.
- **Competitors / precedents:** Edge (verify), Rewind/Recall-style tools
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Index only authorized content (MEM-014, MEM-018)
  - Works offline
  - Hybrid search quality evaluated
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Semantic search needs page-content indexing and embeddings, with real storage, CPU and privacy cost; quality of small embedding models in Spanish and other languages must be proven.

<a id="mem-003"></a>

## MEM-003 — Offline Vault

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Save selected pages as self-contained offline copies (MHTML/WARC) with search.

- **Problem:** Pages disappear or change; users need reliable offline copies.
- **Use case:** A user saves a recipe page and opens it offline months later.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Saved copies open offline
  - Searchable
  - Export as standard format
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** MHTML/WARC snapshots fail on some dynamic, DRM-protected or heavily scripted pages; saved copies may contain personal data visible while logged in.

<a id="mem-004"></a>

## MEM-004 — Draft Protection

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-03 (Draft, form and login protection)

Locally preserve text typed into forms and editors so it can be recovered after crashes, accidental navigation or session expiry.

- **Problem:** Long form inputs are lost when a page reloads or a session expires.
- **Use case:** After a site logs the user out mid-submission, they recover the 800-word text.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — must not capture credentials.
- **Privacy risk:** High — form text is sensitive; strict exclusions required.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Excludes password and payment fields
  - Encrypted, short retention by default
  - Per-site opt-out
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Some editors (canvas-based, custom input) are invisible to standard form capture; storing typed text is inherently sensitive, so retention must be short.

<a id="mem-005"></a>

## MEM-005 — Download Vault

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Searchable record of downloads with source page, date and optional tags.

- **Problem:** Users cannot find which site a file came from or where it went.
- **Use case:** A user finds 'the PDF from the city council website' by searching its source.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [CORE-031](core.md#core-031), [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Search by name/source/date
  - Survives file moves where possible
  - Deletable
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** File moves and renames outside the browser break the link between record and file; search works on metadata, not file contents.

<a id="mem-006"></a>

## MEM-006 — Zero Loss

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Unified recovery center for closed tabs, windows, sessions, drafts and downloads.

- **Problem:** Recovery features are scattered across menus.
- **Use case:** A user opens Zero Loss and recovers a tab, a draft and a deleted workspace from one place.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-001](#mem-001), [MEM-004](#mem-004), [MEM-020](#mem-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Single entry point for all recovery types
  - Keyboard accessible
  - Explains what is recoverable
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Only aggregates what underlying features captured; it cannot recover something that was never recorded (e.g. with Memory disabled).

<a id="mem-007"></a>

## MEM-007 — Session and workspace history

`Flagship` · `Planned` · **P1** · Impact Critical · Complexity L · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Tracked together with MEM-001 (Browser Time Machine).

- **Problem:** Users lose tab sets through accidental closes, bad merges or crashes and have no way back.
- **Use case:** Timeline of how sessions and workspaces changed over time.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-001](#mem-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of MEM-001
  - Use case verified: Timeline of how sessions and workspaces changed over time.
- **Origin:** C · **Duplicate of:** [MEM-001](#mem-001)
- **Limitations / notes:** Technical duplicate merged into MEM-001; kept as its own entry to preserve the use case and traceability.

<a id="mem-008"></a>

## MEM-008 — Restore closed windows

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Tracked together with MEM-006 (Zero Loss).

- **Problem:** Recovery features are scattered across menus.
- **Use case:** Reopen recently closed windows (beyond Chromium's recent-closed list).
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-006](#mem-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of MEM-006
  - Use case verified: Reopen recently closed windows (beyond Chromium's recent-closed list).
- **Origin:** C · **Duplicate of:** [MEM-006](#mem-006)
- **Limitations / notes:** Technical duplicate merged into MEM-006; kept as its own entry to preserve the use case and traceability.

<a id="mem-009"></a>

## MEM-009 — Reading position recovery

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Remember scroll position in long pages and documents across sessions.

- **Problem:** Users lose their place in long articles and docs.
- **Use case:** A user reopens a long PDF and continues where they stopped.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Works for pages and PDF viewer
  - Excluded in incognito
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Scroll position is unreliable on pages that load content lazily or re-render; works best on static articles and PDFs.

<a id="mem-010"></a>

## MEM-010 — Media playback position recovery

`Secondary` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Remember playback position for HTML5 media where sites do not do it themselves.

- **Problem:** Long videos or podcasts restart from the beginning after a reload.
- **Use case:** A user reloads a lecture video and resumes at minute 42.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Opt-in per site
  - Does not conflict with site's own resume
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Many sites manage their own players; feasibility varies.

<a id="mem-011"></a>

## MEM-011 — Local backups

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Scheduled, encrypted local backups of profile data (bookmarks, settings, workspaces, Brumel Store) to a user-chosen folder.

- **Problem:** Profile corruption or disk failure wipes years of data.
- **Use case:** A user restores their full profile on a new computer from a backup file.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Encrypted with user passphrase
  - Restore tested in CI
  - Backup excludes caches
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Backups are only as safe as their storage location and passphrase; a forgotten passphrase makes backups unrecoverable by design.

<a id="mem-012"></a>

## MEM-012 — Settings history

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Versioned history of settings changes with diff and restore.

- **Problem:** Users do not know what changed after something stops working.
- **Use case:** A user sees that an extension changed their search engine yesterday and reverts it.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [ENG-016](engine.md#eng-016)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Change source recorded (user, extension, update, policy)
  - One-click revert
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Settings changed by enterprise policy or upstream migrations may not be attributable to a source.

<a id="mem-013"></a>

## MEM-013 — Non-destructive restore

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Restores merge into or alongside current state instead of overwriting it.

- **Problem:** Restoring a session or backup can destroy the current one.
- **Use case:** A user restores last week's session and their current tabs remain in a separate window.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-001](#mem-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Every restore is reversible
  - Current state snapshotted before restore
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Merging sessions can create duplicates; non-destructive restore favors safety over a clean result.

<a id="mem-014"></a>

## MEM-014 — Brumel Store and local index

`Essential` · `Planned` · **P0** · Impact Critical · Complexity L · Phase 2 (Internal Alpha) · Pillar Memory · Epic EP-MEM-01 (Brumel Store and local index)

Per-profile SQLite store with FTS5 for Brumel modules (archives, highlights, snapshots, metadata), encrypted keys, schema migrations and quotas.

- **Problem:** Each feature creating its own storage multiplies bugs, I/O and privacy risk.
- **Use case:** Workspaces, archived tabs and highlights all persist in one store and are searchable.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [CORE-005](core.md#core-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Single store with per-module tables and quotas
  - Encrypted at rest where sensitive
  - Migration and corruption-recovery tests
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Corresponds to 'local indexing of authorized information' in section C; vector index approach is Research (ADR-0007).

<a id="mem-015"></a>

## MEM-015 — Semantic and text search

`Flagship` · `Research` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Tracked together with MEM-002 (Smart Memory).

- **Problem:** Users remember what a page was about but not its title or URL.
- **Use case:** Search memory by meaning and by exact words.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-002](#mem-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Optional · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — content index; encrypted, excludable and deletable.
- **Competitors / precedents:** Edge (verify), Rewind/Recall-style tools
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of MEM-002
  - Use case verified: Search memory by meaning and by exact words.
- **Origin:** C · **Duplicate of:** [MEM-002](#mem-002)
- **Limitations / notes:** Technical duplicate merged into MEM-002; kept as its own entry to preserve the use case and traceability.

<a id="mem-016"></a>

## MEM-016 — Memory export and import

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Tracked together with MEM-030 (Exit Freedom).

- **Problem:** Browsers lock users in by making data hard to take elsewhere.
- **Use case:** Export and import Brumel Memory data (archives, highlights, snapshots).
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-030](#mem-030)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of MEM-030
  - Use case verified: Export and import Brumel Memory data (archives, highlights, snapshots).
- **Origin:** C · **Duplicate of:** [MEM-030](#mem-030)
- **Limitations / notes:** Technical duplicate merged into MEM-030; kept as its own entry to preserve the use case and traceability.

<a id="mem-017"></a>

## MEM-017 — Configurable local activity journal

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Opt-in local journal of browsing activity by day (time per site, tasks), never uploaded.

- **Problem:** Users want to understand where their time went without cloud trackers.
- **Use case:** A freelancer reviews which client sites they worked on yesterday.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014), [MEM-018](#mem-018)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — opt-in only.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Off by default
  - Granular retention
  - Excludes incognito and sensitive sites
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** A detailed activity journal is a surveillance risk on shared or managed devices; it stays opt-in and may be rejected if misuse risk outweighs value.

<a id="mem-018"></a>

## MEM-018 — Incognito and sensitive-site exclusion

`Essential` · `Planned` · **P0** · Impact Critical · Complexity S · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-MEM-01 (Brumel Store and local index)

Guarantee that incognito, guest, locked spaces and user/sensitive-category sites are never indexed, snapshotted or journaled.

- **Problem:** Memory features can accidentally record the most sensitive browsing.
- **Use case:** A user adds their bank and health sites to exclusions; nothing from them appears in Memory.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** Low — this is the protection itself.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Tests prove incognito never writes to the Brumel Store
  - Default sensitive categories list
  - Exclusions apply retroactively (purge)
- **Origin:** C · **Duplicate of:** —
- **Limitations / notes:** Sensitive-category detection by domain lists is incomplete; users must still add exclusions, and pages opened before an exclusion need a purge.

<a id="mem-019"></a>

## MEM-019 — Resume Cards

`Flagship` · `Research` · **P2** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Cards that capture a task (tabs, scroll positions, notes, drafts) so it can be resumed later in one click.

- **Problem:** Interrupted tasks are expensive to rebuild.
- **Use case:** A user resumes 'Visa application' with all forms, tabs and notes as they left them.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-001](#mem-001), [WRK-004](workspace.md#wrk-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - One-click resume
  - Card content explicit and editable
  - Unloaded until resumed
- **Origin:** R52-01 · **Duplicate of:** —
- **Limitations / notes:** Resuming relies on pages restoring from URLs; tasks involving server-side sessions or one-time links cannot be perfectly resumed.

<a id="mem-020"></a>

## MEM-020 — Universal Undo

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Undo for destructive browser actions: closing windows/groups/workspaces, clearing data scopes, Smart Optimize, bulk bookmark edits.

- **Problem:** Destructive browser actions are often irreversible.
- **Use case:** A user accidentally closes a window with 40 tabs and presses Ctrl+Shift+Z to bring it back.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Undo available for all listed actions within a time window
  - Clearing data warns when undo is impossible
- **Origin:** R52-02 · **Duplicate of:** —
- **Limitations / notes:** Some actions are inherently irreversible (clearing cookies logs users out server-side, data already sent to sites); undo must state its limits.

<a id="mem-021"></a>

## MEM-021 — Copy with Source

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-MEM-04 (Recall, vaults and page history)

Copy text together with its URL, title and access date in a chosen citation format.

- **Problem:** Copied quotes lose their origin.
- **Use case:** A student copies a paragraph and pastes it with a formatted citation.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [UI-001](interface.md#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Formats: plain, Markdown, APA-like
  - Opt-in per action
  - No tracking
- **Origin:** R52-03 · **Duplicate of:** —
- **Limitations / notes:** Clipboard formats vary by destination app; rich citations may degrade to plain text, and sites can alter clipboard behavior.

<a id="mem-022"></a>

## MEM-022 — Page Change History

`Secondary` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Compare a page with the version seen on a previous visit (for saved or watched pages).

- **Problem:** Terms, prices and articles change silently.
- **Use case:** A user sees which clauses of a terms page changed since their last visit.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-003](#mem-003)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Diff only for pages the user saved/watched
  - Local storage only
- **Origin:** R52-04 · **Duplicate of:** —
- **Limitations / notes:** Requires a stored previous version; diffs on dynamic pages (ads, timestamps) are noisy and need content extraction to be useful.

<a id="mem-023"></a>

## MEM-023 — Page Watchers

`Flagship` · `Research` · **P2** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Monitor a selected page element (price, stock, appointment slot) and notify on change.

- **Problem:** Users refresh pages manually to catch changes.
- **Use case:** A user watches a clinic's appointment page and gets notified when a slot appears.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [ENG-045](engine.md#eng-045), [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None — local polling.
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Element selection UI
  - Polling respects rate limits and Idle Scheduler
  - Runs without account or server
- **Origin:** R52-05 · **Duplicate of:** —
- **Limitations / notes:** Logged-in pages may expire; uses Session Guardian. Sites may block frequent polling.

<a id="mem-024"></a>

## MEM-024 — Dead Link Recovery

`Secondary` · `Research` · **P3** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

When a page is gone (404/domain expired), offer the user's own saved copy or public archives (e.g. Internet Archive) with consent.

- **Problem:** Link rot breaks references and bookmarks.
- **Use case:** A bookmark returns 404 and Brumel offers the archived copy.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-003](#mem-003)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** Medium — archive lookups disclose the URL to the archive service.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Public archive lookups are opt-in (leak URL)
  - Own copies preferred
- **Origin:** R52-06 · **Duplicate of:** —
- **Limitations / notes:** Public archive lookups send the URL to a third party and may not exist for private or recent pages.

<a id="mem-025"></a>

## MEM-025 — Receipt Vault

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Save confirmation pages and PDFs of purchases, bookings and government procedures in a searchable vault.

- **Problem:** Proof of purchase or submission is hard to find when needed.
- **Use case:** A user finds the confirmation of a tax filing from last year in seconds.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-003](#mem-003), [NANO-015](nano.md#nano-015)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — financial and identity data; encrypted and excluded from sync by default.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Manual save always available
  - Automatic detection only as suggestion
  - Encrypted storage
- **Origin:** R52-07 · **Duplicate of:** —
- **Limitations / notes:** Automatic detection of receipts would require content analysis; manual save stays primary, and stored receipts are high-value data needing strong encryption.

<a id="mem-026"></a>

## MEM-026 — Already Searched

`Secondary` · `Research` · **P3** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

When repeating a search, show previous searches on the topic and pages the user visited from them.

- **Problem:** Users repeat the same research from scratch.
- **Use case:** Searching 'best router 2027' again shows the three pages read last time.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Local only
  - Can be disabled
  - Excludes incognito
- **Origin:** R52-08 · **Duplicate of:** —
- **Limitations / notes:** Requires retaining search queries locally, which are among the most sensitive data; must be excludable and disabled in incognito.

<a id="mem-027"></a>

## MEM-027 — Video Search

`Experimental` · `Research` · **P3** · Impact Medium · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Search words inside videos (captions or local speech recognition) and jump to the timestamp.

- **Problem:** Finding a moment in a long video means scrubbing manually.
- **Use case:** A user searches a 2-hour lecture for 'eigenvalues' and jumps to minute 47.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [NANO-021](nano.md#nano-021), [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Optional · **Resource cost:** High during transcription; scheduled via Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Uses existing captions first
  - Local ASR optional (NANO-021)
  - Index stored locally
- **Origin:** R52-09 · **Duplicate of:** —
- **Limitations / notes:** Many video sites restrict caption access or use DRM; local ASR is CPU/GPU-intensive and accuracy varies by language and audio quality.

<a id="mem-028"></a>

## MEM-028 — Session Guardian

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-MEM-03 (Draft, form and login protection)

Warn when a site session is about to expire (where detectable) and protect form progress before logout.

- **Problem:** Sites log users out mid-task and discard their work.
- **Use case:** A user filling a long government form gets a warning before session timeout and their input is preserved.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-004](#mem-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Heuristics documented and conservative
  - Relies on Draft Protection for content
- **Origin:** R52-18 · **Duplicate of:** —
- **Limitations / notes:** Session expiry is often not observable; false negatives expected.

<a id="mem-029"></a>

## MEM-029 — Login Memory

`Flagship` · `Planned` · **P2** · Impact High · Complexity S · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-MEM-03 (Draft, form and login protection)

Remember which sign-in method was used on each site (password, Google/Apple/GitHub SSO, passkey, email link) without storing secrets.

- **Problem:** Users forget whether they signed up with email or a social login and create duplicate accounts.
- **Use case:** Visiting a site shows 'You signed in with GitHub last time'.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common user frustration; needs validation.
- **Acceptance criteria:**
  - Stores method only, no credentials
  - Local and deletable
  - Accurate on top sign-in flows
- **Origin:** R52-19 · **Duplicate of:** —
- **Limitations / notes:** Sign-in method detection relies on recognizing OAuth/SSO flows; custom or embedded login flows will be missed or misclassified.

<a id="mem-030"></a>

## MEM-030 — Exit Freedom

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-MEM-02 (Browser Time Machine, Zero Loss and data portability)

Complete export of user data (bookmarks, history, passwords with warning, workspaces, highlights, rules, settings) to open, documented formats.

- **Problem:** Browsers lock users in by making data hard to take elsewhere.
- **Use case:** A user leaves Brumel and imports everything into another browser or tool.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [CORE-044](core.md#core-044), [MEM-014](#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — stores browsing context; must be local, encrypted, excludable and deletable.
- **Competitors / precedents:** Vivaldi, Edge, Arc, Opera
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Every user-visible data type exportable
  - Formats documented (HTML, CSV, JSON, Markdown)
  - Export tested round-trip
- **Origin:** R52-31 · **Duplicate of:** —
- **Limitations / notes:** Some data cannot be exported meaningfully (cookies for security reasons, extension-internal data); password export is plain text and must carry strong warnings.
