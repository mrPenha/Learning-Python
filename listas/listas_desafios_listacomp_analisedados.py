import os
os.system('clear')

"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
1 - quantas pessoas foram cadastradas
2 - uma listagem com as pessoas mais pesadas
3 - uma listagem com as pessoas mais leves
"""
temp = []
peso = 0
pesado = []
leve = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if peso == 0:
        peso = temp[1]
        pesado.append(temp[:])
        leve.append(temp[:])

    else:
        if temp[1] > peso:
            pesado.append(temp[:])
        else:
            leve.append(temp[:])

    temp.clear()

    op = input('Deseja continuar? [S/N]: ').lower()
    if op == 'n':
        os.system('clear')
        break

    elif op == 's':
        os.system('clear')
        continue

    else:
        os.system('clear')
        print('Opção Inválida \n')

if pesado[0] == leve[0]:
    del (leve[0])
else:
    pass


print(f'{"* " * 30} \n\n')

print(f'Quantidade de pessoas cadastradas: {len(pesado+leve)} \n')

for i in pesado:
    print(f'Mais pesados {i[0]: >15} --> {i[1]:.3f}')

print(f'\n{"- " * 30} \n')

for i in leve:
    print(f'Mais leves {i[0]: >15} --> {i[1]:.3f}')

print(f'\n\n{"* " * 30} \n\n')
