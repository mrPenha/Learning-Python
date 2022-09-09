"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16."""
import os
os.system('clear')

print('CÁLCULO DO FATORIAL \n\nInsira apenas números inteiros positivos e menores que 16\n')

cont = 1
while cont > 0:
    numero = input('Informe o número a ser fatorado: ')
    print()

    if ',' in numero:
        numero = numero.replace(',', '.')
    else:
        pass

    if numero.isnumeric():
        numero = float(numero)

        if numero != 0 and numero % numero == 0:
            numero = int(numero)

            if numero > 0 and numero < 16:

                novo_num = numero
                print()

                print(f'{numero} = {numero}', end='')

                cont = 0
                while cont < numero:
                    novo_num -= 1
                    if novo_num == 0:
                        break
                    else:
                        print(f'*{novo_num}', end='')

                    r = numero * novo_num

                    if novo_num == 1:
                        print(f' = {r:,.0f}')

                    numero = r
                    novo_num = novo_num

                    cont += 1

                print()

                sair = input('Gostaria de continuar? [S][N]: ')
                sair = sair.lower()

                if sair == 's':
                    os.system('clear')
                    print()
                    cont = 1
                else:
                    print('\nVolte Sempre! \n')
                    quit()

            else:
                os.system('clear')
                print(
                    '\nÉ permitido a entrada somente de números inteiros e positivos menores que 16 \n')

        else:
            os.system('clear')
            print(
                '\nÉ permitido a entrada somente de números inteiros e positivos menores que 16 \n')

    else:
        os.system('clear')
        print('\nÉ permitido a entrada somente de números inteiros e positivos menores que 16 \n')

        tentar = input('Gostaria de tentar novamente? [S][N]: ')
        tentar = tentar.lower()

        if tentar == 's':
            os.system('clear')
            print()
            cont = 1
        else:
            print()
            quit()
