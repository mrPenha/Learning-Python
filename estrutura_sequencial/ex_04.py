# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('Média bimestral! Insira as 4 notas bimestrais abaixo.')
n1 = int(input('Insira a 1ª nota: '))
n2 = int(input('Insira a 2ª nota: '))
n3 = int(input('Insira a 3ª nota: '))
n4 = int(input('Insira a 4ª nota: '))
media = (n1 + n2 + n3 + n4) / 4
#  média >=6 Passou de ano.
if media >= 6:
    print(f'Sua média = {media} \nVocê foi aprovado.')
else:
    print(f'Sua média = {media} \nVocê foi reprovado.')