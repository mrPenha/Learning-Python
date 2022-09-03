"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"
    
    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

print()
print('\t DETETIVE \n')

classificacao = 0

#  Perguntas
q1 = input('Telefonou para a vítima?: ')
print()
q2 = input('Esteve no local do crime?: ')
print()
q3 = input('Mora perto da vítima?: ')
print()
q4 = input('Devia para a vítima?: ')
print()
q5 = input('Já trabalhou com a vítima?: ')
print()

q1 = q1.lower()
q2 = q2.lower()
q3 = q3.lower()
q4 = q4.lower()
q5 = q5.lower()

#  classificação
if q1 == 'sim':
    classificacao += 1
else:
    classificacao == classificacao

if q2 == 'sim':
    classificacao += 1
else:
    classificacao == classificacao

if q3 == 'sim':
    classificacao += 1
else:
    classificacao == classificacao

if q4 == 'sim':
    classificacao += 1
else:
    classificacao == classificacao

if q5 == 'sim':
    classificacao += 1
else:
    classificacao == classificacao

#  participação no crime
if classificacao == 2:
    print('SUSPEITA')
elif classificacao > 2 and classificacao < 5:
    print('CÚMPLICE')
elif classificacao == 5:
    print('ASSASSINO(A)')
else:
    print('INOCENTE')
