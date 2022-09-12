"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""
import os
os.system('clear')

x = 0
while x < 1:
    turmas = input('Quantidade de turmas: ')
    print()

    if ',' not in turmas and '.' not in turmas:
        turmas = int(turmas)
        x = 1

    else:
        os.system('clear')
        print('Insira apenas números inteiros \n')
        x = 0

media = 0
qtd_alunos = 0
c = 0
while c < turmas:
    alunos = int(input(f"Digite quantos alunos tem na turma {c + 1}: "))
    if alunos <= 40:
        qtd_alunos += alunos
        c += 1
    else:
        break


media = qtd_alunos / turmas
print(f"A media de alunos por turma é {media}")
