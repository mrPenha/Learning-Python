"""Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. """
print()

a = 80000
b = 200000

#  tx crescimento A = 3% / B = 1.5%
a = (a*3)/100+a
b = (b*1.5)/100+b

anos = 0

while a < b:
    #  tx crescimento A = 3% / B = 1.5%
    a = ((a*3)/100)+a
    b = ((b*1.5)/100)+b
    anos += 1

if a > b:
    a = f'{a:_.3f}'
    a = a.replace('.', ',').replace('_', '.')
    b = f'{b:_.3f}'
    b = b.replace('.', ',').replace('_', '.')

    print('População inicial: \nA = 80.000 \nB = 200.000 \n\n')
    print(f'População país A: {a} \n')
    print(f'População país B: {b} \n')
    print(
        f'Para que a população de A ultrapasse a de B são necessários {anos} anos.')

print()
