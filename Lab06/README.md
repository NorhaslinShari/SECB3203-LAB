# SECB3203 Lab 6 - Files and exceptions: bio_io.py and batch.py

Student: NORHASLIN BINTI SHARI, A24CS0149

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check
    python src/batch.py data/river --out results/cli      # the command-line tool

## What is in this repository
- `src/bio_io.py` : FastaFormatError, read_fasta, read_csv_records, write_csv
- `src/batch.py` : process_directory, read_fastq, mean_phred, main (command-line tool)
- `tests/` : visible tests and my own tests (test_lab06_own.py)
- `data/` : raw synthetic data, read-only (amplicons.fasta, river/, qc_records.csv, reads.fastq)
- `results/` : files the tool writes (not committed)
- `AI_USE_LOG.md` : my AI prompt log 

## Exit codes of batch.py
what i understand , code 0 is if everything work well. Next, code 1 if  batch can ran,but atleast one fasta was rejected. Lastly, code 2 if  input directory is not a valid folder before process begin
