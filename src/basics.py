"""Lab 1 - Python fundamentals for biological calculations."""


def gc_percent(a: int, c: int, g: int, t: int) -> float:
    """Return the GC percentage from the four base counts.

    Raises:
        ValueError: if any count is negative or the total is zero.
    """
    counts = (a,c,g,t)
    if any(count < 0 for count in counts):
        raise ValueError("Counts cannot be negative")

    total = sum(counts)
    if total == 0:
        raise ValueError("Total count cannot be zero")

    return ((c+g)/total) * 100


def format_report(sample: str, length: int, gc: float) -> str:
    """Return a one-line report with units, e.g. 'S1: 60 bases, GC 46.7%'."""
    return f"{sample}: {length} bases, GC {gc:.1f}%"


def parse_counts(text: str) -> tuple[int, int, int, int]:
    """Parse 'A C G T' counts separated by spaces or commas.

    Raises:
        ValueError: if there are not exactly four non-negative integers.
    """
    parts = text.replace(",", " ").split()
    if len(parts) != 4:
        raise ValueError("Exactly four integers are required")

    try:
        counts = tuple(int(part) for part in parts)
    except ValueError as exc:
        raise ValueError("All values must be whole numbers") from exc  

    if any(count < 0 for count in counts):
        raise ValueError("Counts cannot be negative")

    return counts
    