"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. """

sexo = input('Qual o seu sexo? [F]eminino / [M]asculino: ')

if sexo == 'm' or sexo == 'M':
    print('M - Masculino')

elif sexo == 'f' or sexo == 'F':
    print('F - Feminino')

else:
    print('Sexo Inválido')
