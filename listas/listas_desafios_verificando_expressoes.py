import os
os.system('clear')

"""
Crie um programa em que o usuário digite uma expressão qualquer que use parênteses. O programa deverá analisar se a expressão está com os parênteses abertos ou fechados na ordem correta.
"""

expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')

    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
        break

if len(pilha) == 0:
    print('Sua expressão está correta \n')

else:
    print('Sua expressão está incorreta \n')
