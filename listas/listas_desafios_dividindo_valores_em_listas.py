import os
import random
os.system('clear')

"""
Crie um programa que recebe vários números e os coloque eles numa lista. Depois disso crie 2 listas extras, uma que vai conter apenas os valores pares e a outra os valores impares. Ao final mostre o conteúdo das 3 listas geradas
"""

valores = []

for i in range(10):
    n = random.randint(1, 100)
    valores.append(n)

lista_par = []
lista_impar = []

for i in valores:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)


print(f'Valores........... {valores} \n')
print(f'V_pares........... {lista_par} \n')
print(f'V_impares......... {lista_impar} \n')
