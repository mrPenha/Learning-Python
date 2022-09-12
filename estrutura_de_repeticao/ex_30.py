"""O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

    Preço do pão: R$ 0.18
    Panificadora Pão de Ontem - Tabela de preços
    1 - R$ 0.18
    2 - R$ 0.36
    ...
    50 - R$ 9.00"""
import os
os.system('clear')

#  preço do pão
while True:
    preco_pao = input('Preço do pão: R$ ')
    if ',' in preco_pao:
        preco_pao = preco_pao.replace(',', '.')
        preco_pao = float(preco_pao)
        break
    else:
        preco_pao = float(preco_pao)
        break


print('\nTABELA DE PREÇOS\n')
print('QTDE           VALOR')
print('--------------------')

inicio = 0
quantidade = 1
c = 50
while c > 0:
    valor = inicio+preco_pao
    if quantidade < 10:
        print(f'0{quantidade}          R$ {valor:.2f}')
        print('---------------------')
    else:
        print(f'{quantidade}          R$ {valor:.2f}')
        print('---------------------')
    quantidade += 1
    inicio = valor
    c -= 1
