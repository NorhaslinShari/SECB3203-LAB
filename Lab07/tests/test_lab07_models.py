import pytest

from models import BiologicalSample, DNASequence, SampleCollection

def test_invalid_dna():
    with pytest.raises(ValueError):
        DNASequence("bad", "ATGNN")

def test_duplicate_sampleId():
    collection = SampleCollection()
    s1 = BiologicalSample("S1", "control", DNASequence("dna1", "ATTGC"))
    s2 = BiologicalSample("S1", "treated", DNASequence("dna2", "GGCC"))
    collection.add(s1) 

    with pytest.raises(ValueError):
        collection.add(s2)

def test_reverse_complement_name():
    dna = DNASequence("seq1", "ATGC")

    rc = dna.reverse_complement()

    assert rc.name == "seq1_rc"
    assert rc.sequence == "GCAT"
        
        
        
