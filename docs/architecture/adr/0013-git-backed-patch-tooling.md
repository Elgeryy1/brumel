# ADR-0013: Git-backed patch series tooling

- Status: Accepted (provisional)
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [ADR-0003](0003-patch-based-repository.md), [`patches/README.md`](../../../patches/README.md), [Building](../../development/BUILDING.md), issue [#63](https://github.com/Elgeryy1/brumel/issues/63)

## Context

[ADR-0003](0003-patch-based-repository.md) keeps Brumel's changes as an ordered patch series. Applying a series is only half of the job: on every upstream update, patches that no longer apply have to be fixed in a real checkout and exported back to `patches/` without losing their headers. The tool must work the same way on Windows and Linux, use only tools a Chromium developer already has, and be safe to run on a checkout that contains hours of work.

## Decision

`scripts/patches.py` manages the series with Git inside the Chromium `src` checkout:

- **Base.** The commit the checkout starts from is recorded as `refs/brumel/base`.
- **One commit per patch.** `apply` runs `git apply --index` for each entry of `patches/series` (optionally `--3way`) and commits the result with the trailer `Brumel-Patch: <path>`.
- **Reproducible commits.** Patch commits use a fixed author, committer and date, so the same pin and the same series produce the same commit IDs on every machine. A different commit ID means a different tree.
- **Resumable.** `apply` reads the trailers already on top of the base and continues with the rest of the series. It refuses to run on uncommitted changes, or when the applied commits do not match the start of the series, unless `--reset` is given.
- **Refresh.** After a conflict is resolved and committed (or amended), `refresh` regenerates each patch from its commits with `git diff`. It keeps the existing header and rewrites a file only when its hunks changed. A commit with a new trailer becomes a new patch with a header template, inserted into `series` after the patch before it.
- **Validation without a checkout.** `check` validates the series and the headers defined in `patches/README.md`. CI runs it on every pull request. It also flags added lines that would weaken the sandbox, site isolation, web security, CFI or the V8 sandbox, unless the patch explains itself in a `Security-Note:` header.
- **Plan first.** `apply` and `refresh` print what they would do. They change the checkout or `patches/` only with `--execute`.
- **Nested repositories** (amended 2026-11-27, found in the build spike). A gclient checkout is many Git repositories: `src` ignores its DEPS, such as `v8/` or `third_party/devtools-frontend/src/`, and ungoogled-chromium patches touch them. `apply` splits each patch by the repository that owns each file and commits each part in that repository, with the same trailer and fixed metadata. `src` always gets one commit per patch, empty when the patch does not touch it, so its history stays the ledger of the series. Nested repositories get their own `refs/brumel/base` and are listed in `brumel-patch-repos` in the Git directory of `src`; `--reset` resets them too. `refresh` joins the parts again with the repository prefix restored, and treats two diffs that differ only in file order as unchanged.

## Consequences

- Positive: developers work with ordinary Git (rebase, amend, bisect) in the checkout, and the repository only ever sees patch files. No dependency beyond Git and the Python standard library.
- Positive: the patch budget (patches, modified upstream files, changed lines) comes from `patches.py stats`, which is the metric [Upstream Strategy](../UPSTREAM_STRATEGY.md) asks for.
- Negative: `refresh` rewrites imported ungoogled-chromium patches in Git's diff format the first time they change, which makes the diff against the upstream file noisier once.
- Negative: a conflict in a nested repository is resolved and committed there, and a patch that is new in a nested repository also needs a commit with the same trailer in `src` (it may be empty). `refresh` refuses a nested commit with no matching commit in `src`. `gclient sync` moves nested repositories back to their pinned commits, so run `apply` again after a sync.
- Negative: committing in a Chromium checkout is slower than in a small repository. This is acceptable for a series of tens to low hundreds of patches. To be measured in the build spike ([#61](https://github.com/Elgeryy1/brumel/issues/61)).

## Alternatives considered

- **quilt.** The format ungoogled-chromium uses. It is not available by default on Windows, and its refresh model is separate from the Git workflow developers use anyway. The series file stays quilt-compatible, so quilt remains usable by hand.
- **`git am` with mbox patches.** It keeps authorship and messages, but Brumel's header lives in the patch file, not in commit messages. Converting between the two adds a fragile step.
- **Keeping a long-lived fork branch instead of patches.** Rejected by [ADR-0003](0003-patch-based-repository.md).

## Revisit when

- The series grows past a few hundred patches and apply or refresh time becomes a bottleneck.
- Imported ungoogled-chromium patches need to stay byte-identical to their upstream files.
