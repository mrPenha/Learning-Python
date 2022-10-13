import os
os.system('clear')
"""
DESAFIO
Criar um programa que tenha uma tupla totalmente preenchida com uma contagem por extenção de 0 até 10.
O programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso
"""

guardar = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if n >= 0 and n <= 10:
        print()
        print(guardar[n].title())
        print()
    else:
        os.system('clear')
        print('Tente novamente. \n\n')
