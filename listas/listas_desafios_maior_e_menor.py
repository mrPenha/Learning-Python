import os
os.system('clear')


"""
DESAFIO
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor e suas respectivas posições na lista.
"""

valores = []
maior = 0
menor = 0

for i in range(5):
    valores.append(int(input(f'Digite o valor na posição {i}: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print()
print('=--' * 30, '\n')
print(f'Os valores digitados foram: {valores} \n')

print(f'O maior valor foi o {maior} nas posições ', end='')
for i, j in enumerate(valores):
    if j == maior:
        print(f'{i}...', end='')

print(f'\nO menor valor foi o {menor} nas posições ', end='')
for i, j, in enumerate(valores):
    if j == menor:
        print(f'{i}...', end='')

print()
