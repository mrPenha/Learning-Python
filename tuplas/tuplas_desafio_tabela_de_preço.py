import os
os.system('clear')

"""
DESAFIO
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados de forma tabular.
"""


def linha():
    print('*' * 45, '\n')


produtos = (
    'bolacha', 2.95,
    'café', 17.20,
    'leite', 4.90,
    'geleia', 3.25
)
print('*' * 45)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('*' * 45)
for i in range(len(produtos)):
    if i % 2 == 0:
        print(f'*  {produtos[i].upper():.<30}', end=' ')
    else:
        print(f'R$ {produtos[i]:>5.2f}  *')

linha()
