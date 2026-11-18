"""Week 6 - reading FASTA and CSV safely."""
import csv
from collections.abc import Iterator
from pathlib import Path


class FastaFormatError(ValueError):
    """Raised when a FASTA file does not follow the format."""


def _finish(record_id: str, chunks: list[str], path) -> tuple[str, str]:
    if chunks == []:
        raise FastaFormatError(f"{path}: record '{record_id}' has no sequence")

    return record_id, "".join(chunks).upper()


def read_fasta(path) -> Iterator[tuple[str, str]]:
    """Yield (record_id, sequence) for every record in a FASTA file.

    The id is the first word of the header. Wrapped lines are joined and the
    sequence is upper-cased. Records are produced one at a time, so large
    files do not have to fit in memory.

    Raises:
        FileNotFoundError: if the file does not exist.
        FastaFormatError: for data before the first header, an empty header
            or a record without sequence.
    """
    record_id = None
    sequence = []
    
    with open(Path(path), "r", encoding="utf-8") as file: # r -> nk read 
        for line in file:
            line = line.strip() # remove whitespace dkt depn and blkg 

            if line == "": # line will skip blank lines
                continue

            if line.startswith(">"): #header >
                if record_id is not None:
                    yield _finish(record_id, sequence, path) #previous file

                header = line[1:].strip() # remove > for header (later line start at index 1 till end)
                if not header:
                    raise FastaFormatError(f"{path}: empty header")

                record_id, sequence = header.split()[0], [] # save first word je, exp geneA
                 # [] start nk collect sequence line 

            else:
                if record_id is None:
                    raise FastaFormatError(
                            f"{path}: data before first header")

                sequence.append(line)

    if record_id is not None: # add this so current file can return
        yield _finish(record_id, sequence, path)  


def read_csv_records(path) -> list[dict[str, str]]:
    """Read a CSV file into a list of dictionaries (all values are strings)."""
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_csv(rows: list[dict], path, fieldnames: list[str]) -> None:
    """Write rows to a CSV file, creating the parent folder if needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True) # create output folder if x exist and make output folder safely
    
    with open(path, "w", newline="", encoding="utf-8") as file:
        write = csv.DictWriter(file, fieldnames=fieldnames)
        write.writeheader() # write column names (guna fieldnames)
        write.writerows(rows)