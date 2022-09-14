"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

    Os juros e a quantidade de parcelas seguem a tabela abaixo:

    Quantidade de Parcelas      % de Juros sobre o valor inicial da dívida
    1                           0
    3                           10
    6                           15
    9                           20
    12                          25

    Exemplo de saída do programa:

    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67"""
import os
os.system('clear')

divida = input('Valor dívida: R$ ')
if ',' in divida:
    divida = divida.replace(',', '.')
    divida = float(divida)
else:
    divida = float(divida)
print()

os.system('clear')

print('Valor Dívida | Valor Juros | Qtde Parcelas | Valor Parcela')
print('----------------------------------------------------------')


valor_divida = 0
valor_juros = 0
valor_parcela = 0
qtd_parcelas = 1
max_parcela = 12
c = 1
while c <= max_parcela:
    if c == 1:
        valor_juros = (divida * 0)/100
        valor_divida = divida + valor_juros
        qtd_parcelas = c
        valor_parcela = valor_divida / qtd_parcelas
        print(f'{valor_divida:.2f}        {valor_juros:.2f}          {qtd_parcelas}               {valor_parcela:.2f}')

    elif c == 3:
        valor_juros = (divida * 10)/100
        valor_divida += valor_juros
        qtd_parcelas = c
        valor_parcela = valor_divida / qtd_parcelas
        print(f'{valor_divida:.2f}        {valor_juros:.2f}        {qtd_parcelas}               {valor_parcela:.2f}')

    elif c == 6:
        valor_juros = (divida * 15)/100
        valor_divida += valor_juros
        qtd_parcelas = c
        valor_parcela = valor_divida / qtd_parcelas
        print(f'{valor_divida:.2f}        {valor_juros:.2f}        {qtd_parcelas}               {valor_parcela:.2f}')

    elif c == 9:
        valor_juros = (divida * 20)/100
        valor_divida += valor_juros
        qtd_parcelas = c
        valor_parcela = valor_divida / qtd_parcelas
        print(f'{valor_divida:.2f}        {valor_juros:.2f}        {qtd_parcelas}               {valor_parcela:.2f}')

    elif c == 12:
        valor_juros = (divida * 25)/100
        valor_divida += valor_juros
        qtd_parcelas = c
        valor_parcela = valor_divida / qtd_parcelas
        print(f'{valor_divida:.2f}        {valor_juros:.2f}        {qtd_parcelas}              {valor_parcela:.2f}')

    else:
        pass

    c += 1

print()
