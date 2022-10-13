import os
os.system('clear')


def linha():
    print(f'\n{"*" * 100} \n\n')


# lista vazia
print('LISTA VAZIA \n')
vazia1 = []
vazia2 = list()
print(f'vazia1 = {vazia1}')
print(f'vazia2 = {vazia2}')
linha()


# lista com elementos
print('LISTA COM ELEMENTOS \n')
lanche = ['hamburguer', 'batata frita', 'refrigerante', 'nuggets']
print(f'lanche = {lanche} \n')
linha()


# lista com elementos e seus respectivos índices
print('LISTA COM ELEMENTOS E SEUS RESPECTIVOS INDICES \n')

print('indices ->    [0]            [1]            [2]            [3]')
print('------------------------------------------------------------------')
print("lanche = ['hamburguer', 'batata frita', 'refrigerante', 'nuggets']")
print('------------------------------------------------------------------')
print('indices ->    [-4]           [-3]           [-2]           [-1] \n')
linha()


# acrescentar elementos na lista
# lista.append('elemento') --> inclui elemento no final da lista
# lista.insert(indice, 'elemento') --> inclui elemento no indice desejado
print('INCLUIR ELEMENTOS NA LISTA \n')
print(f'lanche = {lanche} \n')

print("lanche.append('sorvete')")
lanche.append('sorvete')
print(f'print(lanche) = {lanche} \n')

print("lanche.insert(0, 'tortinha')")
lanche.insert(0, 'tortinha')
print(f'print(lanche) = {lanche} \n')
linha()


# excluir elementos da lista / esvaziar lista
# lista.pop() --> remove último elemento da lista
# lista.pop(indice) --> remove o elemento referente ao indice
# lista.remove('valor') --> remove o item selecionado. Exemplo: lanche.remove('tortinha')
# del(lista[indice]) --> remove o elemento referente ao indice, também pode ser del(lista[:])
# del(lista) --> deleta a lista da memória
# lista.clear() --> esvaziar a lista
print('EXCLUIR ELEMENTOS NA LISTA \n')
print(f'lanche = {lanche} \n')

print("lanche.pop()")
lanche.pop()
print(f'print(lanche) = {lanche} \n')

print("lanche.pop(4)")
lanche.pop(4)
print(f'print(lanche) = {lanche} \n')

print("lanche.remove('tortinha')")
lanche.remove('tortinha')
print(f'print(lanche) = {lanche} \n')

print('==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==')
novo_lanche = ['iogurte', 'bolacha', 'suco', 'pão com mortadela', 'pizza']
print(f'novo_lanche = {novo_lanche} ')
print('==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--== \n')

print("del(novo_lanche[2:])")
del (novo_lanche[2:])
print(f'print(novo_lanche) = {novo_lanche} \n')


print('novo_lanche.clear()')
novo_lanche.clear()
print(f'print(novo_lanche) = {novo_lanche} \n')
linha()


# criar lista através de range
print('CRIAR LISTA ATRAVÉS DE RANGE \n')

print('valores = list(range(10))')
valores = list(range(10))
print(f'print(valores) = {valores} \n')

print('valores = list(range(0, 10, 2))')
valores = list(range(0, 10, 2))
print(f'print(valores) = {valores} \n')
linha()


# ordenar listas
# .sort() --> ordem crescente
# .sort(reverse=True) --> ordem decrescente
# print(sorted(lista)) --> ordem crescente
# print(sorted(lista, reverse=True)) --> ordem crescente
print('ORDENAR LISTAS \n')

nomes = ['joao', 'monique', 'doroth', 'adriana',
         'tamires', 'ana luiza', 'silvio santos']

print(f'nomes = {nomes} \n')

print('nomes.sort() --> crescente')
nomes.sort()
print(f'print(nomes) = {nomes} \n')

print('nomes.sort(reverse=True) --> decrescente')
nomes.sort(reverse=True)
print(f'print(nomes) = {nomes} \n')
linha()


# sabendo o tamanho de uma lista / qtd de elementos
# utiliza-se a função len(lista)
print('SABENDO O TAMANHO DE UMA LISTA / QTD ELEMENTOS \n')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'numeros = {numeros} \n')

print("print(len(numeros)) \n")
print(f'Essa lista tem {len(numeros)} elementos \n')
linha()


# listas são mutáveis!
print('PODE-SE SUBSTITUIR VALORES EM LISTAS (MUTÁVEIS) \n')
doces = ['brigadeiro', 'bolacha', 'bolo', 'sorvete']

print(f'doces = {doces} \n')

print("doces[2] = 'chocolate' ")
doces[2] = 'chocolate'
print(f'print(doces) = {doces} \n')
linha()


# laço for
print('LAÇO FOR \n')
outros_valores = []
print(f'outros_valores = {outros_valores} \n')
print('for i in range(10): \n   outros_valores.append(i)')
for i in range(10):
    outros_valores.append(i)

print(f'\nprint(outros_valores) = {outros_valores}')
linha()


# copiando uma lista
print('COPIANDO UMA LISTA \n')
lista_a = [2, 4, 6, 8, 9]
lista_b = lista_a

print('lista_a = [2, 4, 6, 8, 9]')
print('lista_b = lista_a ---> foi feito uma ligação entre as listas \n')
print('lista_b[2] = 3')
lista_b[2] = '3'
print(f'lista_a = {lista_a} ---> modificou a lista_a')
print(f'lista_c = {lista_b} ---> modificou a lista_b também \n')

print('\n---------------------------------------------------------\n')
lista_b[2] = 6  # deixando a lista como no início

print('lista_a = [2, 4, 6, 8, 9]')
print('lista_c = lista_a[:] ---> copiando a lista_a \n')
lista_c = lista_a[:]
lista_c[2] = '22'
print(f'lista_a = {lista_a}')
print(f'lista_c = {lista_c} ---> agora modificou somente a lista_c \n')
linha()
