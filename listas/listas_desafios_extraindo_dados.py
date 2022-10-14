import os
os.system('clear')

"""
Crie um programa que vai ler vários números e colocá-los em uma lista. Depois, mostre:
1 - Quantos números foram digitados
2 - A lista ordenada de forma Decrescente
3 - Se o valor 5 foi digitado e, se está ou não na lista
"""

valores = []

continuar = 's'

while continuar == 's':
    n = int(input('Digite o valor: '))
    if n not in valores:
        valores.append(n)

    else:
        print('\nValor já inserido')

    continuar = input('\nDeseja continuar? [S/N]: ')
    os.system('clear')

print(f'Valores = {valores} \n')
print(f'Foram digitados um total de {len(valores)} números. \n')
print(f'Ordem Decrescente: {sorted(valores, reverse=True)} \n')

if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')

print()
