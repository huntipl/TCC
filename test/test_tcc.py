import tcc
import pytest


@pytest.mark.parametrize("test_chunks", [1, 3, 5])
def test_empty_array_split_returns_empty_array(test_chunks):
    result = tcc.split_array([], test_chunks)
    expected = [[]]
    assert expected == result


@pytest.mark.parametrize("test_chunks", [0, -5])
def test_split_to_less_than_1_chunks_raises_valueerror_exception(test_chunks):
    with pytest.raises(ValueError):
        tcc.split_array([], test_chunks)