# ADR-0008: Local AI runtime — llama.cpp and ONNX Runtime in a sandboxed process

- Status: Proposed
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [AI Architecture](../AI_ARCHITECTURE.md), [Threat Model §5.4](../../security/THREAT_MODEL.md)

## Context

Brumel Nano provides optional, free, local AI for browser tasks (grouping, semantic search, extraction, OCR, ASR, translation). Chrome's built-in on-device model stack relies on Google-provided models and components that Brumel cannot redistribute. Brumel needs runtimes that are open source, efficient on CPU, can use GPUs and NPUs where available, and can run inside a strict sandbox.

## Decision (proposed)

- **llama.cpp** (MIT) for small generative models in GGUF format.
- **ONNX Runtime** (MIT as last verified; its GitHub repository location changed, so license and source must be re-verified before adoption) for embeddings, OCR, ASR and translation models, with execution providers selected per platform (DirectML on Windows; CUDA/ROCm/OpenVINO/vendor NPU providers as Research).
- Both run inside a **dedicated sandboxed utility process** with **no network access** and no file-system access beyond model file handles passed by the browser process.
- Models are **downloadable components** with signed manifests and pinned hashes; never bundled in the installer.
- The process is started on demand by the Idle Scheduler and exits after an idle timeout.
- Model choice per task is decided by published benchmarks, not by this ADR.

## Consequences

- Positive: permissive licenses; strong CPU performance; hardware acceleration paths; isolation contains runtime bugs.
- Negative: two runtimes increase binary size and maintenance; NPU support is fragmented; model-file parsers are attack surface (mitigated by sandbox and hash pinning).
- Neutral: WebNN may later offer a standardized acceleration path.

## Alternatives considered

- **Single runtime (only ONNX Runtime)**: simpler, but generative small-model performance and quantization ecosystem are stronger in llama.cpp today (to be benchmarked).
- **Single runtime (only llama.cpp)**: weaker for OCR/ASR/embedding model variety.
- **Chrome's on-device model service**: depends on Google-provided components; not redistributable.
- **Cloud-only AI**: violates local-first and free goals; kept only as opt-in BYOK.

## Revisit when

Benchmarks show one runtime suffices, or WebNN/platform ML APIs mature enough to replace bundled runtimes.
