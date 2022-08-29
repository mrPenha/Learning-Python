"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. """

num1 = int(input('Insira um número. Esse número pode ser positivo ou negativo.: '))
print()

if num1 < 0:
    print(f'{num1} é um número negativo.')
elif num1 == 0:
    print(f'{num1} é um número neutro.')
else:
    print(f'{num1} é um número positivo.')
