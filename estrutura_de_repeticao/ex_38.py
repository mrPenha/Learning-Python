"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

    Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""
import os
os.system('clear')

ano_atual = 2022
percentual = 1.5

salario = input('Salário Inicial: R$ ')
if ',' in salario:
    salario = salario.replace(',', '.')
    salario = float(salario)
    salario = f'{salario:_.2f}'
    salario = salario.replace('_', '.').replace('.', ',')
else:
    salario = float(salario)

while True:
    ano = input('Digite o Ano do contrato: ')
    if ano.isnumeric:
        ano = int(ano)
        break
    else:
        print('DADOS INVÁLIDOS')

aumento = (salario*percentual)/100
print(f'\nAno: {ano} ---- Valor: R$ {salario:,.2f} \n')
dobro = aumento
salario += dobro
for i in range(ano, ano_atual+1):
    print(f'\nAno: {ano+1} ---- Valor: R$ {salario:,.2f} \n')
    salario += dobro*2
    ano += 1
