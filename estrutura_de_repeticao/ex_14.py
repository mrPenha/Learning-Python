"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."""


print()

print('INSIRA 10 NÚMEROS INTEIROS \n\n')

par = 0
impar = 0
soma = 0
cont = 0
while cont < 5:

    num1 = int(input(f'Insira o {cont+1}º número: '))

    if num1 % 2 == 0:
        par += 1

    else:
        impar += 1

    soma += num1

    cont += 1
print()

print(f'Soma = {soma} \nNúmeros pares = {par} \nNúmeros impares = {impar}')
print()
