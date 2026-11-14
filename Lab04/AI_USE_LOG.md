# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 4
- Student name: NORHASLIN BINTI SHARI
- Matric no: A24CS0149
- Group ID: n/a
- AI level: 1 
- Tools cited: Microsoft Copilot (GPT-5 Chat Model). Accessed 9 November 2026. Available at: https://copilot.microsoft.com/ 

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 8 November 2026 (8:03 pm)
- Tool: Microsoft Copilot (GPT-5 Chat Model). Accessed 8 November 2026. Available at: https://copilot.microsoft.com/ 
- Purpose: Explain
- Prompt: can u explain to me the flow, just give hint from task 1 to 4
- Output: copilot explain to me about the flow for each task from 1 to 4.
Since this is an AI Level 1 lab, I'll explain the task and give hints, but I won't write the full solution for you.

T1: filter_panel(genes, priority)

Requirements:

genes is a list.
priority is likely a set.
Return only genes that appear in priority.
Keep the original order from genes.
Keep duplicates.
Do not modify the input list. 

T1: sorted_copy(items)

Requirements:

Return a new sorted list.
Original list must stay unchanged.

T2: sort_variants(variants)

Requirements:

variants is a list of Variant objects.
Return a new sorted list.
The original list must stay unchanged.
Sort chromosomes in this order:
1 to 22
X
Y
M
Chromosome names may have a "chr" prefix:
"chr2" and "2" are the same chromosome.
"chrX" and "X" are the same chromosome.
Sort by chromosome first, then by pos.
Do not sort chromosome names as text because:
"10" < "2"

is True when comparing strings.

Key ideas:

Remove the "chr" prefix if it exists.
Convert numeric chromosomes to integers.
Give special ranks to:
X -> 23
Y -> 24
M -> 25

Build a sort key:
(chromosome_rank, position)

Use:
sorted(...)

so the input list is not modified.
T3: CODON_TABLE

Requirements:

Create a dictionary containing all 64 DNA codons.
Use:
itertools.product()

Do not manually type all 64 codons.
Use the _BASES string and _AMINO string provided in the starter code.
Stop codons should map to:
"*"
Key ideas:

Generate all possible 3-base combinations:
itertools.product(_BASES, repeat=3)

Convert each tuple into a DNA codon string using:
"".join(codon)

Pair codons with amino acids using:
zip(...)

Build a dictionary from those pairs.
T3: count_bases(seq)

Requirements:

Count every character in the sequence.
Convert the sequence to uppercase first.
Return a dictionary sorted by key.
Return:
{}

for an empty string.

Key ideas:

Convert:
seq.upper()

Use:
Counter()

Sort dictionary keys with:
dict(sorted(counter.items()))
Example:"ATGc"

becomes:"ATGC"
and counts:

{
    "A": 1,
    "C": 1,
    "G": 1,
    "T": 1
}

T3: kmer_counts(seq, k)

Requirements:

Count overlapping k-mers.
Convert sequence to uppercase.
Return sorted dictionary.
Return:
{}

if k is longer than the sequence.
Raise:
ValueError

if k < 1.

Key ideas:

A k-mer is a substring of length k.
Use slicing:
seq[i:i+k]

Move one position at a time.
Count all generated k-mers using:
Counter()

Sort the result by key.
Example:

seq = "ATGCA"
k = 3

k-mers:"ATG"
"TGC"
"GCA"

T4: shared_genes(panel, detected)

Requirements:

Return genes present in both collections.
Return a set.
Do not modify either input.

Key ideas:

Use set intersection.
Keep only genes appearing in both sets.

Example:

panel = {"BRCA1", "TP53", "EGFR"}
detected = {"TP53", "ALK"}


Result:
{"TP53"}
T4: safe_expression(expression, gene)

Requirements:

Return the gene's value if present.
Return:
None

if the gene is missing.
Must return a real:
0.0

if that is the stored value.
Must not add keys to the dictionary.

Key ideas:

Use:
dict.get()

Avoid using:
setdefault()

because it modifies the dictionary.
Distinguish:
0.0

from:
None


Example:
expression = {
    "BRCA1": 0.0,
    "TP53": 4.5
}
Results:

safe_expression(expression, "BRCA1")
0.0

safe_expression(expression, "EGFR")
None

T4: translate(dna)

Requirements:

Convert DNA into a protein sequence.
Accept upper-case or lower-case DNA.
Translate every codon using CODON_TABLE.
Keep stop codons:
"*"

in the output.
Do not stop translating when a stop codon is found.
Raise:
ValueError

if DNA length is not a multiple of 3.
Raise:
ValueError

if a codon is invalid.
Empty string returns:
""


Key ideas:

Convert DNA to uppercase.
Process DNA three bases at a time:
for i in range(0, len(dna), 3)

Extract codons using:
dna[i:i+3]

Look up amino acids in:
CODON_TABLE

Join all amino acids into one protein string.

Example:

DNA:
ATGTTC

Codons:
ATG
TTC
Translation:

ATG -> M
TTC -> F

Result:
"MF"
Validation checks:

Length must be divisible by 3.
Every codon must exist in CODON_TABLE.
Empty DNA returns an empty protein string.

- Verified by: I tested the functions using the examples provided in the lab instructions and checked that the outputs matched the expected results. I also test with my own code to check whether it show the correct output or not. 
- My change: I used AI to help me understand the requirements and concepts such as list copying, sorting with tuple keys, sets, dictionaries, Counter, and codon translation. Then, using it as guide for me to complete the rest of the code.
- Used in: panel.py and lookup.py


# Entry 2

- Date: 9 November 2026 (8.36 PM)
- Tool: Microsoft Copilot (GPT-5 Chat Model). Accessed 9 November 2026. Available at: https://copilot.microsoft.com/ 
- Purpose: Explain
- Prompt: can u check what is wrong and comment, do not give me answer
- Output: AI reviewed my code and pointed out the mistakes in my logic without giving me the final solution. It explained why some parts were unnecessary, how my loop structure affected the result, and whether my code matched the task requirements.
- Verified by: I compared the feedback with the lab instructions and tested the function using my own examples to see if the behaviour matched the requirements. Then, i ran pytest to see if all test passed or not
- My change: Understand the question and comment given by AI and try to modify my code until all test passed
- Used in: test_lab04_own.py