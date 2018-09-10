import tcc


def test_empty_array_returns_empty_array():
    result = tcc.split_array([],1)
    expected = [[]]
    assert expected == result