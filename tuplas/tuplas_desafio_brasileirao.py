import os
os.system('clear')


def linha():
    print('----------------------------------------------- \n\n')


"""
DESAFIO
Crie uma tupla com os 20 times da tabela do BRASILEIRÃO (atual) na ordem de colocação. Depois mostre:
1 - Os 5 primeiros colocados
2 - Os 4 últimos colocados
3 - Lista com os times em ordem alfabética
4 - Em que posição na tabela está o time ATLÉTICO MINEIRO
"""

times = (
    'Palmeiras',
    'Internacional',
    'Corinthians',
    'Flamengo',
    'Fluminense',
    'Athletico Paranaense',
    'Atlético Mineiro',
    'América Mineiro',
    'Botafogo',
    'Fortaleza',
    'Santos',
    'São Paulo',
    'Red Bull Bragantino',
    'Goiás',
    'Coritiba',
    'Ceará',
    'Cuiabá',
    'Atlético Goianiense',
    'Avaí',
    'Juventude'
)

print('Os 5 primeiros colocados \n'.upper())
for i in range(5):
    print(f'{i+1} - {times[i]}')
linha()

print('Os 4 últimos colocados \n'.upper())
c = 0
pos = 16
while c < 4:
    print(f'{pos+1} - {times[pos]}')
    c += 1
    pos += 1
linha()

print('Lista com os times em ordem alfabética \n'.upper())
for i, j in enumerate(sorted(times)):
    print(f'{i+1} - {j}')
linha()

print('Em que posição na tabela está o time ATLÉTICO MINEIRO \n'.upper())
posicao = times.index('Atlético Mineiro')
print(f'O Atlético MG está na {posicao+1} posição. \n')
for i, j in enumerate(times):
    print(f'{i+1} - {j}')
linha()
