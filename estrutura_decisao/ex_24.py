"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal."""

print()

num1 = float(input('1º número: '))
num2 = float(input('2º número: '))
print()

print('Qual operação deseja realizar?')
print('\n+ (adição) \n- (subtração) \n* (multiplicação) \n/ (divisão)')
op = input('\nOpção: ')
print()

if op == '+':
    resp = num1+num2
    print(resp)
    print()

    if resp % 2 == 0:
        print('Este número é par')
        print()
    else:
        print('Este número é impar')
        print()

    if resp < 0:
        print('Este número é negativo')
        print()
    else:
        print('Este número é positivo')
        print()

    if resp // 1 == resp:
        print('Este número é inteiro')
        print()
    else:
        print('Este número é decimal')
        print()

if op == '-':
    resp = num1-num2
    print(resp)
    print()

    if resp % 2 == 0:
        print('Este número é par')
        print()
    else:
        print('Este número é impar')
        print()

    if resp < 0:
        print('Este número é negativo')
        print()
    elif resp == 0:
        print('Este número é neutro')
        print()
    else:
        print('Este número é positivo')
        print()

    if resp // 1 == resp:
        print('Este número é inteiro')
        print()
    else:
        print('Este número é decimal')
        print()

if op == '*':
    resp = num1*num2
    print(resp)
    print()

    if resp % 2 == 0:
        print('Este número é par')
        print()
    else:
        print('Este número é impar')
        print()

    if resp < 0:
        print('Este número é negativo')
        print()
    else:
        print('Este número é positivo')
        print()

    if resp // 1 == resp:
        print('Este número é inteiro')
        print()
    else:
        print('Este número é decimal')
        print()

if op == '/':
    resp = num1/num2
    print('{:.2f}'.format(resp))
    print()

    if resp % 2 == 0:
        print('Este número é par')
        print()
    else:
        print('Este número é impar')
        print()

    if resp < 0:
        print('Este número é negativo')
        print()
    else:
        print('Este número é positivo')
        print()

    if resp // 1 == resp:
        print('Este número é inteiro')
        print()
    else:
        print('Este número é decimal')
        print()
