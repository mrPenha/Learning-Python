"""O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

    Lojas Quase Dois - Tabela de preços
    1 - R$ 1.99
    2 - R$ 3.98
    ...
    50 - R$ 99.50"""
import os
os.system('clear')

print('\nTABELA DE PREÇOS\n')
print('ITENS          VALOR')
print('--------------------')

inicio = 0
itens = 1
c = 50
while c > 0:
    valor = inicio+1.99
    if itens < 10:
        print(f'0{itens}          R$ {valor:.2f}')
        print('---------------------')
    else:
        print(f'{itens}          R$ {valor:.2f}')
        print('---------------------')
    itens += 1
    inicio = valor
    c -= 1
