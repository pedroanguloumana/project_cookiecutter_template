# Writing

This folder contains the LaTeX manuscript associated with this project. The
`writing/` directory functions as a self-contained LaTeX project, including
source files, bibliographies, and figures generated elsewhere in the repository.

Typical contents:
- `main.tex` — Root LaTeX file for the manuscript
- `sections/` — Optional subfolder for organized LaTeX sections
- `figures/` — Figures imported from `notebooks/publication/` or `scripts/`
- `references.bib` — Bibliography file for the manuscript
- `Makefile` or build scripts (optional)

Best practices:
- Keep the manuscript project self-contained so it can be built via `pdflatex`,
  `latexmk`, or a Makefile without referencing external paths.
- Use `notebooks/publication/` or scripts to generate figures and save them into
  `writing/figures/`.
- Avoid committing large generated PDFs unless needed for archival purposes.
- If the project grows to multiple papers, each manuscript can be placed in a
  separate subfolder under `writing/`.
