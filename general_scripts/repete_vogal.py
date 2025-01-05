#!/usr/bin/env python3
"""
Vowel Repeater

Make a program that asks for one or more words and then duplicates each vowel in the word(s).

ex:
python repete_vogal.py
'Enter a word (or press enter to finish):' hello
'Enter a word (or press enter to finish):' world
'Enter a word (or press enter to finish):' <enter>
heelloo
woorld
"""

words_list = []
vowels = "aeiouAEIOU"

while True:
    word = input("Enter a word (or press enter to finish): ").strip()

    if word == "":
        break

    if any(letter.isnumeric() or letter.isdigit() for letter in word):
        print("Please enter a valid word.")
    else:
        words_list.append(word)


for word in words_list:
    for letter in word:
        if letter in vowels:
            print(letter * 2, end="")
        else:
            print(letter, end="")
    print()
