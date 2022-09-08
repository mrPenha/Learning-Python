"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""
print()

numero = int(input('Quantos número deseja inserir: '))
print()

a = 0  # maior
b = 0  # menor
comeco_b = 0
soma = 0
cont = 0
while cont < numero:

    x = int(input('Insira o número: '))

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
