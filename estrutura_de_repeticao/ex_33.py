"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas."""
import os
os.system('clear')

print('DEPARTAMENTO ESTADUAL DE METEOROLOGIA \n\n(pressione uma letra para sair) \n')
print('-------------------------------------')

a = 0  # maior
b = 0  # menor
comeco_b = 0
soma = 0
media = 0
qtd = 0
while True:

    x = input('Insira a temperatura: ')
    if x.isnumeric():
        x = int(x)
    else:
        break

    if x > a:
        a = x
    else:
        a = a

    if comeco_b == 0:
        comeco_b += 1
        b = x
    else:
        if x < a and x < b:
            b = x
        else:
            b = b

    soma += x
    qtd += 1

media = soma / qtd
print(
    f'\nMaior temperatura: {a}°C \nMenor temperatura: {b}°C \nMédia temperatura: {media:.1f}°C \n')
