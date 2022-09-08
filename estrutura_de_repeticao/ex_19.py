"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""
import os
print()

numero = int(input('Quantos número deseja inserir: '))
print()


a = 0  # maior
b = 0  # menor
comeco_b = 0
soma = 0
cont = 0
while cont < numero:
    x = int(input(f'Insira o {cont+1}º número: '))

    if x < 0 or x > 1000:
        os.system('clear')
        print('Número Inválido \n')
        print('Insira números inteiros entre 0 e 1000 \n')
        soma = 0
        cont = 0

    else:
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
        cont += 1


print()
print(f'Maior número: {a} \nMenor número: {b} \nSoma: {soma}')
