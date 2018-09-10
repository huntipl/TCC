import tcc
import pytest


@pytest.mark.parametrize("test_chunks",[1,3,5])
def test_empty_array_split_returns_empty_array(test_chunks):
    result = tcc.split_array([],test_chunks)
    expected = [[]]
    assert expected == result


def test_split_to_0_chunks_raises_valueerror_exception():
    with pytest.raises(ValueError):
        tcc.split_array([],0)