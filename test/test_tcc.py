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


@pytest.mark.parametrize("test_chunks", ['test', 1.1])
def test_chunks_not_a_integer_raises_valueerror_exception(test_chunks):
    with pytest.raises(ValueError):
        tcc.split_array([], test_chunks)


@pytest.mark.parametrize("test_array", [1.1, 4, set()])
def test_split_array(test_array):
    with pytest.raises(ValueError):
        tcc.split_array(test_array, 1)
