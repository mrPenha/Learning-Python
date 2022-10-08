import os
os.system('clear')


def linha():
    print('----------------------------------------------------- \n')


# TUPLAS
# SEGUE OS MESMOS PADRÕES DA LISTA
# TUPLAS NÃO PODEM SER MODIFICADAS, LISTAS PODEM.

t1 = ()
t2 = (1, 2, 3, 'João', 5, 'Monique')
t3 = 1, 2, 'Monique', 'Doroty', 3, 4
t4 = 1
t5 = 1,
t6 = (1, 2, 3)
t7 = ('João', 'Monique', 'Doroth')
t8 = t6 + t7
n1, n2, n3, *outra, n4 = t3
t9 = ('azul', 'amarelo') * 3
t10 = list(t7)

print(f'{type(t1)} \n')

print(f'TUPLA VAZIA: t1 = {t1}')
linha()

print(f'TUPLA COM ELEMENTOS: t2 = {t2}')
linha()

print(f'ACESSAR ELEMENTO PELO INDICE: t2[3] = {t2[3]}')
linha()

print('ITERAR SOBRE OS ELEMENTOS: \n')
for i in t2:
    print(i)
linha()

print(f'FATIAR A TUPLA: t2[2:4] = {t2[2:4]}')
linha()

print(f'CRIAR TUPLAS SEM PARENTESES: \n')
print("t3 = 1, 2, 'Monique', 'Doroty', 3, 4 \n")
print(f'print(t3) = {t3}')
linha()

print('PARA CRIAR TUPLA COM 1 ELEMENTO, DEVE-SE ADICIONAR A VÍRGULA LOGO APÓS O ELEMENTO. \n')
print(f't4 = 1  {type(t4)} \nt5 = 1, {type(t5)}')
linha()

print('CONCATENAR TUPLAS: \n')
print('t6 = (1,2,3) \nt7 = ("João", "Monique", "Doroth") \nt8 = t6 + t7 \n')
print(f'print(t8) = {t8}')
linha()

print('DESEMPACOTAR EM VARIÁVEIS: \n')
print("t3 = (1, 2, 'Monique', 'Doroty', 3, 4) \nn1, n2, n3, *outra, n4 = t3 \n")
print(
    f'print(n1, n2, n3) = {n1, n2, n3} \nprint(outra) = {outra} \nprint(n4) = {n4}')
linha()

print('REPETIR TUPLA COM MULTIPLICADOR: \n')
print("t9 = ('azul', 'amarelo') * 3 \n")
print(f'print(t9) = {t9}')
linha()

print('CONVERTER TUPLAS EM LISTAS: \n')
print("t7 = ('João', 'Monique', 'Doroth')")
print('t10 = list(t7)')
print(f'print(t10) = {t10} \n')
print('Agora pode-se modificar o elemento da lista. Ex: \n')
t10[0] = 'azul'
print(f"t10[0] = 'Azul' \nprint(t10) = {t10}")
linha()
