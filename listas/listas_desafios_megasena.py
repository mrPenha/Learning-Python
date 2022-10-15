import os
import random
os.system('clear')

"""

"""

qtd = int(input('Quantidade de jogos: '))

jogos = []
temp = []
c = 0
while c < qtd:
    for i in range(6):
        for j in range(1):
            aleatorio = random.randint(1, 60)
            if aleatorio not in temp:
                temp.append(aleatorio)
            else:
                pass

    jogos.append(temp[:])
    temp.clear

    c += 1

print(jogos)
