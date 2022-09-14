"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes"""
import os
os.system('clear')

print('Pressione 0(zero) para sair')
print('---------------------------\n')
maior = 0
menor = 0
pesado = 0
leve = 0
cod_maior = 0
cod_menor = 0
cod_pesado = 0
cod_leve = 0
while True:
    codigo = int(input('Insira o código: '))
    if codigo != 0:
        if codigo != cod_maior and codigo != cod_menor and codigo != cod_pesado and codigo != cod_leve:
            c = codigo
            alt = int(input('Altura(cm): '))
            peso = input('Peso(Kg): ')
            if ',' in peso:
                peso = peso.replace(',', '.')
                peso = float(peso)
                print()
            else:
                peso = float(peso)
                print()

            #  verifica altura
            if alt > maior:
                maior = alt
                cod_maior = codigo
            elif alt < maior:
                menor = alt
                cod_menor = codigo
            else:
                maior = maior
                menor = menor
                cod_maior = codigo
                cod_menor = codigo

            #  verifica peso
            if peso > pesado:
                pesado = peso
                cod_pesado = codigo
            elif peso < pesado:
                leve = peso
                cod_leve = codigo
            else:
                pesado = pesado
                leve = leve
                cod_pesado = codigo
                cod_leve = codigo

        else:
            os.system('clear')
            print('CÓDIGO INVÁLIDO \n')

    else:
        break


os.system('clear')
#  maior altura
print(f'\nMAIOR ALTURA \nCódigo: {cod_maior} \nAltura: {maior}')

#  menor altura
print(f'\nMENOR ALTURA \nCódigo: {cod_menor} \nAltura: {menor}')

#  maior peso
print(f'\nMAIOR PESO \nCódigo: {cod_pesado} \nAltura: {pesado}')

#  menor peso
print(f'\nMENOR PESO \nCódigo: {cod_leve} \nAltura: {leve}')
