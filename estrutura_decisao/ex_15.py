"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;"""

lado1 = float(input('Insira o lado 1 do triângulo: '))
lado2 = float(input('Insira o lado 2 do triângulo: '))
lado3 = float(input('Insira o lado 3 do triângulo: '))

print()

if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
    print('Este é um triângulo Equilátero. Três lados iguais.')

elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print('Este é um triângulo Isósceles. Dois lados iguais.')

else:
    print('Este é um triângulo Escaleno. Três lados diferentes.')

print()
