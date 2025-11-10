# Makefile for exporting Keynote decks to per-page, cropped PDFs using absolute paths.
# Works from any directory. No tabs required (uses .RECIPEPREFIX).

# ---- Configuration ----
.RECIPEPREFIX := >

REPO_NAME := {{ cookiecutter.repo_name }}

# Try to detect repo root via git; fall back to two levels up (typical: repo/writing/slides)
ROOT ?= $(shell git rev-parse --show-toplevel 2>/dev/null)
ifeq ($(ROOT),)
ROOT := $(abspath $(CURDIR)/../..)
endif

SLIDES_DIR := $(ROOT)/writing/slides
FIGS_DIR   := $(SLIDES_DIR)/figs
BUILD_DIR  := $(SLIDES_DIR)/build
OUT_DIR    := $(SLIDES_DIR)

KEY_FILES := $(wildcard $(FIGS_DIR)/*.key)
DECKS     := $(patsubst $(FIGS_DIR)/%.key,%,$(KEY_FILES))

.PHONY: all clean check
all: $(addprefix out-,$(DECKS))

# ---- Preconditions (macOS + tools) ----
check:
> command -v osascript >/dev/null || (echo "ERROR: osascript missing (macOS only)"; exit 1)
> osascript -e 'id of app "Keynote"' >/dev/null 2>&1 || (echo "ERROR: Keynote not installed"; exit 1)
> command -v pdfseparate >/dev/null || (echo "ERROR: pdfseparate missing (install poppler)"; exit 1)
> command -v pdfcrop >/dev/null || (echo "ERROR: pdfcrop missing (install TeX Live)"; exit 1)

# Build one deck: figs/foo.key -> build/foo.pdf -> build/foo-01.pdf ... -> (cropped) foo-01.pdf ...
out-%: $(FIGS_DIR)/%.key | check
> mkdir -p "$(BUILD_DIR)"
> osascript \
>   -e 'tell application "Keynote"' \
>   -e 'set theDoc to open (POSIX file "$(abspath $<)")' \
>   -e 'export theDoc to (POSIX file "$(BUILD_DIR)/$*.pdf") as PDF' \
>   -e 'close theDoc saving no' \
>   -e 'end tell'
> echo "Exported $< -> $(BUILD_DIR)/$*.pdf"
> pdfseparate "$(BUILD_DIR)/$*.pdf" "$(BUILD_DIR)/$*-%02d.pdf"
> echo "Split $(BUILD_DIR)/$*.pdf into per-page PDFs"
> for p in "$(BUILD_DIR)"/$*-*.pdf; do \
>   name=$$(basename $$p); \
>   out="$(OUT_DIR)/$$name"; \
>   pdfcrop "$$p" "$$out" >/dev/null; \
>   echo "Cropped $$p -> $$out"; \
> done
> echo "Done: $* (see $(OUT_DIR)/$*-NN.pdf)"

clean:
> rm -rf "$(BUILD_DIR)"
