"""Altere o programa anterior para mostrar no final a soma dos números."""
print()

print('INTERVALO ENTRE NÚMEROS \n\n')

num1 = int(input('Informe um inicial inteiro: '))
num1 = num1 + 1
num2 = int(input('Informe um final inteiro: '))

print()

for i in range(num1, num2):
    print(i)

    soma = 0
    cont = 0
    while cont < num2:

        if i > soma:
            soma += i
            i += 1
        else:
            soma == soma

        cont += 1

print()
print(soma)
