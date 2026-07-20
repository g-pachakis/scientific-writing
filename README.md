# scientific-writing

Universal evidence-driven workflows for planning, drafting, reviewing, and delivering scientific documents in Pi and Claude Code. Markdown is default. Skills never invent citations, metadata, quotations, data, analyses, results, approvals, or compliance; missing evidence blocks or narrows claims.

## Skills

| Skill | Use |
|---|---|
| `write` | Route only required workflow. |
| `research-planning` | Define contribution, question, argument, and evidence needs. |
| `literature-and-citations` | Search, verify, and manage sources and citations. |
| `data-and-evidence` | Track provenance, analysis, and claim evidence. |
| `study-design-and-reporting` | Apply study-specific methods and reporting checks. |
| `drafting-and-notation` | Draft calibrated prose and keep notation consistent. |
| `figures-and-tables` | Build accessible, traceable visuals and tables. |
| `conclusions-and-abstract` | Derive conclusions, then write abstract last. |
| `review-and-integrity` | Scale scientific, integrity, and submission review. |
| `document-output` | Select and verify Markdown or optional output adapters. |

## Pi

Install:

```bash
pi install git:github.com/g-pachakis/scientific-writing
```

Reload Pi, then use:

```text
/scientific-writing [task]
/skill:write [task]
```

Update or remove:

```bash
pi update git:github.com/g-pachakis/scientific-writing
pi remove git:github.com/g-pachakis/scientific-writing
```

## Claude Code

Inside Claude Code:

```text
/plugin marketplace add g-pachakis/scientific-writing
/plugin install scientific-writing@scientific-writing
```

Restart or reload Claude Code, then use:

```text
/scientific-writing:write
```

Update or remove through `/plugin` → **Manage plugins**, selecting `scientific-writing@scientific-writing`.

## Optional tools

Package has no runtime dependencies. DOCX, LaTeX, plotting, conversion, Python libraries, Pandoc, TeX, Word, and citation-manager tooling are not bundled. Skills use them only when installed and explicitly needed.

## Validate

Requires Python 3 standard library only:

```bash
python3 tests/smoke_test.py --full
```

## License

MIT. See [LICENSE](LICENSE).
