"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada."""
import os
os.system('clear')


print('MÉDIA DE IDADE \n\n')

#  quantidade de pessoas
c = 0
while c < 1:
    qtd = input('Quantidade de pessoas: ')

    if ',' not in qtd and '.' not in qtd:
        qtd = int(qtd)
        c = 1

    else:
        os.system('clear')
        print('Insira apenas números inteiros \n')
        c = 0

print()

#  idades
c = 0
soma = 0
media = 0
while c < qtd:
    idade = input(f'Insira a {c+1}ª idade: ')

    if ',' not in idade and '.' not in idade:
        idade = int(idade)
        soma += idade
        c += 1
    else:
        os.system('clear')
        print('Insira apenas números inteiros \n')
        c = 0

media = soma / qtd

print('\nCLASSIFICAÇÃO DE ACORDO COM A MÉDIA\n')
print('IDADE        CLASSE')
print('-------------------')
print('0-25          Jovem')
print('-------------------')
print('26-60        Adulta')
print('-------------------')
print('60+           Idosa')
print('-------------------\n')

print(f'Média de idades: {media}\n')

if media > 60:
    print('A turma é IDOSA')
elif media > 25:
    print('A turma é ADULTA')
else:
    print('A turma é JOVEM')

print()
