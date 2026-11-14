import pytest

from normalize import cpm, proportions
from sequence_utils import  gc_content, reverse_complement


def test_reverse_complement_valid():
    assert reverse_complement("ACGTCCAT") == "ATGGACGT"


def test_proportions_does_not_change_input():
    counts = [20, 140, 40]
    original = counts.copy()

    proportions(counts)
    assert counts == original


def test_proportions_zero_total():
    with pytest.raises(ValueError):
        proportions([0, 0, 0])


def test_cpm_default_library_size():
    assert cpm([10, 20]) == [333333.3333333333, 666666.6666666666]
