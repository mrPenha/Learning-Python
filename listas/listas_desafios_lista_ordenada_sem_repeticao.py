import os
os.system('clear')

"""
Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.
"""


valores = []

for i in range(5):
    n = int(input('Insira o valor: '))
    if i == 0:
        valores.append(n)

    elif n > valores[-1]:
        valores.append(n)

    else:
        valores.insert(0, n)

print(valores)
