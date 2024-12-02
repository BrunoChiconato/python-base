#!/usr/bin/env python3
""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__author__ = "Bruno Chiconato"
__version__ = "0.0.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

aulas = ["inglês", "música", "dança"]

aluno_sala1_ingles = []
aluno_sala1_musica = []
aluno_sala1_danca = []

aluno_sala2_ingles = []
aluno_sala2_musica = []
aluno_sala2_danca = []

for aluno in sala1:
    if aluno in aula_ingles:
        aluno_sala1_ingles.append(aluno)
    if aluno in aula_musica:
        aluno_sala1_musica.append(aluno)
    if aluno in aula_danca:
        aluno_sala1_danca.append(aluno)

for aluno in sala2:
    if aluno in aula_ingles:
        aluno_sala2_ingles.append(aluno)
    if aluno in aula_musica:
        aluno_sala2_musica.append(aluno)
    if aluno in aula_danca:
        aluno_sala2_danca.append(aluno)

for aula in aulas:
    if aula == "inglês":
        print(f"Alunos da aula de {aula}:")
        print("Sala 1")

        for aluno in aluno_sala1_ingles:
            print(f"- {aluno}")

        print("Sala 2")
        for aluno in aluno_sala2_ingles:
            print(f"- {aluno}")
        
        print()
    elif aula == "música":
        print(f"Alunos da aula de {aula}:")
        print("Sala 1")

        for aluno in aluno_sala1_musica:
            print(f"- {aluno}")

        print("Sala 2")
        for aluno in aluno_sala2_musica:
            print(f"- {aluno}")
        
        print()
    elif aula == "dança":
        print(f"Alunos da aula de {aula}:")
        print("Sala 1")

        for aluno in aluno_sala1_danca:
            print(f"- {aluno}")

        print("Sala 2")
        for aluno in aluno_sala2_danca:
            print(f"- {aluno}")