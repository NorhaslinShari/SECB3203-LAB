"""Lab 4 - dictionaries and sets for biological lookup."""
import itertools
from collections import Counter

_BASES = "TCAG"
_AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON_TABLE: dict[str, str] = {   
    "".join(codon): aa # from ('T', 'T', 'T') tuple = into string "TTT"

    # itertools.product produce every possible combination of 3 bases dna 
    for codon, aa in zip(itertools.product(_BASES, repeat=3), _AMINO) # zip , pairs each codon with one char aa
    
}

def count_bases(seq: str) -> dict[str, int]:
    """Count each character in seq (upper-cased), sorted by key."""
    seq = seq.upper()
    counter = Counter(seq)  # Count the occurrences of each character
    
    return dict(sorted(counter.items())) # include .items() return (key, value) pairs


def kmer_counts(seq: str, k: int) -> dict[str, int]:
    """Count overlapping k-mers, sorted by key. ValueError if k < 1."""
    seq = seq.upper()
    
    if k < 1:
        raise ValueError("k must be at least 1")

    if k > len(seq):
        return {}

    kmers = [] 
    for i in range(len(seq) - k + 1): # len = 5 , k = 2, so range(4) = 0,1,2,3
        kmers.append(seq[i:i+k])  # slice, include start , exclude end

    counter = Counter(kmers)

    return dict(sorted(counter.items()))  

def shared_genes(panel: set[str], detected: set[str]) -> set[str]:
    """Genes that are both on the panel and detected."""
    return panel.intersection(detected)  # return the intersection of two sets


def safe_expression(expression: dict[str, float], gene: str) -> float | None:
    """Return the expression value, or None when the gene is missing."""
    return expression.get(gene)  # Use .get() to safely retrieve the value or return None if the key is not found

def translate(dna: str) -> str:
    """Translate DNA to a protein string ('*' marks a stop codon).
    Raises:
        ValueError: if the length is not a multiple of 3 or a codon is invalid.
    """
    
    if len(dna) % 3 != 0:
        raise ValueError("DNA length must be a multiple of 3")

    dna = dna.upper()
    protein = ""

    for i in range(0, len(dna), 3): #range(start, stop, step)
        codon = dna[i:i+3]
        if codon not in CODON_TABLE:
            raise ValueError(f"Invalid codon: {codon}")
        protein += CODON_TABLE[codon] #CODON_TABLE["ATG"] = "M"

    return protein
