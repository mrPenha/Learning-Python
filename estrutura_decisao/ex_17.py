"""Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto."""

#  Obs1: O ano bissexto foi feito por Augusto, imperador de Roma em 8 d.C., fevereiro tinha 24 dias.
#  Obs2: Em 1582 o Papa Gregório modificou o mês de feverêiro para 29 dias.

ano = int(input("Insira o ano: "))

if ano < 1:
    print('Ano inválido')

if ano % 4 == 0:
    print('Esse ano é/foi Bissexto.')

else:
    print('Esse ano não é/foi Bissexto.')
