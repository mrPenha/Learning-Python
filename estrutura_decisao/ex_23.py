"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento."""

print()

numero = float(input('Insira um número: '))

if numero // 1 == numero:
    print(numero)
    print('Este é um número inteiro')

else:
    print('Este é um número decimal.')

print()
