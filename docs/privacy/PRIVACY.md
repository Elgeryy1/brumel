# Brumel Privacy Principles

Status: **Planned** — this describes how Brumel intends to handle data. There is no Brumel build yet, so nothing here is a description of shipped behavior. This is an engineering document, not a legal privacy policy; a formal privacy notice will be published before any public build or hosted service exists.

Related: [Threat Model](../security/THREAT_MODEL.md) · [Sync Architecture](../architecture/SYNC_ARCHITECTURE.md) · [AI Architecture](../architecture/AI_ARCHITECTURE.md) · [Compatibility](../architecture/COMPATIBILITY.md)

## 1. Principles

1. **Local-first.** Data is created, stored and processed on the user's device. Features must work fully offline and without an account unless their purpose is inherently online (for example sync).
2. **No mandatory telemetry.** Brumel does not collect usage data by default. Any telemetry is opt-in, documented field by field, inspectable before sending and removable.
3. **No mandatory account.** Every essential feature works without signing in to anything.
4. **No Brumel advertising, no data sales.** Brumel does not show its own ads, sponsored tiles or affiliate injections, and never sells or shares personal data.
5. **Verifiable, not promised.** The browser should show what it does. **Glass Box** (Planned) lists every connection the browser itself initiates — destination, purpose, feature responsible, and whether it can be turned off.
6. **Minimization.** Collect the least data, keep it the shortest time, and prefer computing on device.
7. **Off means off.** Disabling a feature stops its data collection and offers to delete what it stored.
8. **Portability.** Users can export everything in open formats and leave (Exit Freedom).
9. **Incognito and guest are sacred.** No Brumel feature indexes, remembers, syncs or analyzes incognito or guest activity.

## 2. Data inventory (planned features)

Retention values are proposed defaults, all user-configurable.

| Feature / module | Data | Stored where | Leaves device? | Proposed retention | User control |
| --- | --- | --- | --- | --- | --- |
| Chromium core: history, bookmarks, cookies, cache | Standard browser data | Profile directory | Only if user enables sync (E2EE) | Chromium defaults | Clear browsing data, per-site data controls |
| Passwords / passkeys | Credentials | OS-protected store via Chromium password manager | No (password sync Deferred) | Until deleted | Password manager UI, export |
| Brumel Engine: Performance History | CPU/RAM/energy samples per site and tab | Brumel Store | No | 30 days | Toggle, clear |
| Brumel Workspace: spaces, tab trees, sessions | Tab URLs, titles, structure | Brumel Store | Only via E2EE sync if enabled | Until deleted | Per-space delete, export |
| Brumel Memory: Time Machine, Smart Memory | Session snapshots, page text extracts, embeddings | Brumel Store, encrypted at rest | No | 90 days (proposed) | Off by default for full-text indexing (opt-in), per-site exclusions, delete all |
| Draft Protection | Text typed in eligible fields | Brumel Store, encrypted | No | 7 days | Per-site off; never password, payment or OTP fields |
| Offline Vault, Receipt Vault | Saved pages / receipts the user chooses | Brumel Store | Only via E2EE sync if enabled | Until deleted | Manual, export |
| Download Vault | Download metadata, optional file text index | Brumel Store | No | Follows download history | Toggle, clear |
| Brumel Shield: Privacy Receipt, Permission Timeline | Counts of blocked requests, permission events | Brumel Store | No | 30 days | Toggle, clear |
| Login Memory | Which sign-in method was used per site (not credentials) | Brumel Store | Only via E2EE sync if enabled | Until deleted | Per-site delete |
| Page Watchers | Selected page regions and their history | Brumel Store | Fetches the watched page | Until watcher deleted | Manage watchers |
| Brumel Nano | Model files; transient inputs/outputs | Component directory; memory only during inference | No (no network access) | Inputs not persisted unless feature stores a result | Remove model entirely |
| Optional cloud AI (BYOK) | The content the user sends for that request | Provider's servers | **Yes**, to the provider the user configured | Provider's policy | Opt-in per provider, per-request disclosure |
| Brumel Connect | Encrypted sync records, device list | Device + relay (ciphertext) | Yes, encrypted | Until deleted / account removal | Per-datatype toggles, delete server data |
| Crash reports | Minidumps | Device; uploaded only if opted in | Opt-in | 90 days on server (proposed) | Opt-in, review before sending (Research) |
| Telemetry (if ever) | Documented aggregate metrics | Device; uploaded only if opted in | Opt-in | Documented | Opt-in, view payload, off |

