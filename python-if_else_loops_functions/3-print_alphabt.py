#!/usr/bin/python3
print("".join(
    "{:c}".format(c) for c in range(97, 123) if c not in (101, 113)
), end="")
