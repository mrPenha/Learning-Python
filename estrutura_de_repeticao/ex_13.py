"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem."""
print()

print('CÁLCULO DE EXPONENCIAÇÃO \n\n')

num1 = float(input('Insira a base: '))
num2 = int(input('Insira o expoente: '))

r = num1**num2

if num1 % 2 == 0:
    num1 = int(num1)
else:
    num1 = float(num1)

if r % 2 == 0:
    r = int(r)
else:
    r = r

print(f'{num1}^{num2} = {r}')
