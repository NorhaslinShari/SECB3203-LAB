import pytest

from basics import  gc_percent, parse_counts

def test_all_gc():
    """Boundary case: all bases are G and C."""
    assert gc_percent(0, 50, 50, 0) == 100.0

def test_zero_total():
    """Zero-total case."""
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)

def test_counts_negative():
    """Invalid-input case."""
    with pytest.raises(ValueError):
        parse_counts("18, -12, 10, 20")
