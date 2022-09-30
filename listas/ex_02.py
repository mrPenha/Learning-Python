import os
import random
os.system('clear')

"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""
vetor_reais = []

for i in range(10):
    n = input('Insira um número real: ')
    if ',' in n:
        n = n.replace(',', '.')
        n = float(n)
        vetor_reais.append(n)
    else:
        n = int(n)
        vetor_reais.append(n)

print()

print(vetor_reais, '\n')

vetor_reais.reverse()

print(vetor_reais, '\n')
