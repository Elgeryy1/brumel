<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Workspace — tabs and productivity

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

38 entries. Epics in this module:

- **EP-WRK-01** Tab strip: vertical tabs, trees and folders — phase 2 (Internal Alpha), P0
- **EP-WRK-02** Workspaces, identities and routing — phase 4 (Public Beta), P1
- **EP-WRK-03** Infinite Tabs, archiving and session recovery — phase 2 (Internal Alpha), P0
- **EP-WRK-04** Universal search, quick actions, split view and panels — phase 3 (Public Alpha), P1
- **EP-WRK-05** Attention tools, collections and rules engine — phase 3 (Public Alpha), P2

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [WRK-001](#wrk-001) | Horizontal and vertical tabs | Essential | Planned | P0 | 2 |
| [WRK-002](#wrk-002) | Tab trees | Secondary | Planned | P2 | 3 |
| [WRK-003](#wrk-003) | Folders and subfolders | Secondary | Planned | P2 | 3 |
| [WRK-004](#wrk-004) | Workspaces | Flagship | Planned | P1 | 4 |
| [WRK-005](#wrk-005) | Pinned and temporary tabs *(→ WRK-013)* | Secondary | Planned | P2 | 3 |
| [WRK-006](#wrk-006) | Split view | Flagship | Planned | P1 | 3 |
| [WRK-007](#wrk-007) | Floating link preview | Secondary | Planned | P2 | 3 |
| [WRK-008](#wrk-008) | Infinite Tabs | Flagship | Planned | P1 | 3 |
| [WRK-009](#wrk-009) | Smart Router | Flagship | Planned | P2 | 4 |
| [WRK-010](#wrk-010) | Multi Identity | Flagship | Planned | P1 | 4 |
| [WRK-011](#wrk-011) | Temporary Identity | Secondary | Planned | P2 | 4 |
| [WRK-012](#wrk-012) | Private Spaces | Secondary | Planned | P2 | 4 |
| [WRK-013](#wrk-013) | Temporary Tabs | Secondary | Planned | P2 | 3 |
| [WRK-014](#wrk-014) | Tab DNA | Experimental | Research | P3 | 4 |
| [WRK-015](#wrk-015) | Live Collections | Experimental | Research | P3 | 4 |
| [WRK-016](#wrk-016) | Smart Bookmarks | Secondary | Planned | P2 | 4 |
| [WRK-017](#wrk-017) | Universal Search | Flagship | Planned | P1 | 3 |
| [WRK-018](#wrk-018) | Quick Actions | Flagship | Planned | P1 | 3 |
| [WRK-019](#wrk-019) | Search across all tabs *(→ WRK-017)* | Flagship | Planned | P1 | 3 |
| [WRK-020](#wrk-020) | Local-AI automatic tab grouping | Secondary | Research | P2 | 4 |
| [WRK-021](#wrk-021) | Smart archiving | Essential | Planned | P1 | 3 |
| [WRK-022](#wrk-022) | Duplicate tab detection | Secondary | Planned | P2 | 3 |
| [WRK-023](#wrk-023) | Session recovery | Essential | Planned | P0 | 2 |
| [WRK-024](#wrk-024) | Named saved sessions | Secondary | Planned | P2 | 3 |
| [WRK-025](#wrk-025) | Web side panels | Secondary | Planned | P2 | 3 |
| [WRK-026](#wrk-026) | Focus Mode | Secondary | Planned | P2 | 3 |
| [WRK-027](#wrk-027) | Research Mode | Experimental | Research | P3 | 4 |
| [WRK-028](#wrk-028) | Web Highlights | Secondary | Planned | P2 | 4 |
| [WRK-029](#wrk-029) | Smart Compare | Experimental | Research | P3 | 4 |
| [WRK-030](#wrk-030) | Visual no-code rules engine | Flagship | Planned | P2 | 4 |
| [WRK-031](#wrk-031) | Tab Snooze | Secondary | Planned | P2 | 3 |
| [WRK-032](#wrk-032) | Reading Queue | Secondary | Planned | P2 | 3 |
| [WRK-033](#wrk-033) | Intent Anchor | Experimental | Research | P3 | 4 |
| [WRK-034](#wrk-034) | Infinite Scroll Brake | Experimental | Research | P3 | 4 |
| [WRK-035](#wrk-035) | Spaced Highlights | Experimental | Research | P3 | 4 |
| [WRK-036](#wrk-036) | Quiet Inbox | Secondary | Research | P2 | 4 |
| [WRK-037](#wrk-037) | Web App Dock | Secondary | Planned | P2 | 4 |
| [WRK-038](#wrk-038) | System Search Integration | Experimental | Research | P3 | 4 |

<a id="wrk-001"></a>

## WRK-001 — Horizontal and vertical tabs

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Everyday Tools · Epic EP-WRK-01 (Tab strip: vertical tabs, trees and folders)

Switch between a horizontal tab strip and a vertical tab sidebar, building on upstream Chromium's native vertical tabs and extending them (trees, folders, workspaces).

- **Problem:** Horizontal tabs become unreadable beyond ~15 tabs; wide screens waste horizontal space.
- **Use case:** A user with 40 tabs switches to vertical tabs and reads full titles.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [UI-001](interface.md#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Chrome (vertical tabs since Chrome 147, as reported), Edge, Vivaldi, Arc, Zen, Brave
- **Evidence:** Competitor precedent; Chrome shipped native vertical tabs in 2026 (Chrome 146 flag, 147 rollout, per press reports — verify upstream Chromium code paths).
- **Acceptance criteria:**
  - Switch without restart
  - Keyboard and screen-reader accessible
  - Drag and drop parity
  - Brumel extensions layered on upstream code, not a parallel implementation
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Reusing upstream vertical tabs reduces maintenance; Brumel-specific extensions must be minimal patches.

<a id="wrk-002"></a>

## WRK-002 — Tab trees

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-01 (Tab strip: vertical tabs, trees and folders)

Hierarchical tabs showing which tab opened which, collapsible.

- **Problem:** Research sessions lose the relationship between pages.
- **Use case:** A user collapses a branch of 12 tabs opened from one search result page.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-001](#wrk-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Vivaldi (stacks), Firefox (Tree Style Tab extension)
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Opener relationships preserved across restart
  - Collapse/expand
  - Move subtree
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Upstream Chromium has no tab-tree model; trees require patches to tab strip models that are among the most frequently changed upstream code.

<a id="wrk-003"></a>

## WRK-003 — Folders and subfolders

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-01 (Tab strip: vertical tabs, trees and folders)

User folders in the vertical tab bar, nestable.

- **Problem:** Groups alone do not scale to many long-lived topics.
- **Use case:** A user keeps a 'Projects > Client A' folder of pinned tabs.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-001](#wrk-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Zen
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Nested folders persist
  - Folders can hold unloaded tabs
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Folders overlap with tab groups and bookmarks; without careful UX they create a third, confusing organization system.

<a id="wrk-004"></a>

## WRK-004 — Workspaces

`Flagship` · `Planned` · **P1** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-02 (Workspaces, identities and routing)

Named sets of tabs, folders and settings that can be switched instantly; inactive workspaces stay unloaded.

- **Problem:** Mixing work, study and personal tabs in one window overloads attention and memory.
- **Use case:** A user switches from 'Work' to 'Personal' and only that workspace's tabs are visible and loaded.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-001](#wrk-001), [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Zen, Edge, Vivaldi, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Switching does not load inactive workspaces
  - Per-workspace RAM budget (ENG-005)
  - Workspaces persist and export
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Chromium windows and profiles were not designed for instant context switching; implementing workspaces as patches to browser and session code is a major maintenance commitment.

<a id="wrk-005"></a>

## WRK-005 — Pinned and temporary tabs

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-01 (Tab strip: vertical tabs, trees and folders)

Tracked together with WRK-013 (Temporary Tabs).

- **Problem:** Quick lookups accumulate as permanent clutter.
- **Use case:** Mix of permanently pinned (CORE-033) and auto-expiring tabs in the sidebar.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-013](#wrk-013)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of WRK-013
  - Use case verified: Mix of permanently pinned (CORE-033) and auto-expiring tabs in the sidebar.
- **Origin:** B · **Duplicate of:** [WRK-013](#wrk-013)
- **Limitations / notes:** Technical duplicate merged into WRK-013; kept as its own entry to preserve the use case and traceability.

<a id="wrk-006"></a>

## WRK-006 — Split view

`Flagship` · `Planned` · **P1** · Impact High · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-04 (Universal search, quick actions, split view and panels)

Show two or more pages side by side in one window with resizable panes.

- **Problem:** Comparing or referencing pages requires juggling windows.
- **Use case:** A user writes in a document while reading a reference article beside it.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-001](#wrk-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Chrome (Split View since Chrome 145, two panes, as reported), Vivaldi, Arc, Zen, Edge
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - 2–4 panes
  - Keyboard focus and accessibility work
  - Panes persist with session
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Upstream Chromium Split View (two panes) is the base; Brumel adds more panes and session persistence only if maintainable.

<a id="wrk-007"></a>

## WRK-007 — Floating link preview

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-04 (Universal search, quick actions, split view and panels)

Preview a link in a floating panel without opening a tab.

- **Problem:** Opening tabs just to peek creates clutter.
- **Use case:** A user previews a search result and closes it with Esc.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-001](#wrk-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc (Peek), Opera, Zen (Glance)
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Preview uses a normal sandboxed renderer
  - Promote to tab
  - Disabled under Battery Saver
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Previews spawn real renderers (memory, network, site visits counted as visits); they are disabled under constrained profiles and cannot be offered for every link type.

<a id="wrk-008"></a>

## WRK-008 — Infinite Tabs

`Flagship` · `Planned` · **P1** · Impact Critical · Complexity L · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-03 (Infinite Tabs, archiving and session recovery)

Keep hundreds of tabs as lightweight entries (title, favicon, state, scroll) without renderer processes; load on demand.

- **Problem:** Heavy tab users keep tabs as a to-do list, which overwhelms memory.
- **Use case:** A user keeps 500 tabs across workspaces while memory stays close to that of a few loaded tabs.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [ENG-019](engine.md#eng-019), [MEM-014](memory.md#mem-014), [WRK-023](#wrk-023)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Hypothesis: savings must be shown in the 100/200-tab benchmarks.
- **Acceptance criteria:**
  - 500-tab benchmark measured vs Chrome
  - Restoring a tab restores URL, scroll and form state where possible
  - No data loss on crash
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Unloaded tabs lose in-memory page state; sites without URL-based state (some web apps, POST results) cannot be faithfully restored.

<a id="wrk-009"></a>

## WRK-009 — Smart Router

`Flagship` · `Planned` · **P2** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-02 (Workspaces, identities and routing)

Rules that open specific sites in a chosen identity, profile or workspace automatically.

- **Problem:** Users manually move links to the right profile (work vs personal) all day.
- **Use case:** Links to the company's tools always open in the Work identity, even when clicked from a personal chat.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-010](#wrk-010), [WRK-004](#wrk-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Edge (automatic profile switching), Firefox (Multi-Account Containers)
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Rules by domain/pattern
  - External links routed too
  - Rule matches are explainable
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Links opened by external apps arrive without context; routing by domain can misfire for shared domains (e.g. Google Docs used for both work and personal).

<a id="wrk-010"></a>

## WRK-010 — Multi Identity

`Flagship` · `Planned` · **P1** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-02 (Workspaces, identities and routing)

Isolated cookie/storage partitions (container-like identities) usable side by side in one window.

- **Problem:** Using two accounts of the same site requires separate profiles or windows.
- **Use case:** A user keeps a personal and a work Google account open in adjacent tabs.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [CORE-026](core.md#core-026)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Medium — partitioning must not leak across identities.
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Firefox (Containers), Vivaldi, Arc
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Storage partitions fully isolated
  - Identity is visible on each tab
  - Works with extensions as documented
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Chromium lacks native containers; requires StoragePartition work. Complexity high.

<a id="wrk-011"></a>

## WRK-011 — Temporary Identity

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-02 (Workspaces, identities and routing)

Disposable identity whose storage is wiped when its tabs close.

- **Problem:** Incognito windows are all-or-nothing and separate from the user's workspace.
- **Use case:** A user opens a coupon site in a temporary identity next to normal tabs.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-010](#wrk-010)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Firefox (Temporary Containers extension)
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Storage wiped on close
  - Clear visual indicator
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Extensions with all-site access can still observe temporary identities unless disabled there; the feature is not anonymity.

<a id="wrk-012"></a>

## WRK-012 — Private Spaces

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-02 (Workspaces, identities and routing)

Workspaces locked behind local OS authentication (Windows Hello/PAM).

- **Problem:** Shared computers expose sensitive tabs (health, finance) to others.
- **Use case:** A user locks a 'Health' space that requires Windows Hello to open.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-004](#wrk-004), [SHD-019](shield.md#shd-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Medium — local auth is not protection against malware with user access.
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Locked space content not visible in UI or switcher
  - Data encrypted at rest (SHD-020)
  - Auto-lock timeout
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Local authentication protects against casual access only; malware or another admin user on the device can still read memory and files.

<a id="wrk-013"></a>

## WRK-013 — Temporary Tabs

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-01 (Tab strip: vertical tabs, trees and folders)

Tabs that auto-close or archive after rules (time, inactivity) unless pinned.

- **Problem:** Quick lookups accumulate as permanent clutter.
- **Use case:** Tabs not touched for 12 hours move to the archive automatically.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-021](#wrk-021)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Configurable expiry
  - Archived, not deleted
  - Undo
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Expiring tabs can archive something the user still needed; archive-not-delete and undo are required, which keeps data around longer.

<a id="wrk-014"></a>

## WRK-014 — Tab DNA

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-WRK-01 (Tab strip: vertical tabs, trees and folders)

Record and show provenance: which page, search or app opened a tab.

- **Problem:** Users forget why a tab is open and where it came from.
- **Use case:** A user sees a tab came from a search for 'flight Madrid Lisbon' three days ago.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-002](#wrk-002), [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Opener chain stored locally
  - Viewable from tab context menu
  - Excluded in incognito
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Opener information is lost for tabs opened from external apps or by sites using noopener; provenance will be incomplete.

<a id="wrk-015"></a>

## WRK-015 — Live Collections

`Experimental` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Dynamic collections built from rules (e.g. all tabs from a domain or with a tag).

- **Problem:** Manual organization does not keep up with browsing.
- **Use case:** A collection automatically gathers all open GitHub PR tabs.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-030](#wrk-030)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Rule-based membership
  - Updates live
  - No AI required
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Rules based on URL patterns are brittle when sites change URLs; collections may silently miss items.

<a id="wrk-016"></a>

## WRK-016 — Smart Bookmarks

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Bookmark organization assistance: duplicate and dead-link detection, folder suggestions.

- **Problem:** Bookmark collections rot over years.
- **Use case:** A user removes 200 duplicate and dead bookmarks after a review.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [CORE-029](core.md#core-029)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Deterministic-first · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Duplicate detection deterministic
  - Dead-link checks opt-in and rate-limited
  - Suggestions never auto-applied
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Dead-link checks make network requests to bookmarked sites, which can reveal bookmarks to those sites; they must be opt-in and rate-limited.

<a id="wrk-017"></a>

## WRK-017 — Universal Search

`Flagship` · `Planned` · **P1** · Impact High · Complexity L · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-04 (Universal search, quick actions, split view and panels)

One search box over open tabs, archived tabs, history, bookmarks, downloads and settings.

- **Problem:** Users search separately in tabs, history and bookmarks.
- **Use case:** A user types 'invoice' and finds the open tab, a download and a bookmark.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Edge
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Sub-100 ms local results target (to be measured)
  - Keyboard-first
  - Scopes filterable
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Full-text search of page content requires indexing it, which raises storage and privacy costs; default scope will be titles and URLs.

<a id="wrk-018"></a>

## WRK-018 — Quick Actions

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-04 (Universal search, quick actions, split view and panels)

Command palette to run browser actions (switch workspace, toggle profile, mute, export) by typing.

- **Problem:** Power features are hidden in menus.
- **Use case:** A user presses Ctrl+K and types 'battery' to switch profile.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [UI-001](interface.md#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Vivaldi, Arc, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - All core actions reachable
  - Extensible by modules
  - Accessible
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** A palette is only as good as the action registry; module actions must be registered and kept accessible, or the palette becomes inconsistent.

<a id="wrk-019"></a>

## WRK-019 — Search across all tabs

`Flagship` · `Planned` · **P1** · Impact High · Complexity L · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-04 (Universal search, quick actions, split view and panels)

Tracked together with WRK-017 (Universal Search).

- **Problem:** Users search separately in tabs, history and bookmarks.
- **Use case:** Find text and titles across all open and archived tabs.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-017](#wrk-017)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Edge
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of WRK-017
  - Use case verified: Find text and titles across all open and archived tabs.
- **Origin:** B · **Duplicate of:** [WRK-017](#wrk-017)
- **Limitations / notes:** Technical duplicate merged into WRK-017; kept as its own entry to preserve the use case and traceability.

<a id="wrk-020"></a>

## WRK-020 — Local-AI automatic tab grouping

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Suggest tab groups and names with Brumel Nano, with deterministic grouping (domain, opener) as fallback.

- **Problem:** Manual grouping is tedious.
- **Use case:** A user clicks 'Suggest groups' and accepts three proposed groups.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [NANO-001](nano.md#nano-001), [CORE-032](core.md#core-032)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Optional · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Chrome (Tab organizer), Edge, Arc
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Suggestions only, never automatic without consent
  - Works without AI via deterministic rules
  - Quality evaluated on labeled set
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Small-model grouping quality is unproven and language-dependent; deterministic grouping may be good enough and is preferred if evaluation shows little gain.

<a id="wrk-021"></a>

## WRK-021 — Smart archiving

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-WRK-03 (Infinite Tabs, archiving and session recovery)

Archive tabs instead of closing them; archived tabs are searchable and restorable.

- **Problem:** Users keep tabs open out of fear of losing them.
- **Use case:** A user archives a finished project's 30 tabs and restores one a month later.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Archive is searchable via Universal Search
  - Restore preserves URL and metadata
  - Retention configurable
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Archived tabs keep URLs and titles indefinitely unless retention is configured, growing the local data footprint and its sensitivity.

<a id="wrk-022"></a>

## WRK-022 — Duplicate tab detection

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-03 (Infinite Tabs, archiving and session recovery)

Detect duplicate or near-duplicate URLs and offer to switch or merge.

- **Problem:** Users open the same page many times.
- **Use case:** Opening a URL already open offers to switch to the existing tab.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-001](#wrk-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Deterministic-first · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Configurable URL normalization
  - Never auto-closes
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** URL normalization can wrongly treat different pages as duplicates (query parameters that matter); suggestions must never auto-close.

<a id="wrk-023"></a>

## WRK-023 — Session recovery

`Essential` · `Planned` · **P0** · Impact Critical · Complexity M · Phase 2 (Internal Alpha) · Pillar Memory · Epic EP-WRK-03 (Infinite Tabs, archiving and session recovery)

Robust session saving and restore after crash, update or forced shutdown, including windows, groups, workspaces and pinned tabs.

- **Problem:** Losing a session after a crash or update is one of the most painful browser failures.
- **Use case:** After a power loss, a user restores all windows and workspaces as they were.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Session snapshots are atomic and versioned
  - Crash-recovery tests in CI
  - Restore never silently drops tabs
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Upstream session restore is solid but session files can still be corrupted by abrupt power loss; versioned snapshots add disk writes.

<a id="wrk-024"></a>

## WRK-024 — Named saved sessions

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-03 (Infinite Tabs, archiving and session recovery)

Save and reopen named sets of windows and tabs.

- **Problem:** Recurring tasks need the same set of tabs repeatedly.
- **Use case:** A user saves 'Monthly accounting' and reopens it next month.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-023](#wrk-023)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Vivaldi, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Save/restore/rename/delete
  - Export as file
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Saved sessions are snapshots of URLs; page state, logins and forms are not preserved.

<a id="wrk-025"></a>

## WRK-025 — Web side panels

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-04 (Universal search, quick actions, split view and panels)

Pin web apps (chat, notes, music) to the sidebar as panels.

- **Problem:** Frequently used apps take full tabs.
- **Use case:** A user keeps a chat app in a side panel while browsing.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-001](#wrk-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Vivaldi, Opera, Edge
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Panels use standard sandboxed renderers
  - Panels can be suspended
  - Mobile UA optional
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Side panels run full web apps that keep consuming resources unless suspended; mobile user agents can break some sites.

<a id="wrk-026"></a>

## WRK-026 — Focus Mode

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Hide UI and other tabs, silence notifications and block configured distracting sites for a period.

- **Problem:** Browsers are the main source of distraction during focused work.
- **Use case:** A student starts a 50-minute focus session blocking social sites.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [UI-001](interface.md#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Timer and block list
  - Can be ended any time
  - Integrates with Quiet Inbox (WRK-036)
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Site blocking is easy to bypass by design (user can end the session); it supports intention, it is not parental control.

<a id="wrk-027"></a>

## WRK-027 — Research Mode

`Experimental` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Workspace preset combining tab trees, highlights, Copy with Source and a notes pane for research tasks.

- **Problem:** Research across many sources loses citations and context.
- **Use case:** A student collects quotes with sources while reading 20 papers.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-004](#wrk-004), [WRK-028](#wrk-028), [MEM-021](memory.md#mem-021)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Composed of existing features, no new data store
  - Exports notes with citations
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Composite feature that only works as well as its components (highlights, citations); risk of UI complexity for a niche audience.

<a id="wrk-028"></a>

## WRK-028 — Web Highlights

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Memory · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Highlight text on pages, stored locally and re-shown on revisit (using text fragments anchoring).

- **Problem:** Insights from reading are lost.
- **Use case:** A user highlights a paragraph and finds it again later via search.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Edge (collections, verify), Extensions (Hypothesis, Glasp)
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Highlights anchor robustly or fail visibly
  - Searchable
  - Exportable to Markdown
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Anchors based on text fragments break when page text changes; highlights on dynamic or logged-in pages may not reattach.

<a id="wrk-029"></a>

## WRK-029 — Smart Compare

`Experimental` · `Research` · **P3** · Impact Medium · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Compare products or options across tabs using deterministic extraction (structured data, tables) with every value linked to its source location.

- **Problem:** Comparing specs across shops is manual and error-prone; AI summaries hallucinate.
- **Use case:** A user compares three laptops and each cell links to the highlighted text on the source page.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [TLS-030](tools.md#tls-030), [WRK-006](#wrk-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Deterministic-first · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Every value has a verifiable source anchor
  - Unverifiable values are marked, never invented
  - No small-model-only factual claims (see NANO-030)
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** Extraction is only reliable where pages expose structured data or clear tables; many shops render specs inconsistently, so many cells will be marked unverifiable.

<a id="wrk-030"></a>

## WRK-030 — Visual no-code rules engine

`Flagship` · `Planned` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Shared 'if condition then action' rules editor used by routing, profiles, temporary tabs, downloads and watchers.

- **Problem:** Each feature reinventing its own rule settings is confusing and buggy.
- **Use case:** A user creates: 'If download is a PDF from bank.example, move it to Finance'.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [CORE-005](core.md#core-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Single rule model reused by modules
  - Rules testable with preview
  - Exportable recipes (UI-021)
- **Origin:** B · **Duplicate of:** —
- **Limitations / notes:** A general rules engine is a large UX and testing surface; complex rules can conflict across modules and need a clear precedence model.

<a id="wrk-031"></a>

## WRK-031 — Tab Snooze

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Memory · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Hide a tab until a date, time or condition (e.g. next workday, page change) and bring it back.

- **Problem:** Tabs kept open as reminders clutter the browser and memory.
- **Use case:** A user snoozes a concert ticket page until sales open on Friday.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-021](#wrk-021), [ENG-045](engine.md#eng-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Snoozed tabs unloaded
  - Reappear reliably after restart
  - List of snoozed tabs
- **Origin:** R52-10 · **Duplicate of:** —
- **Limitations / notes:** Condition-based snoozing (page changes) requires polling via Page Watchers with its rate limits; time-based snoozing depends on the browser running.

<a id="wrk-032"></a>

## WRK-032 — Reading Queue

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-03 (Infinite Tabs, archiving and session recovery)

Queue articles to read later without keeping them loaded; optional offline copy.

- **Problem:** Read-later tabs consume memory and get lost.
- **Use case:** A user queues five articles and reads them offline on a train.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-021](#wrk-021)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Chrome (Reading list), Safari, Edge
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Queue items unloaded
  - Optional offline copy (MEM-003)
  - Progress tracked
- **Origin:** R52-11 · **Duplicate of:** —
- **Limitations / notes:** Offline copies may not include dynamically loaded content or paywalled text; queue sync across devices depends on Connect.

<a id="wrk-033"></a>

## WRK-033 — Intent Anchor

`Experimental` · `Research` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Optionally note what you came to do when opening a new session or workspace; gently remind when drifting.

- **Problem:** Users open the browser for one task and end up somewhere else.
- **Use case:** A user types 'pay electricity bill' and gets a reminder after 20 minutes on video sites.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-004](#wrk-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Hypothesis: value for attention needs user research.
- **Acceptance criteria:**
  - Opt-in only
  - Stored locally
  - Reminder dismissible and not nagging
- **Origin:** R52-12 · **Duplicate of:** —
- **Limitations / notes:** Detecting 'drifting' requires watching browsing behavior; value is unproven and the feature can easily feel patronizing.

<a id="wrk-034"></a>

## WRK-034 — Infinite Scroll Brake

`Experimental` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Insert optional stop points in infinite feeds after a configurable amount of scrolling or time.

- **Problem:** Infinite feeds are designed to remove natural stopping points.
- **Use case:** After 15 minutes on a feed, a calm stop card asks whether to continue.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [UI-001](interface.md#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Opt-in per site
  - Does not break page functionality
  - Easy to continue
- **Origin:** R52-13 · **Duplicate of:** —
- **Limitations / notes:** Detecting feeds reliably across sites is hard; may require per-site rules.

<a id="wrk-035"></a>

## WRK-035 — Spaced Highlights

`Experimental` · `Research` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Memory · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Resurface saved highlights using spaced repetition.

- **Problem:** Highlighted knowledge is forgotten.
- **Use case:** A student reviews five past highlights each morning on the new tab page.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-028](#wrk-028)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Opt-in
  - Local scheduling
  - Export to Anki-compatible format
- **Origin:** R52-14 · **Duplicate of:** —
- **Limitations / notes:** Requires enough highlights to be useful; spaced-repetition scheduling is simple, not a replacement for dedicated learning tools.

<a id="wrk-036"></a>

## WRK-036 — Quiet Inbox

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Group web notifications, deliver them in batches and prioritize important senders.

- **Problem:** Web notifications interrupt constantly and look equally urgent.
- **Use case:** A user receives a digest of social notifications every hour but chat mentions immediately.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [CORE-045](core.md#core-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Per-site priority
  - Batching schedule
  - Never drops notifications silently
- **Origin:** R52-15 · **Duplicate of:** —
- **Limitations / notes:** Web notifications are delivered through the OS; batching delays notifications and could hide urgent ones if priorities are misconfigured.

<a id="wrk-037"></a>

## WRK-037 — Web App Dock

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Efficiency · Epic EP-WRK-04 (Universal search, quick actions, split view and panels)

Manage installed web apps (PWAs and site apps) from one place, sharing the browser engine instead of separate Electron apps.

- **Problem:** Every chat/collaboration app ships its own Electron runtime, multiplying memory use.
- **Use case:** A user replaces three Electron desktop apps with web apps managed in the dock.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [CORE-036](core.md#core-036)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Install/uninstall/launch from dock
  - Per-app permissions and resource limits
  - OS integration (taskbar, start menu)
- **Origin:** R52-36 · **Duplicate of:** —
- **Limitations / notes:** Not every Electron app has a full-featured web equivalent; some desktop-only features (system tray, offline sync, file system access) will be missing.

<a id="wrk-038"></a>

## WRK-038 — System Search Integration

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-04 (Universal search, quick actions, split view and panels)

Optional exposure of tabs and bookmarks to the OS search (Windows Search, GNOME/KDE search providers).

- **Problem:** Users search their OS for things that live in the browser.
- **Use case:** A Linux user finds a bookmarked page from the desktop search.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Research · Linux Research · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Medium — exposes browsing data to the OS index.
- **Competitors / precedents:** Arc, Vivaldi, Zen, Edge, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Opt-in
  - Excludes private/incognito/locked spaces
  - Removable index
- **Origin:** R52-38 · **Duplicate of:** —
- **Limitations / notes:** OS search APIs differ per platform and desktop environment; exposing browsing data to the OS index weakens Brumel's control over its deletion.
