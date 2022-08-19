""" João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que
João deverá pagar. Imprima os dados do programa com as mensagens adequadas. """

regulamento = 50
excesso = 0
multa = 4.00
valor_a_pagar = 0

peso = float(input('Peso de peixes (casa decimal separada por ponto): '))

if peso > regulamento:
    print(f'Peso de Peixes: {peso}')
    excesso = peso - regulamento
    print(f'Excesso de peso: {excesso}')
    valor_a_pagar = excesso * multa
    print(f'Valor de multa a ser pago: R$ {valor_a_pagar:.2f}')

else:
    print(f'Peso de Peixes: {peso}')
    print(f'Valor de multa a ser pago: R$ 0,00')