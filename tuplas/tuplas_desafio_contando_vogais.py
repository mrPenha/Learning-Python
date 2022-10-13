import os
os.system('clear')


def linha():
    print('-' * 40, '\n\n')


palavras = ('abobora', 'arroz', 'feijao', 'batata', 'macarrao',
            'parede', 'alvenaria', 'televisao', 'xbox', 'colchao', 'cotonete')

for i in palavras:
    print(f'\nEm {i.upper()} temos as vogais:', end=' ')
    for j in i:
        if j in 'aeiou':

            print(j.upper(), end=' ')
print()
linha()
