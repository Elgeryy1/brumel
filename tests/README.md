# Tests

Brumel has no browser code yet, so the tests here cover the **repository tooling**
in [`scripts/`](../scripts/README.md). They use Python's built-in `unittest` and
need no third-party packages.

```sh
python3 -m unittest discover -s tests -v
```

| Test file | Covers |
|---|---|
| `test_validate_docs.py` | Link checking and feature-catalog validation in `scripts/validate_docs.py`, using small synthetic fixtures |
| `test_upstream_issue.py` | Tracking-issue rendering for the upstream check, including rejection of untrusted version strings |
| `test_overlay.py` | `overlay.py` source checks and sync (new, changed, stale files; refusing a directory it does not own) |
| `test_bench_harness.py` | Benchmark harness statistics, corpus, process parsing and the local beacon server (no browser is launched) |
| `test_build_tooling.py` | `fetch.py` plans and pin validation, `patches.py` checks and an apply/refresh round trip on a tiny Git repository, and the `build.py` profile guard. Nothing is downloaded. |

CI runs these tests on every push and pull request (see
[`.github/workflows/docs-ci.yml`](../.github/workflows/docs-ci.yml)).

Browser-level testing will come later: Chromium's own unit and browser tests,
Brumel patch regression tests, web compatibility and isolation tests, and the
benchmark harness. That strategy is described in
[BUILDING.md](../docs/development/BUILDING.md) and
[BENCHMARKS.md](../docs/benchmarks/BENCHMARKS.md), and it will live in this
directory once the technical foundation exists.
