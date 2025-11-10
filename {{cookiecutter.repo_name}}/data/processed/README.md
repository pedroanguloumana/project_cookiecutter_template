# Processed Data

This folder contains **final, analysis-ready datasets** created from the raw and
interim data. Notebooks in `notebooks/publication/` and downstream analyses
should read from this directory.

Examples:
- Final cleaned datasets
- Derived metrics or aggregated tables
- Gridded or standardized outputs
- Data used to generate publication figures

Best practices:
- Files here should be reproducible from scripts and not manually modified.
- Keep transformations deterministic and capture logic in `scripts/`.
- Use clear versioning or timestamps if processed data changes over time.