def add_integer(a, b=98):
    """
    adds 2 integers
    a, b should be int or floar otherwise will raise a TypeError
    exception with the message a must be an integer or b must be an integer

    Returns an integer: the addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
