# Raw Data

This folder contains the **original, immutable source data** for the project.
Files here should never be edited, overwritten, or manually modified. All
processing should be performed by scripts in the `scripts/` directory, with
outputs written to `data/interim/` or `data/processed/`.

Examples:
- Downloaded datasets
- External data received from collaborators
- Unmodified observational or model output
- Symbolic links to data stored outside the project directory
  (create links with: `ln -s <path_to_existing_data> {{ cookiecutter.repo_name }}`)

Best practices:
- Treat this directory as read-only.
- Keep metadata (source, date acquired, version) in filenames or a separate log.
- Prefer symbolic links for large or shared datasets to avoid duplication.