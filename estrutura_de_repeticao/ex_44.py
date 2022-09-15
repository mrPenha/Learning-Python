"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

    1 , 2, 3, 4  - Votos para os respectivos candidatos 
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco

    Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero."""
import os
os.system('clear')

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
total = 0
while True:
    print('CANDIDATOS A PRESIDÊNCIA \n\nCódigo   Candidato \n------------------ \n1        Reginaldo \n2        Roberto \n3        Roberta \n4        Rita \n5        Voto Nulo \n6        Voto em Branco \n')

    print('Para encerrar o programa, digite 0 (zero)\n')

    voto = int(input('Código: '))
    if voto == 0:
        break
    else:
        if voto == 1:
            a += 1
            total += 1

        elif voto == 2:
            b += 1
            total += 1

        elif voto == 3:
            c += 1
            total += 1

        elif voto == 4:
            d += 1
            total += 1

        elif voto == 5:
            e += 1
            total += 1

        elif voto == 6:
            f += 1
            total += 1

        else:
            input('CÓDIGO INVÁLIDO!')
            os.system('clear')

    os.system('clear')

os.system('clear')
print('\nCANDIDATOS A PRESIDÊNCIA\n\n')
print('Código   Candidato   Qtde Votos \n')
print(f'1        Reginaldo   {a}')
print(f'2        Roberto     {b}')
print(f'3        Roberta     {c}')
print(f'4        Rita        {d}')
print(f'5        Nulo        {e}')
print(f'6        Em Branco   {f} \n')

#  porcentagem
print(f'Total de votos: {total} \n')

porcent_nulos = (e / total)*100
print(f'Votos Nulos: {porcent_nulos:.1f}% \n')

porcent_brancos = (f / total)*100
print(f'Votos em Branco: {porcent_brancos:.1f}% \n')
