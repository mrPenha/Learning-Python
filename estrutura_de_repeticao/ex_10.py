"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."""
print()

print('INTERVALO ENTRE NÚMEROS \n\n')

num1 = int(input('Informe um inicial inteiro: '))
num1 = num1 + 1
num2 = int(input('Informe um final inteiro: '))

print()

for i in range(num1, num2):
    print(i)
