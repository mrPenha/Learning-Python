"""Faça um programa que leia 5 números e informe a soma e a média dos números."""
print()

soma = 0
cont = 0
while cont < 5:
    numero = int(input('Informe o número: '))
    soma += numero
    cont += 1

    media = soma/5

print()
print(f'Soma = {soma}')
print(f'Média = {media}')
print()
