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

troco = 0
produto = 0
soma = 0
pagamento = 0
c = 0
while c < 1:
    #  começar caixa
    print('Começar > 1 / Finalizar > -1')
    comecar = int(input('> '))

    while comecar == 1:
        os.system('clear')

        print('Finalizar > -1 \n')

        print(f'CAIXA \n\nTotal: R$ {soma:.2f} \n')

        #  valor produto
        produto = float(input('R$: '))
        if produto != -1:
            soma += produto
            produto = 0
            os.system('clear')
        else:
            break

    os.system('clear')

    #  pagamento / troco
    print(f'Total: R$ {soma:.2f} \n')
    pagamento = float(input('Pagamento: R$ '))

    os.system('clear')
    print(f'Total: R$ {soma:.2f} \n')
    print(f'Pagamento: R$ {pagamento:.2f} \n')
    print()
    if pagamento > soma:
        troco = pagamento - soma
        print(f'Troco: R$ {troco:.2f}\n')
    else:
        troco = soma - pagamento
        print(f'Troco: R$ {troco:.2f}\n')

    #  finalizar para continuar com nova compra
    print('Finalizar Caixa > F')
    finalizar = input('> ')
    finalizar = finalizar.lower()
    os.system('clear')
    c = 0
