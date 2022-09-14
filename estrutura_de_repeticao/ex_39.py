"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas."""
import os
os.system('clear')

n_alt = 0
n_bxo = 0
alto = 0
baixo = 0
c = 0
while c < 5:
    numero = int(input('Número do aluno: '))
    altura = int(input('Altura do aluno(cm): '))
    print()

    if altura > alto:
        alto = altura
        n_alt = numero
    else:
        alto = alto

    if baixo == 0:
        baixo = altura
    else:
        if altura < alto:
            baixo = altura
            n_bxo = numero
        else:
            baixo = baixo

    c += 1

print(f'\nMais Alto \nNúmero: {n_alt} \nAltura: {alto}')
print(f'\nMais Baixo \nNúmero: {n_bxo} \nAltura: {baixo}\n')