## 3. Network connections and Google service replacements

Chromium contacts Google services for several features. Brumel will audit every outbound connection (starting from ungoogled-chromium's work, [ADR-0002](../architecture/adr/0002-chromium-base-selection.md)) and classify each as **removed**, **replaced** or **user opt-in**. The full list will be published in Glass Box and in this document before the first public build.

| Chromium / Chrome function | Default in Chrome | Brumel plan | Status |
| --- | --- | --- | --- |
| Google Sync, Google account sign-in | Google | Removed; replaced by optional Brumel Connect (E2EE) | Planned |
| Safe Browsing | Google Safe Browsing | Research: privacy-preserving proxy or Update API with local hash prefixes; must keep strong phishing/malware protection — removal without replacement is **not** acceptable | Research |
| Search suggestions | Default search engine | User-chosen engine; suggestions toggle visible on first run | Planned |
| Translate | Google Translate endpoint | Local translation models (Bergamot-class) as default candidate; cloud opt-in | Research |
| Spellcheck dictionaries | Downloaded from Google | Mirror Hunspell dictionaries on Brumel component channel | Planned |
| Enhanced spellcheck | Google cloud | Removed; local only | Planned |
| Component updates (Widevine, CRLSets, etc.) | Google component updater | Brumel component server for Brumel components; Google-provided components only where license allows and user benefits (e.g. CRLSet-equivalent revocation data) — to be validated | Research |
| Crash reporting | Google | Opt-in, Brumel-operated or self-hostable endpoint | Planned |
| Domain reliability, usage stats, field trials | Google | Removed | Planned |
| Network time | Google | Removed or replaced with OS time checks | Research |
| Media Router / Cast discovery | Google Cast | Opt-in, local network only, subject to compatibility | Research |
| Prefetch / preconnect hints | Various | Smart Preload only to user-visited sites; no prediction services | Planned |
| Brumel updates | — | Brumel update server; requests carry version/platform/channel only | Planned |

Connections Brumel itself will initiate are limited to: updates, component downloads (models, filter lists, dictionaries), optional sync, optional crash reports and optional providers explicitly configured by the user.

## 4. Incognito, guest and sensitive sites

- No Memory, Nano, Workspace history, Performance History, Draft Protection or Login Memory in incognito or guest windows.
- Sensitive-site exclusions (banking, health, adult, government categories — configurable) for indexing features. The classification is local and deterministic (domain lists), not AI.
- Temporary Identity sessions are destroyed with all their storage when closed.

## 5. AI data handling

- Local by default: Brumel Nano runs on device in a sandboxed process without network access.
- No model training on user data. Brumel does not collect data to train models.
- Inputs are assembled per task and discarded after use unless the feature's purpose is to store a result (for example a tab group name).
- Optional cloud providers (OpenAI-compatible, Anthropic, Gemini, Ollama, custom, BYOK) are **off** by default. When enabled, every request shows what will be sent and to whom. API keys are stored with OS-protected encryption.

## 6. Sync

Brumel Connect encrypts data on the device before upload. The relay stores ciphertext and the minimum metadata needed for delivery (account identifier, device identifiers, record sizes rounded into buckets, timestamps). Details: [Sync Architecture](../architecture/SYNC_ARCHITECTURE.md).

## 7. Data portability

- Export everything (bookmarks, history, sessions, spaces, rules, settings, vaults, Memory index metadata) in open formats: HTML bookmarks, JSON, CSV, Markdown, SQLite where appropriate.
- Import from Chrome, Edge, Brave, Vivaldi, Firefox and others with explicit consent per data type (Migration Assistant, Chrome Coexistence).
- Deleting a profile deletes all Brumel data for it, including the Brumel Store and models (models are shared components and are removed when no profile uses them, or explicitly).

## 8. GDPR orientation (not legal advice)

The project intends to operate in a way compatible with the EU General Data Protection Regulation and similar laws. Processing that happens entirely on the user's device is under the user's control. For any service Brumel operates (update server, sync relay, crash reports):

- Lawful basis will be documented per service (for example legitimate interest for update checks, consent for crash reports and telemetry).
- Data subject rights (access, deletion, portability) will be supported; for E2EE sync the operator cannot read content, but can delete it.
- Processors (hosting providers such as Supabase) will be listed with their region.
- A formal privacy notice will be reviewed before any hosted service launches.

## 9. Changes to this document

Any feature that adds a new data store, network connection or data type must update the inventory in this document in the same pull request.
