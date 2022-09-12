"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""
import os
os.system('clear')

#  quantidade de eleitores
x = 0
while x < 1:
    qtd = input('Quantidade de pessoas: ')
    print()

    if ',' not in qtd and '.' not in qtd:
        qtd = int(qtd)
        x = 1

    else:
        os.system('clear')
        print('Insira apenas números inteiros \n')
        x = 0


#  votos
c = 0
qdt_a = 0
qtd_b = 0
qtd_c = 0
while c < qtd:
    #  código de votação
    print('CANDIDATO     CÓDIGO')
    print('--------------------')
    print('A                 90')
    print('--------------------')
    print('B                 80')
    print('--------------------')
    print('C                 70')
    print('--------------------\n')

    voto = input(f'Insira seu voto: ')

    if ',' not in voto and '.' not in voto:
        voto = int(voto)

        if voto == 90 or voto == 80 or voto == 70:

            if voto == 90:
                os.system('clear')
                qdt_a += 1
                c += 1

            elif voto == 80:
                os.system('clear')
                qtd_b += 1
                c += 1

            else:
                os.system('clear')
                qtd_c += 1
                c += 1

        else:
            os.system('clear')
            print('\nInsira código correto\n')
            c = c

    else:
        os.system('clear')
        print('\nInsira apenas números inteiros \n')
        c = 0

print('\n\tVOTOS \n')
print(f'Candidato A: {qdt_a} \nCandidato B: {qtd_b} \nCandidato C: {qtd_c} \n')
