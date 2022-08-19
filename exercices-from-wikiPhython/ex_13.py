""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
    utilizando as seguintes fórmulas:
        Para homens: (72.7*h) - 58
        Para mulheres: (62.1*h) - 44.7  """

print()
h = float(input('Insira a altura separando com um ponto: '))
print()
print('Qual o seu sexo?\n\n')
print('1 - Masculino\n2 - Feminino')
op = input('Opção: ')
print()

if op == '1':
    homem = (72.7*h) - 58
    print(f'{homem:.2f}')

else:
    mulher = (62.1*h) - 44.7
    print(f'{mulher:.2f}')