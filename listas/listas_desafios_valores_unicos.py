import os
os.system('clear')

"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista, não será adicionado. No final exibir todos os valores digitados em ordem crescente.
"""

valores = []

continuar = 's'

while continuar == 's':
    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
    else:
        print('\nValor já existe. \n')

    continuar = input('\nDeseja continuar [S/N]: ').lower()
    os.system('clear')


print(f'Valores informados: {sorted(valores)} \n')
