import collections
import math


def split_array(array, n):
    """"Returns the input array split into n chunks"""

    if not isinstance(array, collections.Sequence):
        raise ValueError("array has to be array or list")
    if not isinstance(n, int):
        raise ValueError("n has to be an integer")
    if n < 1:
        raise ValueError("n has to be greater than 0")

    array_size = len(array)
    max_chunk_size = int(math.ceil(array_size/n))

    print(array_size, max_chunk_size)

    if array_size == 0:
        return [[]]

    return [array[i:i+max_chunk_size] for i in range(0, array_size, max_chunk_size)]
