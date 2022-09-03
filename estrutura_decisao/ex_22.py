"""Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão). """
print()

numero = float(input('insira um numero inteiro: '))

if numero // 1 == numero:
    numero = int(numero)
    if numero % 2 == 0:
        print('Esse número é par')
    else:
        print('Esse número é impar')
else:
    print('Este não é um número inteiro')

print()
