# SECB3203 Lab 5 - Functions and modules: sequence_utils.py and normalize.py

Student: NORHASLIN BINTI SHARI, A24CS0149

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/sequence_utils.py` : clean_sequence, is_valid_dna, gc_content, reverse_complement, find_motif
- `src/normalize.py` : proportions, cpm (never change the caller's data)
- `tests/` : visible tests and my own tests (test_lab05_own.py)
- `AI_USE_LOG.md` : my AI prompt log

## Design decisions
proportions() raises ValueErroer when the total is zero because if one input for instance 20 divided by zero, it shows error (dividing by zero is undefined). Therefore, we need to include ValueError for this case. Next, in normalize.py , line 13 (result = []) is to ensure new list is created. Thus, the original input list wont change.

