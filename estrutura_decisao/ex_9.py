"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))
print()

if c >= a and c >= b and b >= a:
    print(f'Ordem Decrescente: {c, b, a}')

elif a >= c and a >= b and c >= b:
    print(f'Ordem Decrescente: {a, c, b}')

else:
    print(f'Ordem Decrescente: {b, a, c}')
