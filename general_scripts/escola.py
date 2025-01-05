#!/usr/bin/env python3
""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__author__ = "Bruno Chiconato"
__version__ = "0.1.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

dict_classes = {"Ingles": aula_ingles, "Musica": aula_musica, "Danca": aula_danca}

for classes, students in dict_classes.items():
    print(f"Alunos da atividade de {classes}\n")
    print("-" * 40)

    students_classroom_1 = set(sala1) & set(students)
    students_classroom_2 = set(sala2) & set(students)

    print(f"Sala 1 {students_classroom_1}")
    print(f"Sala 2 {students_classroom_2}\n")

    print("#" * 40)
