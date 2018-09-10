import collections
import math


def sanitize_input(func):
    """Checks for array being type collection and positive integer n"""

    def func_wrapper(array, n):
        if not isinstance(array, collections.Sequence):
            raise ValueError("array has to be array or list")
        if not isinstance(n, int):
            raise ValueError("n has to be an integer")
        if n < 1:
            raise ValueError("n has to be greater than 0")
        return func(array, n)
    return func_wrapper


@sanitize_input
def split_array(array, n):
    """"Returns the input array split into n chunks
    :type array: collections.Sequence
    :type n: int
    """

    array_size = len(array)
    max_chunk_size = int(math.ceil(array_size/n))

    if array_size == 0:
        return [[]]

    return [array[i:i+max_chunk_size] for i in range(0, array_size, max_chunk_size)]
