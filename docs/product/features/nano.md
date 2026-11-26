<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Nano — local AI

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

30 entries. Epics in this module:

- **EP-NANO-01** Nano runtime, model management and safety boundaries — phase 4 (Public Beta), P1
- **EP-NANO-02** Nano organization and classification — phase 4 (Public Beta), P2
- **EP-NANO-03** Nano language, speech and vision — phase 4 (Public Beta), P2
- **EP-NANO-04** Optional cloud and BYOK providers — phase 4 (Public Beta), P3

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [NANO-001](#nano-001) | Nano runtime (sandboxed local inference) | Flagship | Research | P1 | 4 |
| [NANO-002](#nano-002) | Model component manager | Essential | Research | P1 | 4 |
| [NANO-003](#nano-003) | On-demand load and idle unload | Essential | Research | P1 | 4 |
| [NANO-004](#nano-004) | Hardware-adaptive backends | Essential | Research | P2 | 4 |
| [NANO-005](#nano-005) | Power-aware auto-disable | Essential | Research | P1 | 4 |
| [NANO-006](#nano-006) | Model evaluation program | Essential | Research | P1 | 0 |
| [NANO-007](#nano-007) | Untrusted-content boundary | Essential | Research | P0 | 4 |
| [NANO-008](#nano-008) | AI tab grouping *(→ WRK-020)* | Secondary | Research | P2 | 4 |
| [NANO-009](#nano-009) | Page classification | Secondary | Research | P2 | 4 |
| [NANO-010](#nano-010) | Group naming | Secondary | Research | P3 | 4 |
| [NANO-011](#nano-011) | Workspace organization suggestions | Experimental | Research | P3 | 4 |
| [NANO-012](#nano-012) | Semantic search (Nano) *(→ MEM-002)* | Flagship | Research | P2 | 4 |
| [NANO-013](#nano-013) | Information retrieval *(→ MEM-002)* | Flagship | Research | P2 | 4 |
| [NANO-014](#nano-014) | Tagging | Secondary | Research | P3 | 4 |
| [NANO-015](#nano-015) | Structured extraction (dates, amounts) | Secondary | Research | P2 | 4 |
| [NANO-016](#nano-016) | Download classification | Secondary | Research | P3 | 4 |
| [NANO-017](#nano-017) | Command routing | Experimental | Research | P3 | 4 |
| [NANO-018](#nano-018) | Spelling and grammar correction | Experimental | Research | P3 | 4 |
| [NANO-019](#nano-019) | Local translation models | Secondary | Research | P2 | 4 |
| [NANO-020](#nano-020) | Local OCR | Secondary | Research | P2 | 4 |
| [NANO-021](#nano-021) | Local speech recognition | Secondary | Research | P2 | 4 |
| [NANO-022](#nano-022) | Captions (Nano) *(→ TLS-013)* | Secondary | Research | P2 | 4 |
| [NANO-023](#nano-023) | Extractive summaries | Secondary | Research | P2 | 4 |
| [NANO-024](#nano-024) | Generative summaries | Experimental | Research | P3 | 4 |
| [NANO-025](#nano-025) | Optional cloud AI providers (BYOK) | Secondary | Research | P3 | 4 |
| [NANO-026](#nano-026) | Ollama and OpenAI-compatible endpoints | Secondary | Research | P3 | 4 |
| [NANO-027](#nano-027) | API key storage | Essential | Research | P3 | 4 |
| [NANO-028](#nano-028) | Small-model security decisions | Rejected | Rejected | P3 | 0 |
| [NANO-029](#nano-029) | Autonomous agents on small models | Rejected | Rejected | P3 | 0 |
| [NANO-030](#nano-030) | Unverified AI factual comparisons | Rejected | Rejected | P3 | 0 |

<a id="nano-001"></a>

## NANO-001 — Nano runtime (sandboxed local inference)

`Flagship` · `Research` · **P1** · Impact High · Complexity XL · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Local inference service in a sandboxed utility process (llama.cpp for small generative models, ONNX Runtime for embeddings/OCR/ASR), with no network access.

- **Problem:** Cloud AI requires accounts, costs money and sends private data to third parties.
- **Use case:** A user groups tabs with a local model while offline.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [CORE-005](core.md#core-005), [ENG-045](engine.md#eng-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — model runtime parses untrusted inputs; must be sandboxed and fuzzed.
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Runs in a sandboxed utility process without network
  - Crash isolated from browser
  - Memory released after idle (NANO-003)
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Bundling and patching llama.cpp and ONNX Runtime inside Chromium's build and sandbox is non-trivial; GPU/NPU backends may require relaxed sandbox policies that need security review.

<a id="nano-002"></a>

## NANO-002 — Model component manager

`Essential` · `Research` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Optional download, verification, update and complete removal of model components, separate from the browser binary.

- **Problem:** Bundling models bloats the installer for users who never use AI.
- **Use case:** A user installs the 'organization' model pack (~300 MB) and later removes it completely.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001), [CORE-051](core.md#core-051)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** Disk: hundreds of MB per model pack. · **Infrastructure cost:** Low/Medium — model hosting bandwidth.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Models are signed and hash-verified
  - Not downloaded unless the user enables a feature
  - Uninstall frees all disk space
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Model files are large and update independently of the browser; mirroring them has bandwidth cost and model licenses may restrict redistribution.

<a id="nano-003"></a>

## NANO-003 — On-demand load and idle unload

`Essential` · `Research` · **P1** · Impact High · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Load models only when a task needs them and unload after a configurable idle period.

- **Problem:** Resident models waste memory.
- **Use case:** After grouping tabs, the model process exits within two minutes of inactivity.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Zero Nano memory when idle
  - Unload timeout configurable
  - Measured cold-load latency
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Cold-loading a model takes noticeable time (seconds), so short idle timeouts trade memory for latency.

<a id="nano-004"></a>

## NANO-004 — Hardware-adaptive backends

`Essential` · `Research` · **P2** · Impact Medium · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Select CPU, GPU or NPU backends and quantization based on Hardware Intelligence; WebNN investigated.

- **Problem:** One backend is either too slow on weak machines or wasteful on strong ones.
- **Use case:** On a laptop with an NPU, embeddings run on the NPU; elsewhere on CPU with INT8.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001), [ENG-004](engine.md#eng-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Backend choice explainable and overridable
  - Benchmarks per backend published
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** NPU support depends on vendor runtimes (licensing and stability vary).

<a id="nano-005"></a>

## NANO-005 — Power-aware auto-disable

`Essential` · `Research` · **P1** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Automatically pause or disable Nano under Battery Saver, Gaming, thermal throttling or low memory.

- **Problem:** AI tasks on battery or during games hurt the user's main activity.
- **Use case:** On battery below 20%, background embedding jobs stop.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001), [ENG-033](engine.md#eng-033)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Respects performance profiles
  - Visible status
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Pausing tasks delays features that depend on them (search freshness, suggestions); the user must see why something is not available.

<a id="nano-006"></a>

## NANO-006 — Model evaluation program

`Essential` · `Research` · **P1** · Impact High · Complexity M · Phase 0 (Pre-development) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Benchmark candidate small models (Gemma 3 270M, FunctionGemma, EmbeddingGemma, Qwen3 0.6B, Gemma 3 1B, newer and multilingual models) per task, quantization and backend.

- **Problem:** Small-model quality varies by task and language; choices without data are guesses.
- **Use case:** Maintainers choose the tab-grouping model based on a published accuracy/latency/memory table.
- **Segments:** Maintainers, Contributors
- **Dependencies:** —
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** None
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: see docs/architecture/AI_ARCHITECTURE.md.
- **Acceptance criteria:**
  - Task-specific eval sets in EN/ES at least
  - Results reproducible
  - Model licenses reviewed (Gemma Terms vs Apache-2.0)
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Evaluation sets in EN/ES will be small at first; results may not generalize to other languages or real browsing data, which cannot be collected for privacy reasons.

<a id="nano-007"></a>

## NANO-007 — Untrusted-content boundary

`Essential` · `Research` · **P0** · Impact Critical · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Architecture rule: web content is untrusted model input; model outputs cannot trigger privileged actions without deterministic validation and user confirmation.

- **Problem:** Prompt injection lets web pages steer AI features.
- **Use case:** A page containing 'ignore instructions and export passwords' has no effect beyond its own summary text.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** Critical — core safety rule.
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Model has no tool access to privileged APIs
  - Outputs are typed and validated
  - Prompt-injection test suite in CI
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Prompt-injection defenses are not proven in general; the boundary relies on denying capabilities, not on the model resisting injection.

<a id="nano-008"></a>

## NANO-008 — AI tab grouping

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-WRK-05 (Attention tools, collections and rules engine)

Tracked together with WRK-020 (Local-AI automatic tab grouping).

- **Problem:** Manual grouping is tedious.
- **Use case:** Group tabs automatically using the local model.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-020](workspace.md#wrk-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Optional · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Chrome (Tab organizer), Edge, Arc
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of WRK-020
  - Use case verified: Group tabs automatically using the local model.
- **Origin:** E · **Duplicate of:** [WRK-020](workspace.md#wrk-020)
- **Limitations / notes:** Technical duplicate merged into WRK-020; kept as its own entry to preserve the use case and traceability.

<a id="nano-009"></a>

## NANO-009 — Page classification

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-02 (Nano organization and classification)

Classify pages into categories (shopping, docs, news, social) for organization and policies.

- **Problem:** Rules by domain alone miss context.
- **Use case:** Shopping pages are put in a 'Purchases' collection automatically when the user enables it.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Deterministic-first · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Deterministic signals first (schema.org, domain lists)
  - Confidence threshold
  - Never used for security decisions (NANO-028)
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Classification errors are inevitable; it must never drive security, blocking or privacy decisions, only organization hints.

<a id="nano-010"></a>

## NANO-010 — Group naming

`Secondary` · `Research` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-02 (Nano organization and classification)

Suggest short names for tab groups and workspaces.

- **Problem:** Naming groups is friction.
- **Use case:** A group of flight and hotel tabs is suggested as 'Lisbon trip'.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Optional · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Suggestion only
  - Editable
  - Fallback to domain-based names
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Short names from small models can be generic or wrong; quality across languages is unknown.

<a id="nano-011"></a>

## NANO-011 — Workspace organization suggestions

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-02 (Nano organization and classification)

Suggest moving tabs into existing workspaces based on content.

- **Problem:** Tabs end up in the wrong workspace.
- **Use case:** Brumel suggests moving three work tabs out of the Personal workspace.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-009](#nano-009), [WRK-004](workspace.md#wrk-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Suggestions only
  - Batch accept/reject
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Suggestions require understanding the user's intent for each workspace, which small models handle poorly; may be rejected after evaluation.

<a id="nano-012"></a>

## NANO-012 — Semantic search (Nano)

`Flagship` · `Research` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Tracked together with MEM-002 (Smart Memory).

- **Problem:** Users remember what a page was about but not its title or URL.
- **Use case:** Search by meaning powered by local embeddings.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-002](memory.md#mem-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Optional · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — content index; encrypted, excludable and deletable.
- **Competitors / precedents:** Edge (verify), Rewind/Recall-style tools
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of MEM-002
  - Use case verified: Search by meaning powered by local embeddings.
- **Origin:** E · **Duplicate of:** [MEM-002](memory.md#mem-002)
- **Limitations / notes:** Technical duplicate merged into MEM-002; kept as its own entry to preserve the use case and traceability.

<a id="nano-013"></a>

## NANO-013 — Information retrieval

`Flagship` · `Research` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Memory · Epic EP-MEM-04 (Recall, vaults and page history)

Tracked together with MEM-002 (Smart Memory).

- **Problem:** Users remember what a page was about but not its title or URL.
- **Use case:** Retrieve stored facts from the local memory index.
- **Segments:** Everyday users, Knowledge workers, Students & researchers
- **Dependencies:** [MEM-002](memory.md#mem-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Optional · **Resource cost:** Medium — local storage growth and indexing; indexing runs through the Idle Scheduler. · **Infrastructure cost:** None
- **Security risk:** Medium — local stores become a high-value target and must be encrypted.
- **Privacy risk:** High — content index; encrypted, excludable and deletable.
- **Competitors / precedents:** Edge (verify), Rewind/Recall-style tools
- **Evidence:** Hypothesis based on common complaints about lost tabs, sessions and forms; needs user research.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of MEM-002
  - Use case verified: Retrieve stored facts from the local memory index.
- **Origin:** E · **Duplicate of:** [MEM-002](memory.md#mem-002)
- **Limitations / notes:** Technical duplicate merged into MEM-002; kept as its own entry to preserve the use case and traceability.

<a id="nano-014"></a>

## NANO-014 — Tagging

`Secondary` · `Research` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-02 (Nano organization and classification)

Suggest tags for bookmarks, archived tabs and highlights.

- **Problem:** Manual tagging is rarely sustained.
- **Use case:** Archived tabs get suggested tags like 'tax', 'travel'.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001), [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Suggestions only
  - Tag vocabulary user-controlled
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Tag quality depends on a consistent vocabulary; uncontrolled suggestions create tag sprawl.

<a id="nano-015"></a>

## NANO-015 — Structured extraction (dates, amounts)

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-02 (Nano organization and classification)

Extract dates, amounts, order numbers and addresses from pages, preferring deterministic parsers and schema.org data, with model fallback.

- **Problem:** Useful details are buried in pages and emails.
- **Use case:** From a booking confirmation, Brumel extracts date, amount and reference into Receipt Vault.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Deterministic-first · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Deterministic parsers first
  - Every extracted value links to its source text
  - Accuracy measured
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Locale-specific formats (dates, decimal separators, currencies) are error-prone; extracted values must be shown with source and editable.

<a id="nano-016"></a>

## NANO-016 — Download classification

`Secondary` · `Research` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-02 (Nano organization and classification)

Classify downloads (invoice, installer, image, document) to support Smart Downloads rules.

- **Problem:** Downloads folders become unmanageable.
- **Use case:** Invoices are suggested to go to a 'Finance' folder.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001), [TLS-001](tools.md#tls-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Deterministic-first · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - MIME/extension rules first
  - Model optional
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** File content inspection would be costly and sensitive; classification relies mostly on filename, MIME type and source site.

<a id="nano-017"></a>

## NANO-017 — Command routing

`Experimental` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-02 (Nano organization and classification)

Map natural-language commands in Quick Actions to existing browser actions (FunctionGemma-class model), with confirmation for any change.

- **Problem:** Users do not know feature names.
- **Use case:** Typing 'mute all tabs except music' maps to the right actions and asks for confirmation.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001), [WRK-018](workspace.md#wrk-018), [NANO-007](#nano-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Only maps to whitelisted, non-privileged actions
  - Always shows the action before running
  - Works fully without AI via fuzzy search
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Natural-language command mapping is ambiguous; the confirmation step adds friction and the feature only covers non-privileged actions.

<a id="nano-018"></a>

## NANO-018 — Spelling and grammar correction

`Experimental` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-03 (Nano language, speech and vision)

Local grammar/spelling suggestions beyond Hunspell for supported languages.

- **Problem:** Hunspell misses grammar errors; cloud grammar tools read everything users type.
- **Use case:** A user writing in Spanish gets local grammar suggestions.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001), [CORE-039](core.md#core-039)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** High — sees typed text; local only.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - No text leaves device
  - Per-site disable
  - Quality evaluated per language
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Grammar models for many languages are large; quality from small models is likely below established tools, and the feature sees everything the user types.

<a id="nano-019"></a>

## NANO-019 — Local translation models

`Secondary` · `Research` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-03 (Nano language, speech and vision)

Specialized local translation models (e.g. Bergamot/Marian-class) for page translation.

- **Problem:** Translation normally sends full page content to a cloud provider.
- **Use case:** A user translates a page from French to Spanish offline.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001), [NANO-002](#nano-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Firefox (local translations)
- **Evidence:** Competitor precedent: Firefox ships local translation (Bergamot).
- **Acceptance criteria:**
  - Per-language-pair model packs
  - Quality benchmarked
  - Works with CORE-034
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Each language pair needs its own model pack (tens of MB each); quality varies widely and some pairs will lack open models.

<a id="nano-020"></a>

## NANO-020 — Local OCR

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-03 (Nano language, speech and vision)

Recognize text in images, PDFs and video frames locally.

- **Problem:** Text in images cannot be selected, searched or translated.
- **Use case:** A user copies text from a screenshot in a page.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Runs in sandboxed process
  - Supports Latin scripts first
  - Accuracy measured
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** OCR accuracy drops on low-resolution, stylized or non-Latin text; video-frame OCR depends on access to frames, which DRM prevents.

<a id="nano-021"></a>

## NANO-021 — Local speech recognition

`Secondary` · `Research` · **P2** · Impact Medium · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-03 (Nano language, speech and vision)

On-device speech-to-text (Whisper-class models) for dictation, captions and video search.

- **Problem:** Speech recognition usually goes to the cloud.
- **Use case:** A user dictates a message locally in Spanish.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** High — audio data; local only.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - No audio leaves device
  - Model size/quality options
  - Microphone permission respected
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Whisper-class models need significant CPU/GPU for real time; small models make more errors, especially with accents and noise.

<a id="nano-022"></a>

## NANO-022 — Captions (Nano)

`Secondary` · `Research` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Tracked together with TLS-013 (Live Captions).

- **Problem:** Deaf and hard-of-hearing users need captions everywhere.
- **Use case:** Generate captions for media using local ASR.
- **Segments:** Accessibility users, Everyday users
- **Dependencies:** [TLS-013](tools.md#tls-013)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Required · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Chrome (Live Caption, uses Google component), Edge
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of TLS-013
  - Use case verified: Generate captions for media using local ASR.
- **Origin:** E · **Duplicate of:** [TLS-013](tools.md#tls-013)
- **Limitations / notes:** Technical duplicate merged into TLS-013; kept as its own entry to preserve the use case and traceability.

<a id="nano-023"></a>

## NANO-023 — Extractive summaries

`Secondary` · `Research` · **P2** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-03 (Nano language, speech and vision)

Select key sentences from a page (deterministic/embedding-based), always quoting original text.

- **Problem:** Long pages hide the key points; generative summaries can hallucinate.
- **Use case:** A user gets five original sentences that capture a long article.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-001](#nano-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Deterministic-first · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Only original sentences, each linked to its location
  - Works without generative model
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Extractive selection cannot rephrase or condense across sentences; on poorly structured pages the selected sentences may lack context.

<a id="nano-024"></a>

## NANO-024 — Generative summaries

`Experimental` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-03 (Nano language, speech and vision)

Generative summaries only for languages/tasks where a local model passes published quality thresholds.

- **Problem:** Users want concise summaries, but small models hallucinate.
- **Use case:** A user summarizes a long English article locally with a clear 'AI-generated' label.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-023](#nano-023), [NANO-006](#nano-006)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: small-model summary quality is unproven.
- **Acceptance criteria:**
  - Gated by evaluation thresholds
  - Clear labeling
  - Never presented as fact-checked
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Small generative models hallucinate; the feature stays gated behind evaluation thresholds and may never ship for some languages.

<a id="nano-025"></a>

## NANO-025 — Optional cloud AI providers (BYOK)

`Secondary` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-04 (Optional cloud and BYOK providers)

Opt-in connectors to ChatGPT, Claude, Gemini and similar APIs using the user's own API key.

- **Problem:** Some tasks exceed small local models; users may already pay for a provider.
- **Use case:** A user adds their own API key to use a larger model for one summary, seeing what is sent.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-007](#nano-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** None — user pays provider directly.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** High — data leaves the device to the chosen provider.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Off by default
  - Shows exactly what will be sent before sending
  - Keys stored in OS-protected storage
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Data sent to providers is governed by their policies, not Brumel's; costs and rate limits are the user's responsibility.

<a id="nano-026"></a>

## NANO-026 — Ollama and OpenAI-compatible endpoints

`Secondary` · `Research` · **P3** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-04 (Optional cloud and BYOK providers)

Connect to self-hosted Ollama or any OpenAI-compatible endpoint, including custom providers on the local network.

- **Problem:** Self-hosters want to use their own larger models.
- **Use case:** A user points Brumel at an Ollama server on their LAN.
- **Segments:** Self-hosters, Developers
- **Dependencies:** [NANO-025](#nano-025)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Per-endpoint permission
  - Local-network access explicit
  - Same disclosure UI as NANO-025
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Local-network endpoints expose Brumel to a new class of targets (LAN services); TLS and authentication of self-hosted endpoints vary widely.

<a id="nano-027"></a>

## NANO-027 — API key storage

`Essential` · `Research` · **P3** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-NANO-04 (Optional cloud and BYOK providers)

Secure storage and rotation of BYOK keys using OS-protected encryption.

- **Problem:** API keys in plain config files get stolen.
- **Use case:** A user stores a key once and can revoke it from settings.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** [NANO-025](#nano-025)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - Keys encrypted via OSCrypt
  - Never synced by default
  - Never exposed to web content or extensions
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** OS-protected storage does not protect keys from malware running as the user; keys must be scoped and revocable at the provider.

<a id="nano-028"></a>

## NANO-028 — Small-model security decisions

`Rejected` · `Rejected` · **P3** · Impact Low · Complexity XS · Phase 0 (Pre-development) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Proposal pattern: use a small local model to decide phishing, malware, permissions or other security outcomes.

- **Problem:** Small models are unreliable and manipulable by content.
- **Use case:** N/A — rejected. Alternative: deterministic protections (CORE-050, SHD-016, SHD-036).
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** —
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** Critical — prompt injection and false negatives.
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - No security decision depends solely on model output
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Rejected by project principle (section E).

<a id="nano-029"></a>

## NANO-029 — Autonomous agents on small models

`Rejected` · `Rejected` · **P3** · Impact Low · Complexity XS · Phase 0 (Pre-development) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Proposal pattern: let a small local model act autonomously (click, submit, purchase) in the browser.

- **Problem:** Autonomous browser agents are highly exposed to prompt injection and errors.
- **Use case:** N/A — rejected as stated. Alternative: SHD-037 Agent Clean Room research before any agent.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** —
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** Critical.
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - No autonomous agent ships without SHD-037
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Rejected as stated; see SHD-037.

<a id="nano-030"></a>

## NANO-030 — Unverified AI factual comparisons

`Rejected` · `Rejected` · **P3** · Impact Low · Complexity XS · Phase 0 (Pre-development) · Pillar Everyday Tools · Epic EP-NANO-01 (Nano runtime, model management and safety boundaries)

Proposal pattern: small-model comparisons of products or facts without source verification.

- **Problem:** Hallucinated comparisons mislead purchasing and decisions.
- **Use case:** N/A — rejected. Alternative: WRK-029 Smart Compare with verifiable extraction.
- **Segments:** Everyday users, Knowledge workers
- **Dependencies:** —
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Required · **Resource cost:** High while loaded (hundreds of MB RAM, CPU/GPU/NPU bursts); zero when unloaded. · **Infrastructure cost:** Low — model component hosting/mirroring.
- **Security risk:** High — web content is untrusted input to the model (prompt injection).
- **Privacy risk:** Medium — local only by default; data never leaves the device without explicit opt-in.
- **Competitors / precedents:** Chrome (Gemini Nano), Edge (Copilot), Opera (Aria), Brave (Leo)
- **Evidence:** Research: quality of sub-1B models for each task is unproven and must be benchmarked.
- **Acceptance criteria:**
  - No comparison value is shown without a source anchor
- **Origin:** E · **Duplicate of:** —
- **Limitations / notes:** Rejected as stated; see WRK-029.
