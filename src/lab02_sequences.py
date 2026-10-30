"""Lab 2 - biological sequences as strings (becomes sequence_utils.py in Week 5)."""

DNA_BASES = frozenset("ACGT")

def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    result = ""

    for char in raw:
        if char.isalpha(): #check if character is a letter
            result += char.upper()

    return result


def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (and N when allowed)."""
    if seq == "": #check if sequence is empty
        return False

    if allow_n:  # if allow_n tu true ada ( ACGTN , True)
        return set(seq) <= set("ACGTN") # check if all characters in the sequence are in the set of valid bases including N

    return set(seq) <= set("ACGT") # ni if allow_n is false



def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""

    seq = seq.upper()  
    if seq == "":
        raise ValueError("Sequence cannot be empty") 

    if not is_valid_dna(seq): 
        raise ValueError("Invalid DNA sequence")

    gc_count = seq.count("G") + seq.count("C")
    return (gc_count/len(seq)) * 100


def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""

    dna = dna.upper()
    if not is_valid_dna(dna):
        raise ValueError("Invalid DNA sequence")

    rna = dna.replace("T", "U") #replace T char with U
    return rna


def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""

    seq = seq.upper()
    motif = motif.upper()

    if motif == "":
        raise ValueError("Motif cannot be empty")

    positions = [] #list to store motif positions
    start = 0  # starting index for searching

    while True:
        pos = seq.find(motif, start) # cri motif kat seq start with start index

        if pos == -1:
            break

        positions.append(pos)  #add found position to the list
        start = pos + 1  # move forward by ONE base , check one by one base 

    return positions
