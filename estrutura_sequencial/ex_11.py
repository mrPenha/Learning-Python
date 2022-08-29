# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     o produto do dobro do primeiro com metade do segundo .
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo. 
print('Calculo de números inteiros e reais')
n1 = int(input('1º Número inteiro: '))
n2 = int(input('2º Número inteiro: '))
n3 = float(input('Número real: '))
print()
print (f'Produto do dobro do primeiro com metade do segundo: {(n1 * 2) * (n2 / 2)}')
print (f'Soma do triplo do primeiro com o terceiro: {n1 * 3 + n3}')
print (f'Terceiro elevado ao cubo: {n3 ** 3}')