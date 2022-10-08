import os
os.system('clear')

# NO DICIONÁRIO CONTROLAMOS OS ÍNDICES


def linha():
    print('------------------------------------------------ \n')


d1 = {}
d1 = {1: 'Monique', 2: 'João Vitor', 3: 'Doroth'}
d2 = {
    'str': 'Valor',
    'núm': 'Valor',

}

print(f'{type(d1)} \n\n')

print('DICIONÁRIO VAZIO: d1 = {}')
linha()

print('COMPOSIÇÃO DE UM DICIONÁRIO: \n')
print("d2 = {'chave1': 'Valor da chave'} ")
linha()

print('DICIONÁRIO COM ELEMENTOS: \n')
print("d2 = {1: 'Monique, 2: 'João Vitor', 3: 'Doroth'} \n")
print(
    f'print(d2[1]) = {d1[1]} \nprint(d2[2]) = {d1[2]} \nprint(d2[3]) = {d1[3]}')
linha()
