"""Week 5 extension - side-effect-free normalisation functions."""


def proportions(counts: list[float]) -> list[float]:
    """Return each count divided by the total; the input is not changed.

    Raises:
        ValueError: if the total is zero (a list of zeros would look like data).
    """
    if counts == []:
        raise ValueError("Empty list")
    
    result = []
    total_counts = sum(counts)

    if total_counts == 0:
        raise ValueError("Total counts is zero")

    for count in counts:
        each = count/total_counts
        result.append(each)

    return result

def cpm(counts: list[float], library_size: float | None = None) -> list[float]:
    """Counts per million; library_size defaults to the sum of counts."""

    count_per_million = []

    if library_size is None:
            library_size = sum(counts)

    if library_size <= 0:
        raise ValueError("Library size cannot be zero or negative")

    for count in counts:
        each = (count/library_size) * 1000000
        count_per_million.append(each)

    return count_per_million

if __name__ == "__main__":
     print(proportions([20, 140, 40]))
     print(cpm([10,20], 100))
     

    
