import os
os.system('clear')


def linha():
    print('-' * 60, '\n')


# tupla VAZIA
vazia = ()
print('TUPLA VAZIA \n')
print(vazia)
linha()


# sintaxe: Tuplas são uma sequência (grupo ordenado) de elementos (items) separados por vírgulas, DELIMITADOS OU NÃO por parênteses, isto é, os parênteses não são obrigatórios.
lanche = ('hamburguer', 'suco', 'pudim', 'pizza', 'batata frita')
print(lanche)
linha()


# Fatiar tuplas
print('FATIAR TUPLAS \n')
print(lanche[:3])
print(lanche[2:])
print(lanche[1:3])
linha()


# Tuplas são imutáveis
print('31| TUPLAS SÃO IMUTÁVEIS \n')
print('32| _________________________________________________')
print('33| indeices       [0]        [1]     [2]      [3] \n')
print(f'34| lanche = {lanche}')
print('\n35| indeices       [-4]       [-3]    [-2]     [-1] ')
print('36| _________________________________________________ \n')
print("37| lanche[1] = 'regrigerante'")
print('\n38| print(lanche[1])')
print(
    '\n\nTraceback (most recent call last): \n  File "/home/pratespenha/Documentos/GitHub/Learning-Python/listas/tuplas.py", line 37, in <module> \n        lanche[1] = ''refrigerante'' \nTypeError: ''tuple'' object does not support item assignment')
linha()


# laço for em tuplas
print('LAÇO FOR \n')
for i in lanche:
    print(f'Item - {i}')

print()

for i in range(len(lanche)):
    print(f'Item - {lanche[i]}')

print()

for i, j in enumerate(lanche):
    print(f'Item {i+1} - {j}')

print()

for i in range(len(lanche)):
    print(f'Item {i+1} - {lanche[i]}')
linha()


# sorted em tuplas
print('ORDENAR TUPLAS \n')
print(f'Ordem crescente - {sorted(lanche)} \n')
print(f'Ordem decrescente - {sorted(lanche, reverse=True)}')
linha()


# concatenar (juntar) tuplas
print('JUNTAR 2 OU MAIS TUPLAS \n')
a = (1, 2, 3, 4)
b = (3, 4, 5, 6, 7, 8)
c1 = a+b
c2 = b+a
print(c1, '\n')
print(c2)
linha()


# tamanho da tupla
print('CONTAR TAMANHO (QTD ELEMENTOS) TUPLAS  \n')
print(len(c1))
linha()


# contar qtd de repetição de um elemento na tupla / tupla.count("elemento")
print('CONTAR QUANTAS VEZES UM ELEMENTO APARECE NA TUPLA \n')
print(c1.count(4))
linha()


# mostrar o índice de um elemento / tupla.index("elemento")
print('MOSTRAR O QUAL O ÍNDICE DO ELEMENTO[?] \n')
print(c1.index(7))
linha()


# tupla.index(?, !)
# ? -> elemento / ! -> a partir de qual posição (deslocamento)
print(
    'MOSTRAR O QUAL O ÍNDICE DO ELEMENTO[?] E DE QUAL POSIÇÃO[?] ELE DEVE COMEÇAR (DESLOCAMENTO) \n')
print(c2.index(3))
#  obs: o mesmo elemento, mas em posições diferêntes
print(c2.index(3, 1))
linha()


# em python as tuplas aceitam dados de tipos diferentes
print('TUPLAS EM PYTHON ACEITAM TIPOS DE DADOS DIFERÊNTES \n')
pessoa = ('joao', 39, 'M', 82.52)
print(pessoa)
linha()


# não é possível deletar um elemento dentro da tupla (imutável)
print('IMPOSSÍVEL DELETAR ELEMENTOS NAS TUPLAS (IMUTÁVEL) \n')
print('122| _________________________________________________')
print('123| indeices   [0]    [1] [2]  [3] \n')
print(f'124| pessoa = {pessoa}')
print('\n125| indeices  [-4]  [-3] [-2]  [-1] ')
print('126| _________________________________________________ \n')
print('127| del (pessoa[0])')
print(
    '\nTraceback (most recent call last): \n    File "/home/pratespenha/Documentos/GitHub/Learning-Python/listas/tuplas.py", line 127, in <module> \n       del (pessoa[0]) \nTypeError: ''tuple'' object doesnt support item deletion')
linha()

# mas é possível deletar a tupla inteira
print('MAS PODEMOS DELETAR UMA TUPLA INTEIRA \n')
del (pessoa)
print('del(pessoa) \n')
print('print(pessoa) \n')
print('Traceback (most recent call last): \n  File "/home/pratespenha/Documentos/GitHub/Learning-Python/listas/tuplas.py", line 134, in <module> \n       print(pessoa) \nNameError: name ''pessoa'' is not defined')
linha()
