#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new
tag: tech
text: Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""
__author__ = "Bruno Chiconato"
__version__ = "0.1.0"

import sys
import os

path = os.curdir
filepath = os.path.join(path, "notes.txt")
valid_cmds = ["new", "read"]
args = sys.argv[1:]

if not args:
    print(f"Invalid usage! You must specify a command: {valid_cmds}")
    sys.exit(1)

if args[0] not in valid_cmds:
    print(f"Invalid command '{args[0]}'")
    sys.exit(1)

if args[0] == "new":
    tag = input("tag: ").strip()
    text = input("text: ").strip()
    writer = f"{tag}:{text}"
    
    with open(filepath, "a") as file:
        file.write(f"{writer}\n")

elif args[0] == "read":
    placeholder, tag = args[1].split("=")
    with open(filepath) as file:
        lines = file.readlines()
        num_lines = 0
        for line in lines:
            num_lines += 1
            nametag, text = line.replace("\n","").split(":")
            if nametag == tag:
                print(text)
            else:
                print(f"No tag such as '{tag}' in line: {num_lines}")
