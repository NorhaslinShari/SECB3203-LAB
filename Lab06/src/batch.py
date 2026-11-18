"""Week 6 extension - batch processing, logging, FASTQ and a command-line tool."""
import argparse
import logging
import sys
from collections.abc import Iterator
from pathlib import Path

from bio_io import FastaFormatError, read_fasta, write_csv

LOG = logging.getLogger("batch")


class FastqFormatError(ValueError):
    """Raised when a FASTQ file is malformed."""


def process_directory(in_dir, out_csv, log_path=None) -> dict[str, int]:
    """Read every *.fasta file in in_dir; one bad file never stops the batch.

    Writes one row per file (file, records, status, reason) to out_csv and
    returns {'processed': ..., 'rejected': ..., 'records': ...}.
    """
    file = None
    if log_path is not None:
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        file = logging.FileHandler(log_path, mode="w", encoding="utf-8") #nk write kt file log nnti
        file.setFormatter(logging.Formatter("%(levelname)s %(message)s")) # set format 
        LOG.addHandler(file) #connect logger to batch.log
        LOG.setLevel(logging.INFO)

    rows = []
    summary = {"processed": 0, "rejected": 0, "records": 0}

    try: 
        for path in sorted(Path(in_dir).glob("*.fasta")): # * untk semua file , ikot order
            try:
                count = sum(1 for _ in read_fasta(path)) # every record found, = 1, kira record dlm stu file
                if count == 0:
                    raise FastaFormatError("empty file")
            except (OSError, UnicodeDecodeError, FastaFormatError) as err:
                LOG.warning("rejected %s: %s", path.name, err)
                rows.append({"file": path.name, "records": 0, "status": "rejected", "reason": str(err)})
                summary["rejected"] += 1
            else:
                LOG.info("processed %s (%d records)", path.name, count) # kiraan dia
                rows.append({"file": path.name, "records": count, "status": "processed", "reason": ""})
                summary["processed"] += 1
                summary["records"] += count

        Path(out_csv).parent.mkdir(parents=True, exist_ok=True)
        write_csv(rows, out_csv, ["file", "records", "status", "reason"]) #info ada kt processing_log.csv

    finally:
        if file is not None:
            LOG.removeHandler(file) # awal tu addHandler, connect ngn log, ni nk disconnect 
            file.close()
    return summary


def read_fastq(path) -> Iterator[tuple[str, str, str]]:
    """Yield (read_id, sequence, quality) for each 4-line FASTQ record."""
    with open(path, "r", encoding="utf-8") as file:
        while True:
            header = file.readline() # baca exp: @read1
            if not header:
                return
            if not header.strip(): # ni skip blank lines ngn whitespace dpn blkg
                continue
            seq = file.readline().strip()
            plus = file.readline().strip()
            qual = file.readline().strip()
            if not header.startswith("@") or not plus.startswith("+"):
                raise FastqFormatError(f"{path}: malformed record near {header.strip()!r}")
            if len(seq) != len(qual):
                raise FastqFormatError(f"{path}: sequence and quality lengths differ" 
                                       f"for {header.strip()!r}")
            
            read_id = header[1:].split()[0]
            yield read_id, seq, qual  


def mean_phred(quality: str, offset: int = 33) -> float:
    """Mean Phred score of a quality string (Phred+33 by default)."""
    if not quality:
        raise ValueError("quality string is empty")
    return sum(ord(ch) - offset for ch in quality) / len(quality)


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point. Exit code 0 = all good, 1 = some files rejected, 2 = bad input."""
    
    parser = argparse.ArgumentParser( description="Summarise every FASTA file in a folder.")
    parser.add_argument("in_dir", help="folder containing *.fasta files")
    parser.add_argument("--out", default="results",
                        help="output folder (default: results)")
    args = parser.parse_args(argv)

    if not Path(args.in_dir).is_dir():
        print(f"error: {args.in_dir} is not a folder", file=sys.stderr)
        return 2
    
    out = Path(args.out)
    summary = process_directory( args.in_dir, out / "processing_log.csv", out / "batch.log")
    print(f"processed={summary['processed']} "
          f"rejected={summary['rejected']} "
          f"records={summary['records']}")
    
    return 1 if summary["rejected"] else 0

if __name__ == "__main__":
    sys.exit(main())
