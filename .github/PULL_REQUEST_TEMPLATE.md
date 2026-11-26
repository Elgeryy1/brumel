## Summary

<!-- What does this change and why? -->

## Related

<!-- Issues (Closes #123) and catalog IDs (ENG-001, SHD-012), ADRs. -->

- Issues:
- Catalog IDs:
- ADRs:

## Type of change

- [ ] Documentation
- [ ] Feature catalog (features.json / epics.json)
- [ ] Architecture / ADR
- [ ] Brand / design
- [ ] Scripts / tooling / CI
- [ ] Patch against Chromium
- [ ] Other:

## Checklist

- [ ] `python3 scripts/validate_docs.py` passes
- [ ] If the catalog changed: `python3 scripts/catalog/render_features.py` was run and `docs/product/FEATURES.md` is up to date
- [ ] `python3 -m unittest discover -s tests -v` passes
- [ ] New files carry an SPDX header (MPL-2.0 for Brumel-original files, BSD-3-Clause for patches to Chromium files)
- [ ] All commits are signed off (DCO: `git commit -s`)
- [ ] No Chromium source or other large upstream trees are committed
- [ ] No secrets, personal data or private infrastructure details are included
- [ ] Statuses are honest (nothing planned is described as available)
- [ ] Third-party material is recorded in `THIRD_PARTY_NOTICES.md`

## Security impact

<!-- Does this touch sandboxing, site isolation, permissions, credentials, updates, extensions, IPC or AI tool access? Explain or write "None". -->

## Privacy impact

<!-- Does this add data collection, storage, network requests or sync? Explain or write "None". -->

## AI assistance

<!-- Was a substantial part generated with an AI tool? Disclose briefly (see CONTRIBUTING.md). -->
