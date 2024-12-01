#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---

    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
...
##################
---Tabuada do 2---

    2 x 1 = 1
    2 x 2 = 4
    2 x 3 = 6
...
"""
__version__ = "0.0.2"
__author__ = "Bruno Chiconato"

numbers = list(range(1, 11))

for number in numbers:
    header = f"Tabuada do {number}"
    len_header = len(header) + 6
    print(f"{header:-^{len_header}}\n")

    for multiplier in numbers:
        result = number * multiplier
        msg = f"{number} x {multiplier} = {result}"
        print(f"{msg:^{len_header}}")

    print("\n", "#" * len_header)
