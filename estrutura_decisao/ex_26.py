"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool: Até 20 litros, desconto de 3% por litro. Acima de 20 litros, desconto de 5% por litro
    Gasolina: Até 20 litros, desconto de 4% por litro. Acima de 20 litros, desconto de 6% por litro

    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""
print()

preco_litro_a = 1.90
preco_litro_g = 2.50
desconto_alco_abaixo_vinte = 3
desconto_alco_acima_vinte = 5
desconto_gaso_abaixo_vinte = 4
desconto_gaso_acima_vinte = 6

print('\t COMBUSTÍVEIS COM DESCONTO \n')
print('\t     TABELA DE PREÇOS \n')
print('Produto      | Valor          | Desconto')
print('-----------------------------------------------------------------')
print('Álcool       | R$ 1,90(L)     | Até 20L (3%)  |Acima de 20L (5%)')
print('Gasolina     | R$ 2,50(L)     | Até 20L (4%)  |Acima de 20L (6%)')
print('-----------------------------------------------------------------')
print()

print('Digite a letra referente ao Produto \n\n"A" - Álcool \n"G" - Gasolina \n"S" - Sair \n')
op = input('> ')
op = op.lower()

print()
if op == 'a':
    qtd = int(input('Insira a quantidade de Litros: '))
    print()

    if qtd <= 20:
        bruto = qtd*preco_litro_a
        liquido = bruto-((bruto*desconto_alco_abaixo_vinte)/100)
        print(f'Valor Bruto: R$ {bruto:.2f} \nValor Líquido: R$ {liquido:.2f}')
    else:
        bruto = qtd*preco_litro_a
        liquido = bruto-((bruto*desconto_alco_abaixo_vinte)/100)
        print(f'Valor Bruto: R$ {bruto:.2f} \nValor Líquido: R$ {liquido:.2f}')

elif op == 'g':
    qtd = int(input('Insira a quantidade de Litros: '))
    print()

    if qtd <= 20:
        bruto = qtd*preco_litro_g
        liquido = bruto-((bruto*desconto_gaso_abaixo_vinte)/100)
        print(f'Valor Bruto: R$ {bruto:.2f} \nValor Líquido: R$ {liquido:.2f}')
    else:
        bruto = qtd*preco_litro_g
        liquido = bruto-((bruto*desconto_gaso_abaixo_vinte)/100)
        print(f'Valor Bruto: R$ {bruto:.2f} \nValor Líquido: R$ {liquido:.2f}')

elif op == 's':
    print('Volte Sempre!')
    print()
    quit()

else:
    if op != 'a' or op != 'g' or op != 's':
        print('Opção Inválida')
        print()
        quit()

print()
