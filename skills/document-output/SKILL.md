---
name: document-output
description: Use when selecting or producing Markdown, DOCX, LaTeX, or venue-template output for a scientific document.
---

# Document Output

Keep reviewed Markdown as default portable source. Choose another adapter only from explicit user, collaborator, repository, or venue requirements.

## Select output

- **Markdown:** default for drafting, review, portability, and version control.
- **DOCX:** use when editing or submission requires Word-compatible output.
- **LaTeX:** use when the project or venue requires TeX sources.
- **Venue template:** use the real user-provided or authoritative current template; do not recreate one from memory.

Preserve headings, equations, citations, cross-references, figures, tables, captions, alt text, metadata, and tracked unresolved markers through conversion.

## Capability boundary

Pandoc, Python document libraries, TeX engines, desktop Word, citation managers, and converters are optional capabilities, not package dependencies. Detect availability before choosing a command. If a required tool is absent, keep the Markdown source and provide the exact conversion or manual step; never claim an artifact was generated.

Do not synthesize linked citation-manager fields or claim live citation links unless genuine user-provided records and a supporting tool created and verified them. Plain citations are preferable to fake field codes.

## Verify output

When generation tools permit:

1. confirm output exists and parses or opens;
2. inspect headings, citations, references, equations, figures, tables, numbering, metadata, and unresolved markers;
3. render or open the final artifact and inspect pagination, clipping, overlap, fonts, symbols, links, and image quality;
4. compare content with reviewed source and record tool/version and warnings.

If structural or visual inspection is unavailable, say which check remains manual. Never call output submission-ready without fresh project-specific verification.
