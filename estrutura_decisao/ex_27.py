"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente."""
print()

preco_morango_ate_5 = 2.50
preco_morango_acima_5 = 2.20
preco_maca_ate_5 = 1.80
preco_maca_acima_5 = 1.50

#  se peso da compra > 8kg ou se valor total > R$ 25,00
desconto_maior = 10

print('                      Até 5 Kg           Acima de 5 Kg')
print('Morango         R$ 2,50 por Kg          R$ 2,20 por Kg')
print('Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg')
print('------------------------------------------------------\n')


kg_morango = float(input('Insira a quantidade em "Kg" do morango: '))
kg_maca = float(input('Insira a quantidade em "Kg" da maçã: '))
kg_total = kg_morango + kg_maca
print()

if kg_morango > 5:
    #  preço morango > 5kg
    preco_morango = kg_morango * preco_morango_acima_5
else:
    #  preço morango <= 5kg
    preco_morango = kg_morango * preco_morango_ate_5

if kg_maca > 5:
    #  preço maçã > 5kg
    preco_maca = kg_maca * preco_maca_acima_5
else:
    #  preço maçã <= 5kg
    preco_maca = kg_maca * preco_maca_ate_5


#  desconto de 10% se o preço total da compra for > R$ 25,00 ou se o peso total > 8kg
preco_total = preco_morango + preco_maca
if preco_total > 25 or kg_total > 8:
    valor_bruto = preco_total
    desconto = (valor_bruto * desconto_maior)/100
    valor_liquido = valor_bruto - desconto

    print(f'Morango \nPeso: {kg_morango:.2f} Kg \nValor: R$ {preco_morango:.2f} \n\nMaçã \nPeso: {kg_maca:.2f} Kg \nValor: R$ {preco_maca:.2f} \n\nPeso Total: {kg_total:.2f} Kg \nSubtotal: R$ {valor_bruto:.2f} \nDesconto: R$ {desconto:.2f} \n\nTotal: R$ {valor_liquido:.2f}')

else:
    valor_bruto = preco_total
    desconto = 0
    valor_liquido = valor_bruto - desconto

    print(f'Morango \nPeso: {kg_morango:.2f} Kg \nValor: R$ {preco_morango:.2f} \n\nMaçã \nPeso: {kg_maca:.2f} Kg \nValor: R$ {preco_maca:.2f} \n\nPeso Total: {kg_total:.2f} Kg \nSubtotal: R$ {valor_bruto:.2f} \nDesconto: R$ {desconto:.2f} \n\nTotal: R$ {valor_liquido:.2f}')


print()
