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
def test_input_array_is_type_of_array_list_set_etc(test_array):
    with pytest.raises(ValueError):
        tcc.split_array(test_array, 1)


@pytest.mark.parametrize("test_array, test_chunks, expected", [
    [[1, 2, 3], 3, [[1], [2], [3]]],
    [[1, 2, 3, 4], 2, [[1, 2], [3, 4]]],
    [['1', 2, 3.3, 4], 2, [['1', 2], [3.3, 4]]],
    ]
)
def test_array_dividing_without_remainder_splits_into_n_even_chunks(test_array, test_chunks, expected):
    assert expected == tcc.split_array(test_array, test_chunks)


@pytest.mark.parametrize("test_array, test_chunks, expected", [
    [[1, 2, 3], 2, [[1, 2], [3]]]]
)
def test_array_dividing_with_remainder_splits_into_n_minus_1_even_chunks_and_remainder_in_the_last_chunk(test_array, test_chunks, expected):
    assert expected == tcc.split_array(test_array, test_chunks)
