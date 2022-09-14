"""Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7

    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35"""
import os
os.system('clear')

while True:
    numero = int(input('Montar tabuada de: '))
    comeca = int(input('Começar por: '))
    termina = int(input('Terminar em: '))
    if termina < comeca:
        print('\nO Começar deve ser menor que o Terminar\n')
    else:
        break
print()

while comeca <= termina:
    r = numero*comeca
    print(f'{numero} X {comeca} = {r}')
    comeca += 1

print()
