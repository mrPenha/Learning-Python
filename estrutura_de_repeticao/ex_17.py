"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 """
print()

numero = int(input('Informe o número a ser fatorado: '))
novo_num = numero
print()

print(f'{numero} = {numero}', end='')

cont = 1
while cont < numero:
    novo_num -= 1
    if novo_num == 0:
        break
    else:
        print(f'*{novo_num}', end='')

    r = numero * novo_num

    if novo_num == 1:
        print(f' = {r:,.0f}')

    numero = r
    novo_num = novo_num
    cont += 1

print()
