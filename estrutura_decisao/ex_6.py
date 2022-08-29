"""Faça um Programa que leia três números e mostre o maior deles. """

num1 = int(input('Insira o primeiro número: '))
print()
num2 = int(input('Insira o segundo número: '))
print()
num3 = int(input('Insira o terceiro número: '))
print()

if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior dos três números.')

elif num2 > num1 and num2 > num3:
    print(f'{num2} é o maior dos três números.')

else:
    print(f'{num3} é o maior dos três números.')
