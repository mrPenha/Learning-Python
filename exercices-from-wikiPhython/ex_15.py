""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
    
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$ """
print()
valor_hora = float(input('Quanto você ganha por hora: '))
horas_trab = int(input('Quantas horas você trabalha no mês: '))
total_mes = valor_hora * horas_trab

bruto = total_mes
total_venc = bruto
ir = (bruto*11)/100
inss = (bruto*8)/100
sindicato = (bruto*5)/100
total_desc = ir+inss+sindicato
total_liq = bruto-ir-inss-sindicato
print()
print()
print('**********************************************************************************')
print('                                     HOLERITE                                     ')
print('**********************************************************************************')
print(f'Descrição     |Referência   | Proventos             |Descontos                   ')
print(f'---------------------------------------------------------------------------------')
print(f'Salário base  |{horas_trab}          |{bruto}               |                            ')
print(f'IR            |11%          |                       |{ir}                        ')
print(f'INSS          |8%           |                       |{inss}                      ')
print(f'Sindicato     |5%           |                       |{sindicato}                 ')
print(f'---------------------------------------------------------------------------------')
print(f'                            |Total Venc.: {bruto}   |Total Desc.: {total_desc}   ')
print(f'---------------------------------------------------------------------------------')
print(f'                            |Total Líquido:         |{total_liq}                 ')
print('**********************************************************************************')