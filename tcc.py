def split_array(aray, n):
    if type(n) is not int:
        raise ValueError("n has to be an integer")
    if n < 1:
        raise ValueError("n has to be greater than 0")
    return [[]]
