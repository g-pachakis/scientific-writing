# Scientific Writing

Evidence-driven workflows for planning, drafting, reviewing, and delivering scientific documents. This package works with both [Pi](https://pi.dev) and Claude Code, loading only the guidance relevant to each request.

## What it covers

- Research questions, contribution, argument structure, and evidence planning
- Literature search, source verification, citations, and bibliographies
- Data provenance, study design, statistical reporting, and reproducibility
- Evidence-calibrated drafting, notation, figures, tables, conclusions, and abstracts
- Scientific integrity review and Markdown, DOCX, or LaTeX delivery

## Included skills

| Skill | Purpose |
|---|---|
| `write` | Select the smallest relevant workflow. |
| `research-planning` | Define contribution, question, argument, and evidence needs. |
| `literature-and-citations` | Search, verify, and manage sources and citations. |
| `data-and-evidence` | Track provenance, analysis, and claim evidence. |
| `study-design-and-reporting` | Apply study-specific methods and reporting checks. |
| `drafting-and-notation` | Draft calibrated prose and keep notation consistent. |
| `figures-and-tables` | Build accessible, traceable visuals and tables. |
| `conclusions-and-abstract` | Derive conclusions, then write the abstract last. |
| `review-and-integrity` | Scale scientific, integrity, and submission review. |
| `document-output` | Select and verify Markdown or optional output formats. |

## Installation

### Pi

```bash
pi install git:github.com/g-pachakis/scientific-writing
```

Restart or reload Pi, then use:

```text
/scientific-writing [task]
/skill:write [task]
```

Update or remove:

```bash
pi update git:github.com/g-pachakis/scientific-writing
pi remove git:github.com/g-pachakis/scientific-writing
```

### Claude Code

Run inside Claude Code:

```text
/plugin marketplace add g-pachakis/scientific-writing
/plugin install scientific-writing@scientific-writing
```

Restart or reload Claude Code, then use:

```text
/scientific-writing:write [task]
```

Update or remove through `/plugin` → **Manage plugins**, selecting `scientific-writing@scientific-writing`.

## Examples

```text
/scientific-writing Plan the argument and evidence map for this manuscript.
/scientific-writing Revise this discussion without overstating causality.
/scientific-writing Check these results against the study design and reporting requirements.
/scientific-writing Review this draft for evidence, notation, integrity, and submission readiness.
```

## Safety and limitations

The skills do not invent citations, metadata, quotations, data, analyses, results, approvals, or compliance. Missing evidence is reported or used to narrow claims. Generated scientific work still requires project-specific verification and appropriate expert review.

## Optional tools

Package has no runtime dependencies. DOCX, LaTeX, plotting, conversion, Python libraries, Pandoc, TeX, Word, and citation-manager tools are not bundled; workflows use them only when available and explicitly needed.

## Verification

Requires only Python 3 standard library:

```bash
python3 tests/smoke_test.py --full
```

## License

MIT. See [LICENSE](LICENSE).
