"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""

from math import sqrt


print('EQUAÇÃO DO SEGUNDO GRAU, NA FORMA ax² + bx + c')

print()

a = int(input('Insira o valor de A: '))

if a == 0:
    print('A equação não é de segundo grau.')
    print()
    quit()


else:
    b = int(input('Insira o valor de B: '))
    c = int(input('Insira o valor de C: '))
    print()

#  valor de delta
delta = b**2-4*a*c
print(f'Delta = {delta}')
print()


#  saída
if delta < 0:
    print(f'A equação NÃO possui raizes reais')
    print()

elif delta == 0:
    raiz = -(-b) / (2*a)
    print(f'A equação POSSUI apenas uma raiz real {raiz}')
    print()

else:
    raiz1 = ((-b + sqrt(delta)) / (2*a))
    raiz2 = ((-b - sqrt(delta)) / (2*a))
    print('A equação POSSUI duas raizes reais:')
    print(f'Raizes: {raiz1} e {raiz2}')
    print()
