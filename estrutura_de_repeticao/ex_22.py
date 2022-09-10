"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível."""
import os
os.system('clear')

print('Números primos são números divisíveis por 1 e por ele mesmo\n\n')

while True:
    num = input('Insira um número: ')
    os.system('clear')

    print('\nO número é divisível por: \n')

    if ',' not in num and '.' not in num:
        num = int(num)

        total = 0
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=' ')
                total += 1

            else:
                total = total

        if total == 2:
            os.system('clear')
            print(f'\nO número {num} É primo.\n')
            break

        else:
            print(f'\n\nO número {num} NÃO É primo.\n')
            break

    else:
        os.system('clear')
        print('\nInsira apenas números inteiros\n')

print()
