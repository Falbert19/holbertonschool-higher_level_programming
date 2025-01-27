#!/usr/bin/python3
def add_integer(a, b=98):
   """This module contains a function to add two integers

The function takes two arguments, `a` and `b` (with `b` defaulting to 98).
It casts both arguments to integers if they are floats, and raises a `TypeError`
if either of the arguments is not an integer or a float
"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
