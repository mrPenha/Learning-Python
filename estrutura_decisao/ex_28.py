"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar."""
print()

print('OP   TIPO')
print('----------------')
print('1    File Duplo \n2    Alcatra \n3    Picanha ')
print('----------------')
op = int(input('Op > '))
print()

quantidade = float(input('Digite a quantidade (Kg): '))
print()
print('Compra com cartão Tabajara? \n1 - Sim \n2 - Não')
print('----------------')
cartao = int(input('Op > '))
print()

if op == 1:
    tipo = "File Duplo"
    if quantidade <= 5:
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.80

if op == 2:
    tipo = "Alcatra"
    if quantidade <= 5:
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80

if op == 3:
    tipo = "Picanha"
    if quantidade <= 5:
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80

if cartao == 1:
    r = "CarTab"
    desconto = ((preco * 5) / 100)
    total = preco - desconto
else:
    r = "Outros"
    desconto = 0
    total = preco

print('------------------------------')
print('\t CUPOM FISCAL ')
print('------------------------------')
print(f'Descrição         {tipo}')
print(f'Quantidade        Kg {quantidade:.2f}')
print(f'Preço             R$ {preco:.2f}')
print('------------------------------')
print(f'Forma Pgto        {r}')
print('------------------------------')
print(f'Desconto          R$ {desconto:.2f}')
print('------------------------------')
print(f'Total             R$ {total:.2f}')
print('------------------------------')

print()
