# ADR-0009: Local-first, end-to-end encrypted sync

- Status: Proposed
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [Sync Architecture](../SYNC_ARCHITECTURE.md), [Privacy](../../privacy/PRIVACY.md), [Threat Model §5.6](../../security/THREAT_MODEL.md)

## Context

Google restricted Chrome Sync for third-party Chromium builds in 2021, so Brumel needs its own sync. Users expect bookmarks, tabs, spaces and settings across devices, but Brumel's principles forbid mandatory accounts and require that servers cannot read user data. The project has no budget for large infrastructure and must not depend on the maintainer's personal hardware.

## Decision (proposed)

- **Local-first**: devices hold full copies and work offline; servers are relays/mailboxes.
- **End-to-end encryption in clients**; the server stores ciphertext and minimal metadata.
- **Per-data-type CRDT/LWW merge** over an operation log with periodic encrypted snapshots.
- **Device pairing** via QR code with short authentication string, or a recovery code.
- **Transport**: HTTPS relay for encrypted batches; WebRTC data channels for direct device-to-device transfer with TURN fallback.
- **Server**: Supabase Free (PostgreSQL with Row Level Security) as the candidate hosted relay for early phases; a **self-hostable Docker reference server** implementing the same protocol.
- **Password and passkey sync: Deferred** pending a dedicated security review.
- Sync is optional; the browser is fully functional without it.

## Consequences

- Positive: privacy by construction; low server cost; resilience to server loss; self-hosting.
- Negative: no server-side recovery if users lose all devices and the recovery code; protocol and crypto design is demanding and requires expert review; free-tier quotas limit scale.
- Neutral: Supabase can be replaced because the server is a thin, protocol-defined relay.

## Alternatives considered

- **Server-readable sync** (traditional): simpler, unacceptable for privacy.
- **Reuse Chromium sync protocol with a custom server** (as some forks do): possible, but Chromium's protocol is designed around Google's server model; E2EE beyond custom passphrase mode needs changes. Studied, not chosen.
- **Pure peer-to-peer without relay**: fails when devices are rarely online at the same time.

## Revisit when

Cryptographic review recommends a different design (e.g. MLS), or free-tier limits make Supabase unsuitable.
