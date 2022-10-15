import os
import random
os.system('clear')

"""
Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista única que mantenha separados em valores pares e impares. No final mostre os valores em ordem crescente.
"""

valores = [[], []]


for i in range(5):
    n = (int(input(f'Insira o {i+1} valor: ')))

    if n % 2 != 0:
        valores[0].append(n)
    else:
        valores[1].append(n)


print(f'\n\nValores Impares: {sorted(valores[0])} \n')
print(f'Valores Pares: {sorted(valores[1])} \n')
