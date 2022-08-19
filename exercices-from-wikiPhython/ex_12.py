""" Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58 """

altura = float(input('Insira sua altura separando com um ponto: '))
peso_ideal = (72.7*altura) - 58
print(f'{peso_ideal:.2f}')