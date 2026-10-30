# SECB3203 Lab 2 - Biological sequences as strings

Student: NORHASLIN BINTI SHARI, A24CS0149

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/lab02_sequences.py` : clean_sequence(), is_valid_dna(), gc_content(), transcribe(), find_motif()
- `tests/` :  test_clean_sequence_visible(), test_is_valid_dna_visible(), test_gc_content_visible(), test_transcribe_visible(), test_find_motif_visible() ||
test_find_motif_empty_motif(), test_find_motif_overlap(), test_find_motif_ignore_case()
- `AI_USE_LOG.md` : my AI prompt log 
