"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10."""

print()

nota1 = float(input('1ª nota: '))
if nota1 < 0 or nota1 > 10:
    print('Nota inválida!')
    quit()

nota2 = float(input('2ª nota: '))
if nota2 < 0 or nota2 > 10:
    print('Nota inválida!')
    quit()

nota3 = float(input('3ª nota: '))
if nota3 < 0 or nota3 > 10:
    print('Nota inválida!')
    quit()

media = (nota1+nota2+nota3)/3

print()

if media == 10:
    print('APROVADO COM DISTINÇÃO')

elif media >= 7:
    print('APROVADO')

else:
    print('REPROVADO')

print()
