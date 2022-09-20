"""
Split - Dividir uma String  # str
Join - Juntar uma lista  # str
Enumerate - Enumerar elementos da lista  # iteraveis
"""
import os
os.system('clear')

# #  Split
# txt = 'O Brasil é o país do futebol, o Brasil sil sil é penta.'
# lista_1 = txt.split(' ')
# lista_2 = txt.split(',')
# print(lista_1, '\n')
# print(lista_2, '\n')
# #################################################################

# # Join
# txt = 'O Brasil é penta.'
# lista_1 = txt.split(' ')
# print(lista_1, '\n')
# lista_2 = '--'.join(lista_1)
# print(lista_2, '\n')
# #################################################################

# #  Enumerate
# txt = 'O Brasil é penta.'
# #     [0] [1]  [2] [4]
# lista_1 = txt.split(' ')
# for v1, v2 in enumerate(lista_1):
#     # v1 = indice / v2 = valor real da lista
#     print(v1, '-', v2, '\n')
