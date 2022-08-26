""" Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). """

tamanho = float(input('Qual o tamanho de um arquivo para download: '))
velocidade = float(input('Qual a velocidade do link de internet (em Mbps): '))


#  tempo aproximado do download em minutos
tempo_min = (tamanho / velocidade) * 60
print(f'Tempo aproximado de download (em minutos): {tempo_min:.2f}')

#  para um melhor entendimento
tempo_hora = tempo_min / 60
print(f'Tempo aproximado de download (em horas): {tempo_hora:.2f}')
