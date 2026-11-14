"""Reusable DNA sequence utilities for BioPyLearn."""

DNA_BASES = frozenset("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    result = ""

    for char in raw:
        if char.isalpha():
            result += char.upper()

    return result

def is_valid_dna(sequence: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (N if allowed)."""
    sequence = sequence.upper()
    if sequence == "":
        return False

    if allow_n:
        return set(sequence) <= set("ACGTN") # <= (subset)

    return set(sequence) <= set(DNA_BASES)

def gc_content(sequence: str) -> float:
    """Return GC percentage (0-100); ValueError if invalid."""
    sequence = sequence.upper()
    if sequence == "":
        raise ValueError("Sequence are empty")

    if not is_valid_dna(sequence):
        raise ValueError("Invalid DNA sequence")

    gc_total = sequence.count("G") + sequence.count("C")
    return (round((gc_total/len(sequence) * 100), 2))

def reverse_complement(sequence: str) -> str:
    """Return the reverse complement; ValueError if invalid."""
    sequence = sequence.upper()
    if sequence == "":
        raise ValueError("Sequence are empty")

    if not is_valid_dna(sequence):
        raise ValueError("Invalid DNA sequence")

    rev_complement = sequence.translate(COMPLEMENT)[::-1] #reverse
    return rev_complement      

def find_motif(sequence: str, motif: str) -> list[int]:
    """Return every 0-based start of motif (overlaps allowed)."""
    sequence = sequence.upper()
    motif = motif.upper()
    
    if motif == "":
        raise ValueError("Motif cannot be empty")

    if len(motif) > len(sequence):
        return []

    position = []
    start = 0

    while True: 
        pos = sequence.find(motif, start)

        if pos == -1:
            break

        position.append(pos)
        start = pos + 1

    return position


if __name__ == "__main__":
    print(clean_sequence("hAslinN 2jfb/n"))
    print(is_valid_dna("Acgt",True))
    print(gc_content("gctaggcctaaatcg"))
    print(reverse_complement("acgtgttacc"))
    print(find_motif("AAAA", "aa"))