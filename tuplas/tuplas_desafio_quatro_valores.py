import os
os.system('clear')

"""
DESAFIO
Desenvolva um programa que leia 4 valores e guarde-os em uma tupla. No final, mostre:
1 - Quantas vezes apareceu o valor 9
2 - Em que posição foi digitada o primeiro valor 3
3 - Quais foram os números pares
"""


def linha():
    print('-------------------------------------- \n\n')


valores = []

for i in range(4):
    n = int(input(f'Digite o {i+1}º valor: '))
    valores.append(n)
linha()

tupla = tuple(valores)

print('Quantas vezes apareceu o valor 9:', tupla.count(9))
linha()

if 3 in tupla:
    print('Em que posição foi digitada o primeiro valor 3:', tupla.index(3))
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
linha()

print('Quais foram os números pares:', end=' ')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
    else:
        pass
print()
linha()
