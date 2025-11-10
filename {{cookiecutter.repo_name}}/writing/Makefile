# --- Paths relative to this Makefile ---
ROOT := $(abspath ..)
SLIDES_DIR := $(abspath .)
BUILD_DIR := $(SLIDES_DIR)/build
FIGS_DIR := $(SLIDES_DIR)
OUT_DIR := $(SLIDES_DIR)

KEY_FILES := $(wildcard $(FIGS_DIR)/*.key)
DECKS := $(basename $(notdir $(KEY_FILES)))

.PHONY: all clean check

all: $(addprefix out-,$(DECKS))

check:
	@command -v osascript >/dev/null || (echo "ERROR: osascript missing (macOS only)"; exit 1)
	@osascript -e 'id of app "Keynote"' >/dev/null 2>&1 || (echo "ERROR: Keynote not installed"; exit 1)
	@command -v pdfseparate >/dev/null || (echo "ERROR: pdfseparate missing (install poppler)"; exit 1)
	@command -v pdfcrop >/dev/null || (echo "ERROR: pdfcrop missing (install TeX Live)"; exit 1)

# Build rule: paper_figures.key -> paper_figures.pdf -> paper_figures-01.pdf etc
out-%: %.key | check
	@mkdir -p "$(BUILD_DIR)"
	@osascript \
	    -e 'tell application "Keynote"' \
	    -e 'set theDoc to open (POSIX file "$(abspath $<)")' \
	    -e 'export theDoc to (POSIX file "$(BUILD_DIR)/$*.pdf") as PDF' \
	    -e 'close theDoc saving no' \
	    -e 'end tell'
	@echo "Exported: $(BUILD_DIR)/$*.pdf"

	@pdfseparate "$(BUILD_DIR)/$*.pdf" "$(BUILD_DIR)/$*-%02d.pdf"
	@echo "Split into pages."

	@for p in "$(BUILD_DIR)"/$*-*.pdf; do \
	    name=$$(basename $$p); \
	    out="$(OUT_DIR)/$$name"; \
	    pdfcrop "$$p" "$$out" >/dev/null; \
	    echo "Cropped $$p -> $$out"; \
	done
	@echo "DONE: $*"
	
clean:
	rm -rf "$(BUILD_DIR)"
