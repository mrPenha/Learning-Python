"""Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo."""
import os
os.system('clear')

print('Para finalizar digite um número negativo \n\n')

a = 0
b = 0
c = 0
d = 0
while True:
    numero = input('Insira um número positivo: ')
    if ',' in numero:
        numero = numero.replace(',', '.')
        numero = float(numero)
    else:
        numero = int(numero)

    if numero < 0:
        break
    else:

        if numero <= 25:
            a += 1

        elif numero <= 50:
            b += 1

        elif numero <= 75:
            c += 1

        elif numero <= 100:
            d += 1

        else:
            pass

print('\nINTERVALOR DE NÚMEROS\n')
print('Intervalo          QTDE')
print('-----------------------')
print(f'[0-25]             {a}')
print(f'[26-50]            {b}')
print(f'[51-75]            {c}')
print(f'[76-100]           {d}')
print('----------------------- \n')
