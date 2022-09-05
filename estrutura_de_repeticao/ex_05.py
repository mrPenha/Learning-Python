"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. """
import os

print()

print('TAXA DE CRESCIMENTO DA POPULAÇÃO \n\n')

while True:
    #  população inicial A
    a = input('Insira a População inicial de A sem pontuações: \n> ')
    if a.isnumeric():
        a = float(a)
        print()
    else:
        print('Dado Inválido!')
        quit()

    #  população inicial B
    b = input('Insira a População inicial de B sem pontuações: \n> ')
    if b.isnumeric():
        b = float(b)
        print()
    else:
        print('Dado Inválido!')
        quit()

    #  tx crescimento A
    tx_cresc_a = float(
        input('Insira a taxa de crescimento (%) de A (separar com ponto ".": \n> '))
    print()

    #  tx crescimento B
    tx_cresc_b = float(
        input('Insira a taxa de crescimento (%) de B (separar com ponto ".": \n> '))
    print()

    #  tempo de crescimento (em anos)
    anos = int(
        input('Em quantos anos gostaria de ver a taxa de crescimento? \n> '))
    print()

    #  cálculo da tx de crescimento
    cresc_a = (((a*tx_cresc_a)/100)+a)*anos
    cresc_b = (((a*tx_cresc_b)/100)+b)*anos

    #  formatação dos números

    #  população A
    a = f'{a:_.3f}'
    a = a.replace('.', ',').replace('_', '.')
    #  população B
    b = f'{b:_.3f}'
    b = b.replace('.', ',').replace('_', '.')

    #  taxa de crescimento A
    tx_cresc_a = f'{tx_cresc_a:_.2f}%'
    tx_cresc_a = tx_cresc_a.replace('.', ',').replace('_', '.')
    #  taxa de crescimento B
    tx_cresc_b = f'{tx_cresc_b:_.2f}%'
    tx_cresc_b = tx_cresc_b.replace('.', ',').replace('_', '.')

    #  crescimento de A
    cresc_a = f'{cresc_a:_.3f}'
    cresc_a = cresc_a.replace('.', ',').replace('_', '.')
    #  crescimento de B
    cresc_b = f'{cresc_b:_.3f}'
    cresc_b = cresc_b.replace('.', ',').replace('_', '.')

    #  imprime na tela
    print(f'População inicial: \nA = {a} \nB = {b} \n\n')
    print(f'Tx de Cres. Anual: \nA = {tx_cresc_a} \nB = {tx_cresc_b} \n\n')
    print(f'Tempo (em anos) de crescimento: {anos} \n\n')
    print(f'Crescimento da População: \nA = {cresc_a} \nB = {cresc_b} \n')
    print()

    sair = input('Gostaria de continuar? [S]/[N]: \n> ')
    sair = sair.lower()

    if sair != 's':
        break
    else:
        os.system('clear')


print()
