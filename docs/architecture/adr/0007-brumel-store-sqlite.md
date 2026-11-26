# ADR-0007: Shared encrypted SQLite "Brumel Store" per profile

- Status: Proposed
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [Architecture §6](../ARCHITECTURE.md), [Privacy](../../privacy/PRIVACY.md), [Threat Model §5.3](../../security/THREAT_MODEL.md)

## Context

Memory, Workspace, Shield, Tools and Engine features need to store structured local data: session snapshots, text extracts, embeddings, vault items, performance samples, permission events. If each feature opens its own database, the result is many files, duplicated migration logic, inconsistent encryption and retention, and more background I/O. Chromium already ships SQLite (`//sql`) with FTS support and OSCrypt for key protection.

## Decision (proposed)

- One **Brumel Store** SQLite database per profile, accessed only from the browser process on a dedicated sequenced task runner, through a typed C++ API in `//brumel/components/store/`.
- Per-feature tables with a shared, versioned migration system; retention policies declared per table and enforced by the Idle Scheduler.
- **FTS5** for full-text search.
- **Encryption at rest** with keys protected by OSCrypt. Granularity (whole-database page encryption vs field-level encryption of sensitive columns) is an open question.
- **Vector search**: brute-force similarity over compact embeddings for small corpora as the starting point; an ANN index or SQLite vector extension is evaluated later for size, licensing and security.
- **Idle Scheduler**: one scheduler for deferrable background work across features (indexing, embedding, compaction, backups), aware of power, activity, thermal state and performance profile.
- Incognito and guest profiles never open the store.

## Consequences

- Positive: consistent encryption, retention, export and deletion; fewer files and I/O; one place to audit.
- Negative: shared schema needs governance; a bug can affect several features; contention must be managed with careful transactions.
- Neutral: some data (e.g. large page snapshots, blobs) may live in content-addressed files referenced from the store.

## Alternatives considered

- **Separate database per feature**: simpler isolation, but inconsistent and heavier. Rejected as default.
- **LevelDB / IndexedDB-style key-value store**: no relational queries or FTS. Rejected.
- **Embedded vector database**: large dependency; deferred until measured need.

## Open questions

- Page-level vs field-level encryption, and performance impact.
- Maximum practical corpus size for brute-force embeddings on low-end hardware.
- Backup/export format for the store.

## Revisit when

Prototype measurements in Phase 2 show contention, size or performance problems.
