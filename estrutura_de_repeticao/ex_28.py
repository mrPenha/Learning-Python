"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""
import os
os.system('clear')

#  qtd CD's
x = 0
while x < 1:
    qtd_cds = input('Quantidade de turmas: ')
    print()

    if ',' not in qtd_cds and '.' not in qtd_cds:
        qtd_cds = int(qtd_cds)
        x = 1

    else:
        os.system('clear')
        print('Insira apenas números inteiros \n')
        x = 0
print()

media = 0
soma = 0
c = 0
while c < qtd_cds:
    valor = input(f'Insira o valor do {c+1}º CD: R$ ')
    if ',' in valor:
        valor = valor.replace(',', '.')
        valor = float(valor)
        soma += valor
        c += 1
    else:
        valor = float(valor)
        soma += valor
        c += 1

media = soma / qtd_cds
print(f'\nA média de valor gasta nos CDs foi de R$ {media:.2f} \n')
