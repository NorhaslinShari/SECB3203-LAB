"""Lab 3 - sequence quality control with conditions and loops."""


def classify_read(
    length: int,
    n_count: int,
    gc: float,
    *,
    min_len: int = 500,
    max_n: int = 10,
    gc_range: tuple[float, float] = (30.0, 70.0),) -> str: #[0 = 30.0, 1 = 70.0]
    """Return 'reject', 'review' or 'pass' for one sequencing record.

    Rules are checked in this order: too short -> reject; too many N or GC
    outside the inclusive range -> review; otherwise pass.
    """
    if length < min_len:
        return "reject"

    if n_count > max_n or not (gc_range[0] <= gc <= gc_range[1]): # gc within the inclusive range
        return "review"

    else:
        return "pass"
 

def qc_summary(records: list[dict]) -> dict[str, int]:
    """Count records per decision. Values may be numbers or CSV strings."""
    summary = {"pass": 0, "review": 0, "reject": 0}

    for record in records:
        length = int(record["length"]) # set length to the integer value of the "length" key in qc_records.csv
        n_count = int(record["n_count"])
        gc = float(record["gc_percent"])
        decision = classify_read(length, n_count, gc)
        summary[decision] = summary[decision] + 1  # decision = pass -> summary["pass"] = 0 + 1

    return summary


def trim_low_quality(quals: list[int], threshold: int = 20) -> int:
    """Return how many bases to keep after trimming a low-quality 3' tail."""

    end = len(quals)

    while end > 0 and quals[end - 1] < threshold:    # only keep bases more than or equal to threshold
        end = end - 1

    return end 
