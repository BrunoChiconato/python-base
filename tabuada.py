#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
---------------
Tabuada do 2
2
4
6
...
"""
__version__ = "0.0.1"
__author__ = "Bruno Chiconato"

numbers = list(range(1, 11))

for number in numbers:
    print("Tabuada do:", number)
    for multiplier in numbers:
        print(multiplier * number)
    print("------------")
