import os
os.system('clear')

lista = [
    ['p1', 13],
    ['p2', 7],
    ['p3', 25],
    ['p4', 12],
    ['p5', 4]
]

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)


a = lambda item: item[1]

def funcao(item):
    return item[1]