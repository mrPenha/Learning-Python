import os
os.system('clear')

"""
Matriz com dimensão 3x3 e preencha com valores lidos pelo teclado. Mostre:
1 - A soma dos valores pares
2 - A soma dos valores da terceira coluna
3 - O maior valor da segunda coluna
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(
            input(f'Digite o valor para [{l}] e [{c}]: '))

print(f'\n{"-=" * 30}')

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'{"-=" * 30}\n')

soma_par = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]


soma_terceira = 0
for i in range(3):
    for j in range(3):
        if j == 2:
            soma_terceira += matriz[i][j]


print(f'A soma dos valores pares é: {soma_par} \n')
print(f'A soma dos valores da terceira coluna é: {soma_terceira} \n')
print(f'O maior valor da segunda coluna é: {max(matriz[1])} \n')
