# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print('O dobro da área de um quadrado')
lado = float(input('Insira o lado do quadrado: '))
area = lado ** 2
dobro = area * 2
print(f'A área do quadrado é de {area} cm². O dobro dessa área é de {dobro} cm²')