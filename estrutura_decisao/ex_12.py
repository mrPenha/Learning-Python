"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
    
    Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00"""


print()

print('\tTABELA DE DESCONTOS (Salário Bruto)\n')

print('Até 900 (inclusive)              :isento')
print('*************************************************')
print('Até 1500 (inclusive)             :desconto de 5%')
print('*************************************************')
print('Até 2500 (inclusive)             :desconto de 10%')
print('*************************************************')
print('Acima de 2500                    :desconto de 20%')
print('*************************************************')

print()

valor_hora = float(input('Valor da hora trabalhada: R$ '))
qtd_hora_t = int(input('Horas trabalhadas no mês: '))
bruto = valor_hora*qtd_hora_t
print()
print(f'Salário Bruto: R$ {bruto:.2f}')

print()

#  ir == 5;
#  inss == 10;
#  fgts == 11

if bruto <= 900:
    #  ir isento
    ir = 0
    inss = (bruto*10)/100
    fgts = (bruto*11)/100
    total_desc = ir+inss
    liquido = bruto-total_desc

elif bruto > 900 and bruto <= 1500:
    ir = (bruto*5)/100
    inss = (bruto*10)/100
    fgts = (bruto*11)/100
    total_desc = ir+inss
    liquido = bruto-total_desc

elif bruto > 1500 and bruto <= 2500:
    ir = (bruto*10)/100
    inss = (bruto*10)/100
    fgts = (bruto*11)/100
    total_desc = ir+inss
    liquido = bruto-total_desc

else:
    ir = (bruto*20)/100
    inss = (bruto*10)/100
    fgts = (bruto*11)/100
    total_desc = ir+inss
    liquido = bruto-total_desc

print()

print('\t\tHOLERITE\n')

print(f'Salário Bruto           : {bruto:.2f}')
print('*********************************')
print(f'(-) IR (5%)             : {ir:.2f}')
print('*********************************')
print(f'(-) INSS ( 10%)         : {inss:.2f}')
print('*********************************')
print(f'Total de descontos      : {total_desc:.2f}')
print('*********************************')
print(f'Salário Liquido         : {liquido:.2f}')
print('*********************************')
print(f'FGTS (11%)              : {fgts:.2f}')
print('*********************************')

print()
