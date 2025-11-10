# Interim Data

This folder contains **intermediate files** generated during multi-stage data
processing. These datasets are typically produced by scripts in `scripts/` and
serve as inputs to subsequent processing steps.

Examples:
- Cleaned but not yet fully standardized datasets
- Merged or subsetted intermediates
- Temporary artifacts needed for later steps
- Outputs from long-running preprocessing tasks

Best practices:
- Files should be able to be deleted and regenerated at any time.
- Do not hand-edit files in this directory.
- Keep this directory organized by using clear, stage-specific filenames.