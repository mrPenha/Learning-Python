"""Faça um programa que calcule o mostre a média aritmética de N notas."""
import os
os.system('clear')


print('MÉDIA ARITMÉTICA \n\n')

#  quantidade de notas
c = 0
while c < 1:
    qtd = input('Quantidade de notas a serem calculadas: ')

    if ',' not in qtd and '.' not in qtd:
        qtd = int(qtd)
        c = 1

    else:
        os.system('clear')
        print('Insira apenas números inteiros \n')
        c = 0

print()

#  Notas a serem inseridas e cálculo das notas
c = 0
soma = 0
media = 0
while c < qtd:
    nota = input(f'Insira a {c+1}ª nota: ')
    if ',' in nota:
        nota = nota.replace(',', '.')
        nota = float(nota)
    else:
        nota = float(nota)

    soma += nota
    c += 1

media = soma / qtd

print(f'\nMédia: {media}\n')
