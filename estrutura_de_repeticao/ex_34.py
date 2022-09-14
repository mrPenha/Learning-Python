"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo."""
import os
os.system('clear')


while True:
    num = input('Insira um número: ')

    if ',' not in num and '.' not in num:
        num = int(num)

        total = 0

        for i in range(1, num + 1):
            if num % i == 0:
                total += 1

            else:
                pass

        if total == 2:
            print(f'\nEste número é primo\n')
            break

        else:
            print(f'\nEste número não é primo\n')
            break

    else:
        os.system('clear')
        print('\nInsira apenas números inteiros\n')
