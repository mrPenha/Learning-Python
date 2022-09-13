"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
    ..."""
import os
os.system('clear')

print('LOJAS TABAJARA\n')
print('0 - Sair \n')

total = 0
din = 0
prod = 0
troco = 0
c = 1
while c > 0:

    prod = float(input(f'Produto {c}: R$ '))
    total += prod
    c += 1

    if prod == 0:
        print('----------------------')
        print(f'Total: R$ {total:.2f}')
        print('----------------------')
        din = float(input('Dinheiro: R$ '))
        print('----------------------')
        if din > total:
            troco = din - total
            print(f'Troco: R$ {troco:.2f}')
            print('----------------------\n')

            sair = input('Press C para sair: \n> ')
            sair = sair.lower()
            if sair == 'c':
                total = 0
                prod = 0
                c = 1
                os.system('clear')
                print('LOJAS TABAJARA\n')
                print('0 - Sair \n')

        else:
            troco = total - din
            print(f'Troco: R$ {troco:.2f}')
            print('----------------------\n')

            sair = input('Press C para sair: \n> ')
            sair = sair.lower()
            if sair == 'c':
                total = 0
                prod = 0
                c = 1
                os.system('clear')
                print('LOJAS TABAJARA\n')
                print('0 - Sair \n')
