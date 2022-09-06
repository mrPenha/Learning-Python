"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50"""
print()

numero = int(input('Qual tabuada deseja ver: '))
print()

print(f'Tabuada do {numero}: \n')

cont = 0
while cont <= 10:
    r = numero*cont
    print(f'{numero} X {cont} = {r}')
    cont += 1

print()
