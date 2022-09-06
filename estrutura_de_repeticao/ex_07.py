"""Faça um programa que leia 5 números e informe o maior número. """
print()

print('Você precisa informar 5 números \n\n')
maior = 0
cont = 0
while cont < 5:
    numero = int(input('Informe o número: '))

    if numero > maior:
        maior = numero
    else:
        maior = maior
    cont += 1

print()
print(f'O maior número informado foi {maior} \n')
