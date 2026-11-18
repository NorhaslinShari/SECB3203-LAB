# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 6
- Student name: NORHASLIN BINTI SHARI
- Matric no: A24CS0149
- Group ID: n/a
- AI level: 1 
- Tools cited: Microsoft Copilot (GPT-5 Chat Model). Accessed 17 November 2026. Available at: https://copilot.microsoft.com/  

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 17 November 2026 (8:02 PM)
- Tool: Microsoft Copilot (GPT-5 Chat Model). Accessed 17 November 2026. Available at: https://copilot.microsoft.com/ 
- Purpose: explain
- Prompt: I want u to explain task by task what this lab 6 wants, detail please but do not give answer just hint so i can complete my lab
- Output: Your job is to build a system that:

        Reads FASTA safely.
        Reads/writes CSV safely.
        Processes an entire folder without crashing.
        Reads FASTQ quality data.
        Can be run from the command line.
        T1: FASTA Reader (5 marks)
        What problem are they solving?
        A FASTA file can contain many sequences, not just one.

        Example:
        Plain Text
        >geneA
        ATGC
        >geneB
        AAATTT
        >geneC
        GGGCCC

        Many beginners only read:
        Python
        first sequence

        and accidentally ignore:
        Plain Text
        geneB
        geneC

        The lecturer wants you to read every record.
        What you need to understand
        FASTA structure

        Header:
        >geneA

        Sequence:
        Plain Text
        ATGC
        Header ID

        Example:
        Plain Text
        >geneA human mitochondria

        Only take:
        Plain Text
        geneA

        not:

        Plain Text
        geneA human mitochondria
        Wrapped sequences

        This:
        Plain Text
        fasta isn’t fully supported. Syntax highlighting is based on Plain Text.
        >geneA
        ATGC
        ATGC
        ATGC

        must become:
        Plain Text
        ATGCATGCATGC

        Not three separate sequences.

        Generator

        They specifically want:
        Python
        yield

        Why?
        Without generator:

        Python
        read entire file
        store everything

        With generator:
        Python
        yield sequence1
        yield sequence2
        yield sequence3

        Good for huge FASTA files.

        Error handling
        Data before header

        Bad:
        Python
        ATGC
        >geneA

        Should raise:
        Python
        FastaFormatError
        Empty header

        Bad:
        >
        ATGC

        Raise:
        Python
        FastaFormatError
        No sequence

        Bad:
        >geneA

        Raise:
        Python
        FastaFormatError
        Empty file
        Plain Text
        (empty)

        This is NOT an error.

        Just:
        Python
        yield nothing
        T2: CSV Reading and Writing (2 marks)
        Why?

        The batch program must produce reports.
        Reports are usually:
        CSV
        file,status,records
        A.fasta,processed,10
        B.fasta,rejected,0
        read_csv_records()

        Purpose:

        Turn
        CSV
        name,score
        Ali,10
        Siti,20

        into

        Python
        [
        {"name":"Ali","score":"10"},
        {"name":"Siti","score":"20"}
        ]
        write_csv()

        Purpose:

        Turn

        Python
        [
        {"name":"Ali","score":"10"}
        ]

        into

        CSV
        name,score
        Ali,10
        Why newline=""?

        Windows problem.

        Without:

        Python
        newline=""

        you get:

        CSV
        name,score
         
        Ali,10
         
        Siti,20

        Extra blank lines.

        T3: process_directory() (3 marks)

        This is the main idea of the lab.

        Scenario

        Folder:

        Plain Text
        river/
        ├── a.fasta
        ├── b.fasta
        ├── c.fasta
        Normal beginner mistake
        Python
        for file in files:
        read_fasta(file)

        If:

        Plain Text
        b.fasta

        is bad,

        program crashes.

        What lecturer wants

        Process:

        Plain Text
        a.fasta ✅
        b.fasta ❌
        c.fasta ✅

        Even though:

        Plain Text
        b.fasta

        fails.

        Why try is inside loop

        Wrong:

        Python
        try:
        for file in files:

        One error kills everything.

        Correct:

        Python
        for file in files:
        try:

        Each file handled separately.

        Logging

        Instead of:

        Python
        print()

        create:

        Plain Text
        batch.log

        Example:

        Plain Text
        INFO processed a.fasta
        WARNING rejected b.fasta
        INFO processed c.fasta
        CSV report

        Example:

        CSV
        file,records,status,reason
        a.fasta,10,processed,
        b.fasta,0,rejected,empty file
        c.fasta,20,processed,
        Summary dictionary

        Return:

        Python
        {
        "processed": 2,
        "rejected": 1,
        "records": 30
        }
        T4: FASTQ + CLI (4 marks)

        Now we move from FASTA to FASTQ.

        FASTQ

        Structure:

        Python
        fastq isn’t fully supported. Syntax highlighting is based on Python.
        @read1
        ATGC
        +
        IIII

        4 lines.

        Always.

        Why exactly 4 lines?

        Quality can contain:

        Plain Text
        @
        +
         

        inside it.

        So don't search for symbols.

        Read:

        Python
        line1
        line2
        line3
        line4

        every time.

        FASTQ checks

        Header must start:

        Plain Text
        @

        Third line must start:

        Plain Text
        +

        Lengths must match:

        Plain Text
        ATGC
        IIII
         

        4 = 4

        Bad:

        Plain Text
        ATGC
        III

        4 ≠ 3

        Raise:

        Python
        FastqFormatError
        mean_phred()

        Quality characters are encoded.

        Example:

        Python
        "I"

        ASCII:

        Python
        73

        Then:

        Python
        73 - 33

        Phred:

        Python
        40

        Mean:

        Python
        sum(scores)/count
        Command-Line Tool

        Now users should run:

        Shell
        python src/batch.py data/river

        instead of opening Python.

        Exit code 0

        Everything good.

        Plain Text
        processed=3 rejected=0 records=40

        Return:

        Python
        0
        Exit code 1

        Some files rejected.

        Plain Text
        processed=2 rejected=1 records=30

        Return:

        Python
        1
         
        Exit code 2

        Input folder doesn't exist.

        Plain Text
        error: missing folder

        Return:

        Python
        2
        Why use argv?

        So tests can do:

        Python
        main(["data/river"])

        without opening CMD.

        That's why:

        Python
        parse_args(argv)

        is required.

        T5: Your Own Tests (4 marks)

        Now YOU become the tester.

        Lecturer already has hidden tests.

        You must create your own.

        What they want

        Use:

        Python
        tmp_path

        to create temporary files/folders.

        Good test ideas
        Empty file
        Plain Text
        empty.fasta

        Expect:

        Python
        []
        Missing sequence
        Python
        >geneA

        Expect:
        Python
        FastaFormatError
        Missing file
        Plain Text
        missing.fasta

        Expect:
        Python
        FileNotFoundError
        Empty folder
        Python
        process_directory()
         

        Expect:
        Python
        {
        "processed":0,
        "rejected":0,
        "records":0
        }
         
        Missing folder
        Python
        main(["missing"])

        Expect:
        Python
        2
- Verified by: i read the slide in week 6 and try to understand it using AI, i run pytest and do my oown test (print) eacah time create new def 
- My change: i tryy follow the code that already in slide and try adding few comment based on my understading
- Used in: batch.py, bio_io.py and test_lab06_own.py

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry y3 ... -->
