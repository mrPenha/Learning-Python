"""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário. """
import os
os.system('clear')

print('Número primos entre 1 e N (N fornecido pelo usuário) \n\n')

c = 0
while c < 1:

    num = input('Insira O valor de N: ')

    if ',' not in num and '.' not in num:
        num = int(num)
        c = 1

    else:
        os.system('clear')
        print('Insira apenas números inteiros \n')
        c = 0


os.system('clear')
print(f'\nNúmeros primos de entre 1 e {num}: \n')


a = 1
acumulador = 1
divisoes = 0
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
        total = total

    a += 1
    i = 1

    acumulador += 1
    if acumulador == num+1:
        break


print('\n')
