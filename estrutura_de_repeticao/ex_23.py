"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""
import os
os.system('clear')

print('Número primos entre 1 e N (N fornecido pelo usuário) \n\n')

num = input('Insira O valor de N: ')

if ',' not in num and '.' not in num:
    num = int(num)
else:
    print('Insira apenas números inteiros.')


os.system('clear')
print(f'\nNúmeros primos de entre 1 e {num}: \n')


a = 1
acumulador = 1
while True:

    total = 0
    for i in range(1, num + 1):
        if a % i == 0:
            total += 1

        else:
            total = total

    if total == 2:
        print(a, end=' ')

    else:
        pass

    a += 1
    i = 1
    acumulador += 1
    if acumulador == num+1:
        break

print('\n\nFIM \n')
