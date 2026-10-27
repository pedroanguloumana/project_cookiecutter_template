# Working conventions for Codex

This is a scientific analysis project used on personal computers and HPC systems. Keep the same analysis code usable in each environment, even when the available datasets and storage paths differ.

## Where code belongs

- **Python package** (the directory containing `__init__.py`): Put genuinely reusable data loading, scientific calculations, and plotting helpers here. Move a notebook helper into the package when it represents a stable operation that is useful across workflows, not merely because a few lines appear twice.
- **`notebooks/`**: Use notebooks for exploration, interpretation, and assembling individual figures. Give each notebook a clear question or output. Use Markdown headings to explain the scientific purpose, inputs, choices, and conclusions. Keep the sequence readable from top to bottom. Small, figure-specific glue code may stay in the notebook.
- **`scripts/`**: Put repeatable command-line and batch workflows here, especially preprocessing or figure production that should run unattended on a cluster. Document how to run each script and its expected inputs and outputs. Make scripts runnable from the project root without changing `sys.path`.
- **`data/`**: Treat this as the required entry point for all data access. Keep local symlinks here to model and observation archives; do not commit large raw files. Raw data may live outside the repository on each machine.
- **`figures/`**: Save a figure only when the user directs you to save it. When saving a figure intended for review or a manuscript, use this directory. Prefer vector PDF for publication figures. Use descriptive, stable filenames and commit only outputs worth sharing across machines.

## Python and scientific code

- Import between modules in the same package with relative imports, such as `from .paths import FIGURE_DIR`. Import the installed package by its generated name from notebooks and scripts. Do not assume the package is named `src` or rely on the current working directory for imports.
- Centralize project paths in `paths.py` and use `pathlib.Path`. Before adding or changing a data path, inspect the repository's `data/` directory and check that the required symlink exists and resolves. **Always route data access through `data/` symlinks**; do not put direct machine-specific archive paths, environment-variable bypasses, or fallback roots in analysis code. Configure each machine by updating its local symlinks.
- Write cohesive functions with descriptive names. Prefer explicit arguments and return values over hidden state. Add concise docstrings for reusable functions, including expected dimensions, units, and returned objects when these matter.
- Preserve xarray coordinates, dimensions, attributes, and units where possible. State selections, averaging, normalization, sign conventions, and unit conversions explicitly. Check source metadata before treating a numerical factor as a physical conversion.
- Fail clearly when required inputs are missing or ambiguous. Avoid silently substituting a different dataset, variable, time period, or calculation.
- Put shared plot styling and save helpers in the package; keep the scientific content and layout of a particular figure close to its notebook or script. Label axes and colorbars with quantities and units.
- Make every figure a single, stand-alone panel unless the user directs you to make a multi-panel figure. When several figures are needed, create separate single-panel figures in a loop where appropriate.
- Prefer explicit imports in new code. Keep comments focused on scientific reasoning or non-obvious implementation choices.

## Readability over strict DRY

- Start with the smallest direct implementation that meets the request. Do not add speculative flexibility, configuration, validation, or helper layers. Add complexity only for a concrete current requirement or an observed failure; prefer two simple functions over a shared abstraction when they are easier to understand.
- Optimize for understanding the analysis at the point of use. Some repetition is acceptable when it keeps a notebook, figure, or scientific calculation readable from top to bottom.
- Extract a helper when it captures a meaningful, stable operation, removes substantial complexity, or keeps an important scientific rule consistent across uses. Do not extract code solely because two blocks look similar.
- Avoid chains of tiny functions, single-use wrappers, generic frameworks, and extra configuration layers that make the reader jump between files to follow one calculation.
- Keep consequential scientific choices visible near the calculation or figure: dataset, region, time range, units, thresholds, normalization, plot levels, and output name. Do not bury these in helper defaults just to reduce repeated lines.
- Before refactoring repeated code, compare the complete result with the original. Prefer the version a researcher can understand more quickly, even if it has more lines.

## Reproducible workflows across machines

- Keep code, documentation, and selected figures in Git. Record which input dataset, processing step, and parameters produced a shared figure or derived product. Avoid committing large raw or intermediate datasets by default.
- A notebook should run from a fresh kernel when its required data and dependencies are available. Do not depend on execution order from an earlier interactive session. Keep useful rendered outputs when their size is reasonable, and clear stale outputs after changing the code that produced them.
- Before running expensive analysis, inspect the active environment, available data, and output location. Use a small subset to check a new workflow when practical. Report what was actually run and what remains unverified.
- Preserve existing results and user edits. When a scientific choice is not specified and changes the interpretation, explain the choice or ask before committing to it.