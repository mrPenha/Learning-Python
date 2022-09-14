"""O cardápio de uma lanchonete é o seguinte:

    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00

    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado."""
import os
os.system('clear')

print('Especificação    Código  Preço')
print('--------------------------------')
print('Cachorro Quente  100     R$ 1,20')
print('Bauru Simples    101     R$ 1,30')
print('Bauru com ovo    102     R$ 1,50')
print('Hambúrguer       103     R$ 1,20')
print('Cheeseburguer    104     R$ 1,30')
print('Refrigerante     105     R$ 1,00')
print('--------------------------------')
print('Pressione 0 para sair')
print('--------------------------------')

total = 0
while True:
    codigo = int(input('Código: '))

    if codigo == 0:
        break
    else:

        if codigo == 100 or codigo == 101 or codigo == 102 or codigo == 103 or codigo == 104 or codigo == 105:

            qtd = int(input('Quantidade: '))

            print('\nEspecificação    Qtde  Preço')

            if codigo == 100:
                preco = qtd*1.20
                print(f'Cachorro Quente  {qtd}     {preco:.2f} \n')
                total += preco

            if codigo == 101:
                preco = qtd*1.30
                print(f'Bauru Simples    {qtd}     {preco:.2f} \n')
                total += preco

            if codigo == 102:
                preco = qtd*1.50
                print(f'Bauru com Ovo    {qtd}     {preco:.2f} \n')
                total += preco

            if codigo == 103:
                preco = qtd*1.20
                print(f'Hambúrguer       {qtd}     {preco:.2f} \n')
                total += preco

            if codigo == 104:
                preco = qtd*1.30
                print(f'Chesseburguer    {qtd}     {preco:.2f} \n')
                total += preco

            if codigo == 105:
                preco = qtd*1.00
                print(f'Refrigerante     {qtd}     {preco:.2f} \n')
                total += preco

        else:
            os.system('clear')
            print('CÓDIGO INVÁLIDO\n\n')

            print('Especificação    Código  Preço')
            print('--------------------------------')
            print('Cachorro Quente  100     R$ 1,20')
            print('Bauru Simples    101     R$ 1,30')
            print('Bauru com ovo    102     R$ 1,50')
            print('Hambúrguer       103     R$ 1,20')
            print('Cheeseburguer    104     R$ 1,30')
            print('Refrigerante     105     R$ 1,00')
            print('--------------------------------')
            print('Pressione 0 para sair')
            print('--------------------------------')

print(f'\nValor Total: R$ {total:.2f} \n')
