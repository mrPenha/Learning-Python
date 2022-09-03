"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e
depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
    uma nota de 5 e quatro notas de 1."""

nota1 = 1
nota5 = 5
nota10 = 10
nota50 = 50
nota100 = 100

print()
print('\tCAIXA ELETRÔNICO')
print()
print('Saque mínimo de R$ 10,00 e máximo de R$ 600,00')
print()
print('NOTAS DISPONÍVEIS: 1, 5, 10, 50 e 100')
print()
print()


valor = int(input('Valor: R$ '))
if valor < 10 or valor > 600:
    print('O valor do saque é INFERIOR ou SUPERIOR ao permitido')
    quit()

unidade = valor % 10
dezena = ((valor-unidade)//10) % 10
centena = valor // 100

print()
print()

print('NOTAS          QUANTIDADE')
print('-------------------------')

#  notas de 100
if centena < 10:
    notas_de_cem = (centena * nota100)//nota100
    print(f'R$ 100,00          :{notas_de_cem}')
    print()

#  notas de 50 + notas de 10
if dezena > 5 and dezena < 10:
    notas_de_cinquenta = nota50//nota50
    notas_de_dez = dezena - 5
    print(f'R$  50,00          :{notas_de_cinquenta}')
    print()
    print(f'R$  10,00          :{notas_de_dez}')
    print()

#  notas de 50
if dezena == 5:
    notas_de_cinquenta = nota50//nota50
    print(f'R$  50,00          :{notas_de_cinquenta}')
    print()

#  notas de 10
if dezena > 1 and dezena < 5:
    notas_de_dez = nota10
    print(f'R$  10,00          :{notas_de_dez}')
    print()

#  notas de 5 + notas de 1
if unidade > 5 and unidade < 10:
    notas_de_cinco = nota5//nota5
    notas_de_um = unidade - 5
    print(f'R$   5,00          :{notas_de_cinco}')
    print()
    print(f'R$   1,00          :{notas_de_um}')
    print()

#  nota de 5
if unidade == 5:
    notas_de_cinco = nota5//nota5
    print(f'R$   5,00          :{notas_de_cinco}')
    print()

if unidade < 5:
    notas_de_um = nota1//nota1
    print(f'R$   1,00          :{notas_de_um}')
    print()

print()
