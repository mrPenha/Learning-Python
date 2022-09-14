"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""
import os
os.system('clear')

cidades = 5
codigo_maior_indice = 0
codigo_menor_indice = 0
veiculos = 0
acidentes = 0
maior_indice = 0
menor_indice = 0
soma_acidentes_2000 = 0
qtd_cidade_menor_2000_veic = 0
soma_veiculos = 0
media_veiculos = 0
media_acidentes = 0

c = 0
while c < cidades:
    codigo_cidade = input('Código da cidade: ')
    print('----------------------------------')
    qtd_veiculos = int(input('Qtde veículos: '))
    print('----------------------------------')
    num_acidentes = int(input('Qtde acidentes: '))
    print('----------------------------------')
    codigo = codigo_cidade
    veiculos = qtd_veiculos
    acidentes = num_acidentes
    print()

    #  testa para indices maiores de acidentes
    if acidentes > maior_indice:
        maior_indice = acidentes
        codigo_maior_indice = codigo
    else:
        maior_indice = maior_indice

    if menor_indice == 0:
        menor_indice = acidentes
    else:
        if acidentes < maior_indice and acidentes < menor_indice:
            menor_indice = acidentes
            codigo_menor_indice = codigo
        else:
            menor_indice = menor_indice

    if veiculos < 2000:
        soma_acidentes_2000 += acidentes
        qtd_cidade_menor_2000_veic += 1
    else:
        soma_acidentes_2000 = soma_acidentes_2000

    soma_veiculos += veiculos

    c += 1

media_veiculos = soma_veiculos / 5
media_acidentes = soma_acidentes_2000 / qtd_cidade_menor_2000_veic

print(f'\nMaior Indice: {maior_indice} ----- Código da cidade: {codigo_maior_indice} \nMenor indice: {menor_indice} ----- Código da cidade: {codigo_menor_indice} \n')

print(f'\nMédia de veículos nas 5 cidades juntas: {media_veiculos} \n')

print(
    f'\nMédia de acidentes em cidades com menos de 2.000 veículos de passeio: {media_acidentes} \n')
