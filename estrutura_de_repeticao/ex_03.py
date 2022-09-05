"""Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';"""
import os
print()

#  começa entrada de dados
nome = input('Nome: ')
nome = nome.lower()
print()

idade = int(input('Idade: '))
print()

salario = float(input('Salário: '))
print()

print('F - Feminino / M - Masculino')
sexo = input('Sexo: ')
sexo = sexo.lower()
print()

print('S - Solteiro(a) / C - Casado(a) / V - Viuvo(a) / D - Divorciado(a)')
estado_civil = input('Estado Civil: ')
estado_civil = estado_civil.lower()
print()

os.system('clear')


#  Validação. Caso negativo, repete até que seja verdadeiro.
cont = 0
while len(nome) <= 3:
    nome = input('Nome: ')
    print()
    cont += 1

cont = 0
while idade < 0 or idade > 150:
    idade = int(input('Idade: '))
    print()
    cont += 1

cont = 0
while salario <= 0:
    salario = float(input('Salário: '))
    print()
    cont += 1

cont = 0
while sexo != 'f' and sexo != 'm':
    print('F - Feminino / M - Masculino')
    sexo = input('Sexo: ')
    sexo = sexo.lower()
    print()
    cont += 1

cont = 0
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print('S - Solteiro(a) / C - Casado(a) / V - Viuvo(a) / D - Divorciado(a)')
    estado_civil = input('Sexo: ')
    estado_civil = estado_civil.lower()
    print()
    cont += 1

#  sexo por extenso
if sexo == 'f':
    sexo = 'Feminino'

else:
    sexo = 'Masculino'

#  estado civil por extenso
if estado_civil == 's':
    estado_civil = 'Solteiro(a)'

elif estado_civil == 'c':
    estado_civil = 'Casado(a)'

elif estado_civil == 'v':
    estado_civil = 'Viuvo(a)'

else:
    estado_civil = 'Casado'


#  imprime os dados na tela
os.system('clear')

print(f'Nome: {nome} \n')
print(f'Idade: {idade} \n')
print(f'Salário: R$ {salario:.2f} \n')
print(f'Sexo: {sexo} \n')
print(f'Estado Civil: {estado_civil} \n')
