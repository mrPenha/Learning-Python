# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
print('Total do salário no mês')
valor_por_hora = float(input('Insira o valor de quanto você ganha por hora: '))
horas_trab_mes = float(input('Quantas horas você trabalha no mês: '))
total = valor_por_hora * horas_trab_mes
print(f'Seu salário mensal é de R$ {total}')