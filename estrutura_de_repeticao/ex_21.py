"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1."""
import os
os.system('clear')

num = int(input('Insira um número: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        total += 1

    else:
        pass

if total == 2:
    print(f'\nEste número é primo\n')

else:
    print(f'\nEste número não é primo\n')

# print(f'\nO número foi divisível {total} vezes\n')
