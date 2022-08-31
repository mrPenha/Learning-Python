"""Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido."""

numero = int(input('Digite um número de 1 a 7: '))
print()


if numero == 1:
    print('1 - Domingo')

elif numero == 2:
    print('2 - Segunda Feira')

elif numero == 3:
    print('3 - Terça Feira')

elif numero == 4:
    print('4 - Quarta Feira')

elif numero == 5:
    print('5 - Quinta Feira')

elif numero == 6:
    print('6 - Sexta Feira')

else:
    print('7 - Sábado')

print()
