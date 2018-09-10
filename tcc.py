import collections


def split_array(array, n):
    """"Returns the input array split into n chunks"""

    if not isinstance(array, collections.Sequence):
        raise ValueError("array has to be array or list")
    if not isinstance(n, int):
        raise ValueError("n has to be an integer")
    if n < 1:
        raise ValueError("n has to be greater than 0")

    return [[]]
