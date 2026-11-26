# ADR-0004: MPL-2.0 for Brumel files, BSD-3-Clause for Chromium patches

- Status: Accepted
- Date: 2026-11-26 (approved by the project owner)
- Deciders: @Elgeryy1
- Related: [Licensing](../../legal/LICENSING.md), [ADR-0002](0002-chromium-base-selection.md), [THIRD_PARTY_NOTICES.md](../../../THIRD_PARTY_NOTICES.md)

## Context

Brumel combines three kinds of code: upstream Chromium and its many third-party components (mostly BSD-3-Clause, plus many other licenses), imported ungoogled-chromium patches (BSD-3-Clause), and Brumel's original work. The license for Brumel's own code should keep improvements open, stay compatible with Chromium and with GPL-licensed code that might be combined later, and allow fixes to be upstreamed.

## Decision

- **New files authored for Brumel** (modules, services, WebUI, scripts, tooling) are licensed under the **Mozilla Public License 2.0** (`SPDX-License-Identifier: MPL-2.0`).
- **Patches that modify Chromium-derived files** are licensed under **BSD-3-Clause**, the same as the files they modify, so they can be upstreamed and do not create mixed-license files.
- **Third-party code and imported patches keep their original licenses and notices**; Brumel never relicenses them.
- Every source file and patch carries an SPDX identifier.

## Consequences

- Positive: file-level copyleft keeps Brumel's modules open when redistributed, without affecting Chromium or proprietary OS components; MPL-2.0 is compatible with GPL via its secondary-license provision; same model as Brave.
- Negative: contributors must pay attention to which license a change falls under; two licenses must be explained.
- Neutral: documentation files follow the repository license (MPL-2.0) unless stated otherwise; brand assets may get a separate trademark policy later.

## Alternatives considered

- **BSD-3-Clause everywhere**: maximum compatibility, but allows closed redistribution of Brumel's own modules.
- **GPL-3.0**: strong copyleft (used by Helium), but restricts combinations and is stricter than needed.
- **Apache-2.0**: explicit patent grant, but permissive like BSD and less common in browser projects; GPLv2 incompatibility is irrelevant here but the copyleft goal is not met.

## Revisit when

Brumel adopts a component whose license is incompatible with this scheme, or legal review identifies a problem.
