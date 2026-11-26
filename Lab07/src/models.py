"""Week 7 - classes for biological sequences and samples."""
from sequence_utils import find_motif, gc_content, is_valid_dna, reverse_complement


class DNASequence:
    """A validated, read-only DNA sequence with a name."""

    def __init__(self, name: str, sequence: str):
        sequence = sequence.upper()
        if not is_valid_dna(sequence):
            raise ValueError(
                f"invalid DNA sequence for {name!r}: {sequence!r}")
        self._name = name
        self._sequence = sequence


    @classmethod
    def from_fasta_record(cls, record_id: str, sequence: str) -> "DNASequence":
        """Build an object from a (record_id, sequence) pair such as read_fasta yields."""
        return cls(record_id, sequence)

    @property
    def name(self) -> str:
        return self._name

    @property
    def sequence(self) -> str:
        return self._sequence

    def gc_content(self) -> float:
        return gc_content(self._sequence)

    def reverse_complement(self) -> "DNASequence":
        return DNASequence(f"{self._name}_rc", reverse_complement(self._sequence))

    def find_motif(self, motif: str) -> list[int]:
        raise NotImplementedError("TODO: implement find_motif")

    def __len__(self) -> int:
        raise NotImplementedError("TODO: implement __len__")

    def __repr__(self) -> str:
        raise NotImplementedError("TODO: implement __repr__")

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("TODO: implement __eq__")

    def __hash__(self) -> int:
        raise NotImplementedError("TODO: implement __hash__")


class BiologicalSample:
    """Sample metadata plus a validated sequence and analysis results (composition)."""

    def __init__(self, sample_id: str, group: str, dna: DNASequence):
        raise NotImplementedError("TODO: implement __init__")

    def add_result(self, name: str, value) -> None:
        raise NotImplementedError("TODO: implement add_result")

    @property
    def results(self) -> dict:
        """A copy, so callers cannot change the stored results by accident."""
        raise NotImplementedError("TODO: implement results")

    def to_dict(self) -> dict:
        raise NotImplementedError("TODO: implement to_dict")


class SampleCollection:
    """An ordered collection of samples with unique ids."""

    def __init__(self):
        raise NotImplementedError("TODO: implement __init__")

    def add(self, sample: BiologicalSample) -> None:
        raise NotImplementedError("TODO: implement add")

    def __len__(self) -> int:
        raise NotImplementedError("TODO: implement __len__")

    def __iter__(self):
        raise NotImplementedError("TODO: implement __iter__")

    def by_group(self, group: str) -> list[BiologicalSample]:
        raise NotImplementedError("TODO: implement by_group")

    def summary(self) -> dict[str, int]:
        """Number of samples per group, sorted by group name."""
        raise NotImplementedError("TODO: implement summary")
