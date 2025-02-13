#!/usr/bin/env python3
"""Calculadora prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em 'prefixcalc.log'
"""
__author__ = "Bruno Chiconato"
__version__ = "0.1.1"

import os
import sys
from datetime import datetime

valid_input = len(sys.argv)
file_path = os.path.join(os.curdir, "prefixcalc.log")

if valid_input == 4:
    operation, n1, n2 = sys.argv[1:]
    operation = operation.strip().lower()
    n1 = float(n1.strip())
    n2 = float(n2.strip())
    if operation == "sum":
        print(f"{n1 + n2}")
    elif operation == "sub":
        print(f"{n1 - n2}")
    elif operation == "mul":
        print(f"{n1 * n2}")
    elif operation == "div":
        print(f"{n1 / n2}")
    else:
        print(f"'{operation}' não é válido! Tente novamente.")
        sys.exit(1)
elif valid_input == 1:
    operation = input("Operação: ")
    operation = operation.strip().lower()
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    if operation == "sum":
        print(f"{n1 + n2}")
    elif operation == "sub":
        print(f"{n1 - n2}")
    elif operation == "mul":
        print(f"{n1 * n2}")
    elif operation == "div":
        print(f"{n1 / n2}")
    else:
        print(f"'{operation}' não é válido! Tente novamente.")
        sys.exit(1)
else:
    print("Erro")
    sys.exit(1)

timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

with open(file_path, "a") as file:
    file.write(f"{timestamp} | {user} | {operation}, {n1}, {n2}\n")
