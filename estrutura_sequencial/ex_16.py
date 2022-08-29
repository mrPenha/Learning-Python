"""Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

import os

print('Bem-vindo(a) a PRATES & PENHA')
print()
print('Insira a opção desejada abaixo\n')
print('1 - Tamanho em M² (metros quadrados)')
print('2 - Descobrir o tamanho em M² (metros quadrados)')
print('\nObs: Para a segunda opção é necessário saber a medida do comprimento e da largura da área a ser pintada.')
op = int(input('Opção: '))
print()

if op == 1:
    #  tamanho em metros quadrados da área a ser pintada.
    tamanho = float(input('Tamanho em M²: '))

    #  1 litro para cada 3 metros quadrados
    #  lata = 18 litros

    litros = tamanho / 3.0
    latas = int(litros / 18.0)
    if litros % 18 != 0:
        latas += 1

    print('Voce deverá comprar', latas, 'latas.')
    print('O valor total é:', latas * 80.00)

if op == 2:
    comp = float(input('Insira o comprimento: '))
    larg = float(input('Insira a largura: '))
    tamanho = comp * larg

    litros = tamanho / 3.0
    latas = int(litros / 18.0)
    if litros % 18 != 0:
        latas += 1

    print('Voce deverá comprar', latas, 'latas.')
    print('O valor total é:', latas * 80.00)

print()
print('Obrigado por comprar na PRATES & PENHA')
