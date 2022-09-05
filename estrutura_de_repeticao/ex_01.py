"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. """
print()

nota = int(input('Insira uma nota entre 0 e 10: \n> '))
print()

cont = 0
while nota < 0 or nota > 10:
    print('Nota Inválida \n')
    nota = int(input('Insira uma nota entre 0 e 10: \n> '))
    cont += 1
    print()

print()
