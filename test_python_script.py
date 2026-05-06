"""
Test suite for python_script.py.

These tests use pytest to verify that:
- DNA sequence validation works correctly
- k-mer counting behaves as expected
- k-mer context tracking is accurate

This follows a test-driven development (TDD) approach.
"""

import python_script as ps


# TEST: validate_sequence

def test_validate_sequence_valid():
    """
    Test that a valid DNA sequence passes validation.
    """
    assert ps.validate_sequence("ACGTACGT", 2) is True


def test_validate_sequence_invalid_chars():
    """
    Test that a sequence with invalid characters fails validation.
    """
    assert ps.validate_sequence("ACGTXYZ", 2) is False


def test_validate_sequence_too_short():
    """
    Test that sequences shorter than k+1 are rejected.
    """
    assert ps.validate_sequence("ACG", 5) is False


# TEST: update_kmer_count

def test_update_kmer_count():
    """
    Test that a single k-mer update correctly records:
    - total k-mer count
    - next character frequency
    """
    data = {}

    ps.update_kmer_count(data, "AT", "G")

    assert data["AT"]["count"] == 1
    assert data["AT"]["next_chars"]["G"] == 1


def test_update_kmer_count_multiple():
    """
    Test that repeated updates accumulate counts correctly.
    """
    data = {}

    ps.update_kmer_count(data, "AT", "G")
    ps.update_kmer_count(data, "AT", "G")
    ps.update_kmer_count(data, "AT", "C")

    assert data["AT"]["count"] == 3
    assert data["AT"]["next_chars"]["G"] == 2
    assert data["AT"]["next_chars"]["C"] == 1



# TEST: count_kmers_with_context

def test_count_kmers_with_context():
    """
    Test that k-mer extraction correctly identifies:
    - k-mers in a sequence
    - following character relationships
    """
    data = {}

    result = ps.count_kmers_with_context("ATG", 2, data)

    assert "AT" in result
    assert result["AT"]["next_chars"]["G"] == 1
    
def test_empty_sequence():
    """
    Empty sequence should produce no k-mers.
    """
    data = {}
    result = ps.count_kmers_with_context("", 2, data)
    assert result == {}
    
def test_sequence_too_short_for_k():
    """
    Sequence too short should produce no k-mer counts.
    """
    data = {}
    result = ps.count_kmers_with_context("A", 2, data)
    assert result == {}
    
def test_k_equals_one():
    """
    k=1 should still correctly track single-base k-mers.
    """
    data = {}
    result = ps.count_kmers_with_context("AT", 1, data)

    assert "A" in result
    assert result["A"]["next_chars"]["T"] == 1

def test_repeated_sequence():
    """
    Repeated nucleotides should accumulate counts correctly.
    """
    data = {}
    ps.count_kmers_with_context("AAAA", 1, data)

    assert data["A"]["count"] == 3
