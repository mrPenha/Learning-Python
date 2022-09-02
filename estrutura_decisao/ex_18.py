"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

#  Obs1: O ano bissexto foi feito por Augusto, imperador de Roma no ano 8 D.C., fevereiro tinha 24 dias.
#  Obs2: Em 1582 o Papa Gregório modificou o mês de feverêiro para 29 dias."""


dia = int(input('Dia: '))
if dia < 1:
    print()
    print('DATA INVÁLIDA')
    quit()

mes = int(input('Mês: '))
if mes < 1 or mes > 12:
    print()
    print('DATA INVÁLIDA')
    quit()

ano = int(input('Ano: '))
if ano < 1:
    print()
    print('DATA INVÁLIDA')
    quit()

print()

valido = False

#  meses com 31 dias
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        valido = True

#  meses com 30 dias
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        valido = True

elif mes == 2:
    #  testando se ano é bissexto
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        if dia <= 29:
            valido = True
    else:
        if dia <= 28:
            valido = True


if valido:
    print(f'{dia}/{mes}/{ano}')
    print()
    print('DATA VÁLIDA')
    print()

else:
    print(f'{dia}/{mes}/{ano}')
    print()
    print('DATA INVÁLIDA')
    print()
