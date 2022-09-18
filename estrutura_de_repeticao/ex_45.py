"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.

    Gabarito da Prova:

    01 - A
    02 - B
    03 - C
    04 - D
    05 - E
    06 - E
    07 - D
    08 - C
    09 - B
    10 - A

    Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa."""
import os
os.system('clear')
qtd_acerto = []
qtd_erro = []
nota_maxima = 10
nota = []
acerto = 0
erro = 0
gabarito = ''
resposta = ''
nome_do_aluno = []
qtd_alunos = 0
op = -1
while op != 4:
    print('Escolha a opção \n1 - Professor \n2 - Aluno \n3 - Resultados \n4 - finalizar')
    print('----------------')

    op = int(input('> '))

    if op == 4:
        break

    #  entrada do professor (qtde questões e gabarito de respostas)
    elif op == 1:
        os.system('clear')
        qtd_questoes = int(input('Quantidade de Questões: '))
        print('Insira as respostas como sendo A, B, C, D ou E \n')

        c = 0
        while c < qtd_questoes:
            r = input(f'Resposta da questão {c+1}: ')
            if r == 'a' or r == 'b' or r == 'c' or r == 'd' or r == 'e':
                gabarito += r.upper()
                c += 1
            else:
                print('\nInsira as respostas como sendo A, B, C, D ou E \n')
                c = c

        os.system('clear')

    #  entrada do aluno (nome e respostas)
    elif op == 2:
        os.system('clear')
        nome = input('Nome do Aluno: ')
        print('Insira as respostas como sendo A, B, C, D ou E \n')
        nome_do_aluno.append(nome)
        qtd_alunos += 1

        c = 0
        while c < qtd_questoes:
            r = input(f'Resposta da questão {c+1}: ')
            if r == 'a' or r == 'b' or r == 'c' or r == 'd' or r == 'e':
                resposta += r.upper()
                c += 1
            else:
                print('\nInsira as respostas como sendo A, B, C, D ou E \n')
                c = c

        for i in range(qtd_questoes):
            if resposta[i] == gabarito[i]:
                acerto += 1
            else:
                erro += 1

        qtd_acerto.append(acerto)
        qtd_erro.append(erro)
        nota.append((nota_maxima/qtd_questoes)*acerto)

        os.system('clear')

    #  resultados (gabarito x resposta(por aluno))
    elif op == 3:
        os.system('clear')
        x = 0
        while x < qtd_alunos:
            print(f'Aluno: {nome_do_aluno[x]} \n')
            print(f'Gabarito --- Respostas')
            print('-----------------------')
            x += 1

            c = 0
            while c < qtd_questoes:
                print(f'{gabarito[c]}            {resposta[c]}')
                print('-----------------------')
                c += 1

            print()
            c += 1

        input('\nPressione ENTER para sair dos resultados \n')
        os.system('clear')


os.system('clear')
