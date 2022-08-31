"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre zero e 4.0        E
      
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. """

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

print()

if media < 4:
    print(f'Primeira nota             : {nota1}')
    print(f'Segunda nota              : {nota2}')
    print(f'Média                     : {media}')
    print('Média de Aproveitamento   : E')
    print()
    print('--------- "REPROVADO" ---------')

elif media < 6:
    print(f'Primeira nota             : {nota1}')
    print(f'Segunda nota              : {nota2}')
    print(f'Média                     : {media}')
    print('Média de Aproveitamento   : D')
    print()
    print('--------- "REPROVADO" ---------')

elif media < 7.5:
    print(f'Primeira nota             : {nota1}')
    print(f'Segunda nota              : {nota2}')
    print(f'Média                     : {media}')
    print('Média de Aproveitamento   : C')
    print()
    print('--------- "APROVADO" ---------')

elif media < 9:
    print(f'Primeira nota             : {nota1}')
    print(f'Segunda nota              : {nota2}')
    print(f'Média                     : {media}')
    print('Média de Aproveitamento   : B')
    print()
    print('--------- "APROVADO" ---------')

else:
    print(f'Primeira nota             : {nota1}')
    print(f'Segunda nota              : {nota2}')
    print(f'Média                     : {media}')
    print('Média de Aproveitamento   : A')
    print()
    print('--------- "APROVADO" ---------')

print()
