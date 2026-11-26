# Good first issues

This guide explains how starter work is selected and labeled, what kind of starter
work exists while Brumel is in **Pre-development**, and how to claim it.

## How issues are labeled

| Label | Meaning |
|---|---|
| `good first issue` | Well-scoped, low-risk, with enough context that a newcomer can finish it without deep knowledge of Chromium or the project. |
| `help wanted` | Maintainers would welcome outside help. It may need more experience than a good first issue. |
| `type:docs`, `type:research`, `type:task` | The kind of work. |
| `module:*` | The module involved (for example `module:engine`, `module:shield`). |

A maintainer adds `good first issue` only when the issue:

1. describes the expected outcome and how it will be reviewed;
2. points to the files or documents involved;
3. needs no access to private infrastructure, secrets or a Chromium checkout;
4. can reasonably be finished in a few hours;
5. has no unresolved design decision blocking it.

## Starter work available now

There is no browser code yet, but there is real work that improves the project.

### Documentation

- Fix unclear wording, typos or inconsistencies between documents. For example, a
  phase name that differs between the roadmap and a feature entry.
- Improve examples and diagrams in architecture documents.
- Check that every document links correctly. `python3 scripts/validate_docs.py`
  helps here.

### Research verification

- **Verify cells in the [feature matrix](../product/FEATURE_MATRIX.md).** Each
  comparison claim about another browser should have a source (official docs,
  release notes, source code) and an access date. Pick a row, verify it, and submit
  corrections with citations.
- Find primary sources for the "evidence" field of catalog entries. User complaints
  on public bug trackers, published studies and specifications are especially
  valuable.
- Check license statements in [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md)
  and [LICENSING.md](../legal/LICENSING.md) against the upstream projects.

### Brand and design feedback

- Review the [logo proposals](../../assets/branding/README.md) at real sizes (16 ×
  16, 32 × 32, taskbar, tab strip) on light and dark backgrounds, and report
  legibility problems.
- Check color contrast of the provisional palette against WCAG 2.2 in
  [DESIGN_SYSTEM.md](../design/DESIGN_SYSTEM.md).

### Feature catalog refinement

- Improve **acceptance criteria** so that they are testable. "Feels fast" is not
  testable. "Restores 200 tabs with at most N loaded within T seconds on the
  reference hardware" is.
- Spot duplicates and suggest `duplicate_of` links, without deleting entries.
- Propose missing risks (security, privacy) for a feature.

Remember to run `python3 scripts/catalog/render_features.py` after editing
`features.json`.

### Repository tooling

- Add unit tests for edge cases in [`scripts/validate_docs.py`](../../scripts/validate_docs.py).
- Improve error messages in the scripts.

## How to claim an issue

1. Comment on the issue saying you would like to work on it, and roughly when you
   expect to open a pull request.
2. A maintainer assigns it to you. Please wait for that before starting larger work.
3. If you can no longer work on it, say so. That is completely fine. Issues without
   activity for about two weeks after assignment may be released for others.
4. Open a pull request that references the issue (`Closes #N`) and follows
   [CONTRIBUTING.md](../../CONTRIBUTING.md), including DCO sign-off.

Questions? Ask in [GitHub Discussions](https://github.com/Elgeryy1/brumel/discussions)
(Q&A category).
