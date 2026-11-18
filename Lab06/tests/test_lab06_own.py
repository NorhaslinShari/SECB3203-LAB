from pathlib import Path

import pytest

from batch import main, process_directory
from bio_io import FastaFormatError, read_fasta

def test_empty_file_fasta(tmp_path):
    fasta = tmp_path / "geneC.fasta"
    fasta.write_text("", encoding="utf-8")

    assert list(read_fasta(fasta)) == []

def test_record_without_sequence(tmp_path):
    record = tmp_path / "geneD.fasta"
    record.write_text(">geneD", encoding="utf-8")

    with pytest.raises(FastaFormatError): 
        list(read_fasta(record))

def test_empty_folder_process_directory(tmp_path):
    out_csv = tmp_path / "results.csv"
    summary = process_directory(tmp_path,out_csv)

    assert summary == {"processed": 0, "rejected": 0, "records": 0}

def test_exit_code2_missing_folder(tmp_path):
    missing = tmp_path / "missing"
    assert main([str(missing)]) == 2
                       
