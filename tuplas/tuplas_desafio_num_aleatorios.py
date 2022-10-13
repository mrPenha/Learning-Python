import os
import random
import string
os.system('clear')

"""
DESAFIO
Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números e também indique o menor e o maior valor que estão na tupla.
"""


def linha():
    print('--------------------------------------- \n\n')


numeros = []
for i in range(5):
    n = (random.randint(1, 1000))
    numeros.append(n)

numeros = tuple(numeros)

print(f'Os números gerados foram: {numeros}')
linha()

print(f'Maior = {max(numeros)}')
linha()

print(f'Menor = {min(numeros)}')
linha()
