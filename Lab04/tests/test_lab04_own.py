from lookup import kmer_counts, safe_expression
from panel import Variant, sort_variants, sorted_copy

def test_sorted_copy_unchanged():
   ori = ["CFTR", "TP53", "BRCA1"]
   copyOri = ori.copy()
   assert sorted_copy(ori) ==  ["BRCA1", "CFTR", "TP53"]
   assert ori == copyOri

def test_chrom_sort_variants_include_X_M():
    ct = [Variant("10", 5, "A", "Y"),Variant("M", 2, "C", "T"), Variant("3", 2, "A", "G"), Variant("X", 1, "S", "A")]
    assert [c.chrom for c in sort_variants(ct)] == ["3", "10", "X", "M"]

def test_k_larger_and_empty_kmer_counts():
    assert kmer_counts("atgtgatgc", 10) == {}
    assert kmer_counts("", 1) == {}

def test_missing_gene_and_real_safe_expression():
    assert safe_expression({"TP53": 5.7}, "CFTR") is None
    assert safe_expression({"BRCA1" : 0.0}, "BRCA1") == 0.0