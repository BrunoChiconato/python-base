#!/usr/bin/env python3
"""
Make a program that print all even numbers between 1 and 200.

ex:
python numeros_pares.py
2
4
6
8
...
"""

for num in range(1, 201):
    if num % 2 == 0:
        print(num)