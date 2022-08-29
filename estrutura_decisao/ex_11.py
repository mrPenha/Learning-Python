"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa
que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento."""
print()

print('\t\tTABELA DE REAJUSTE\n')

print('Até R$ 280,00 ------------------------- +20%')
print('********************************************')
print('Entre R$ 280,00 e R$ 700,00 ----------- +15%')
print('********************************************')
print('Entre R$ 700,00 e R$ 1500,00 ---------- +10%')
print('********************************************')
print('De R$ 1500,00 em diante ---------------- +5%')
print('********************************************')

print()

salario = float(input('Insira o salário do colaborador: R$ '))
reajuste = int(input('Insira o percentual de reajuste do salário: '))

if salario <= 280.00:
    if reajuste != 20:
        print('Insira o reajuste conforme a tabela acima.')
    aumento = (salario*reajuste)/100
    novo_salario = salario+aumento

elif salario > 280.00 and salario <= 700.00:
    if reajuste != 15:
        print('Insira o reajuste conforme a tabela acima.')
    aumento = (salario*reajuste)/100
    novo_salario = salario+aumento

elif salario > 700.00 and salario < 1500.00:
    if reajuste != 10:
        print('Insira o reajuste conforme a tabela acima.')
    aumento = (salario*reajuste)/100
    novo_salario = salario+aumento

else:
    if reajuste != 5:
        print('Insira o reajuste conforme a tabela acima.')
    aumento = (salario*reajuste)/100
    novo_salario = salario+aumento

print('\n\n\n')

print('\t\tSALÁRIO APÓS REAJUSTE\n')

print(f'Salário Atual ------------------- R$ {salario:.2f}')
print('***********************************************')
print(f'Percentual aplicado ---------------  {reajuste} %')
print('***********************************************')
print(f'Valor do aumento ---------------- R$ {aumento:.2f}')
print('***********************************************')
print(f'Salário após reajuste ----------- R$ {novo_salario:.2f}')
print('***********************************************')

print()
