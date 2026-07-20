---
name: data-and-evidence
description: Use when scientific files contain data or results, analysis needs provenance, or manuscript claims need traceable evidence and limitation records.
---

# Data and Evidence

Make every material claim traceable. Missing evidence narrows the claim; it never licenses a stronger story.

## Start with an inventory

List each relevant file or dataset with path, format, owner or origin, collection or retrieval date when known, version, access restrictions, and readable/unreadable state. Report unknown or inaccessible inputs explicitly.

Preserve originals. For every transformation or analysis, record:

- input version and selection rules;
- cleaning, exclusions, joins, derivations, and parameter choices;
- code, command, or reproducible procedure;
- output path/version;
- warnings, failures, and deviations.

Never silently alter observations, labels, units, missing values, or exclusions. Never delegate, upload, or expose sensitive unpublished data without explicit user authorization; obey recorded access restrictions.

## Evidence ledger

Create one row per claim:

| Claim | Source | Exact locator | Evidence type | Limitations | Verification state |
|---|---|---|---|---|---|

A source may be a dataset/version, analysis output, figure/table, verified publication, or documented method. Locator must identify the supporting record precisely. Verification state is `verified`, `unverified`, or `blocked`, with reason when not verified.

Before drafting, compare claim strength with design and evidence type. Correlation alone does not establish causation. If raw data, methods, or analysis outputs are absent, use association wording and request the design or analysis evidence needed for a causal claim.

Do not invent analyses, values, provenance, or results. Hand design-specific analysis and reporting checks to `study-design-and-reporting`; hand prose calibration to `drafting-and-notation`.
