# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 7
- Student name: NORHASLIN BINTI SHARI
- Matric no: A24CS0149
- Group ID:  n/a
- AI level: 1
- Tools cited: Microsoft Copilot (GPT-5 Chat Model). Accessed 26 November 2026. Available at: https://copilot.microsoft.com/  


## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 26 November 2026 (7:47 pm)
- Tool: Microsoft Copilot (GPT-5 Chat Model). Accessed 26 November 2026. Available at: https://copilot.microsoft.com/  
- Purpose: check the code
- Prompt: can u check is there anything wrong with my test code​
- Output: Test 3
Python
def test_reverse_complement_name():
dna = DNASequence("seq1", "ATGC")
 
rc = dna.reverse_complement()
assert rc.name == "seq1_rc"

⚠️ Here is the one I would double-check.

Questions:
Does DNASequence use name?

For example:

class DNASequence:
def __init__(self, sequence_id, sequence):
self.sequence_id = sequence_id

Then this should be:
assert rc.sequence_id == "seq1_rc"

instead of:

assert rc.name == "seq1_rc"
Does reverse_complement() actually append _rc?

Your code may return:

DNASequence("seq1", "GCAT")

instead of
DNASequence("seq1_rc", "GCAT")
Look at the implementation.
- Verified by: <How you checked it: ran pytest, read the docs, compared with data, asked lecturer>
- My change: <What you accepted, rejected or rewrote, and why>
- Used in: <File and function, or report section, where it ended up (or 'not used')>

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->
