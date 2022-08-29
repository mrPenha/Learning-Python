"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""

produto1 = float(input('Insira o preço do primeiro produto: R$ '))
print()
produto2 = float(input('Insira o preço do segundo produto: R$ '))
print()
produto3 = float(input('Insira o preço do terceiro produto: R$ '))
print()

if produto1 < produto2 and produto1 < produto3:
    print(f'Você deve comprar o produto com o valor de R$ {produto1:.2f}')

elif produto2 < produto1 and produto2 < produto3:
    print(f'Você deve comprar o produto com o valor de R$ {produto2:.2f}')

else:
    print(f'Você deve comprar o produto com o valor de R$ {produto3:.2f}')
