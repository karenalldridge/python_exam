import python_script as ps


def test_validate_sequence_valid():
    assert ps.validate_sequence("ACGTACGT", 2) is True


def test_validate_sequence_invalid_chars():
    assert ps.validate_sequence("ACGTXYZ", 2) is False


def test_validate_sequence_too_short():
    assert ps.validate_sequence("ACG", 5) is False


def test_update_kmer_count():
    data = {}
    ps.update_kmer_count(data, "AT", "G")

    assert data["AT"]["count"] == 1
    assert data["AT"]["next_chars"]["G"] == 1


def test_count_kmers_with_context():
    data = {}
    result = ps.count_kmers_with_context("ATG", 2, data)

    assert "AT" in result
    assert result["AT"]["next_chars"]["G"] == 1
