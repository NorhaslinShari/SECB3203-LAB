"""Lab 4 - lists and tuples for a gene panel and variant records."""
from typing import NamedTuple


class Variant(NamedTuple):
    """One variant coordinate: an immutable record with named fields."""

    chrom: str  #cannot change the value of the field after the object is created
    pos: int
    ref: str
    alt: str


def filter_panel(genes: list[str], priority: set[str]) -> list[str]:
    """Keep the genes that are in priority, preserving the original order."""
# save list of gene that are in priority list
    result = []
 
    for i in genes:
        if i in priority: # dalam set, so boleh check terus
                result.append(i)
    return result


def sorted_copy(items: list) -> list:
    """Return a sorted copy; the original list is not changed."""
    result = sorted(items) #way to sort the list and return a new list  
    return result 


def _chrom_key(chrom: str) -> tuple:
    chrom = chrom.removeprefix("chr")  # Remove "chr" prefix if present
    if chrom.isdigit():
         return(0, int(chrom))  # Numeric chromosomes come first

    order = {"X": 23, "Y": 24, "M": 25}  # Order for non-numeric chromosomes
    return (1, order[chrom])


def sort_variants(variants: list[Variant]) -> list[Variant]:
    """Sort by chromosome (1-22, X, Y, M) and then by position."""
    variant = sorted(variants, key=lambda v: (_chrom_key(v.chrom), v.pos))  # Sort by chromosome then by position (pos is for int, chrom (str))
    return variant             # key = ... For every Variant v, calculate a value and sort using that value
