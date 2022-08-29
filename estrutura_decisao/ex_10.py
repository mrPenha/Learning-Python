"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

print('Qual turno você estuda?')
print('[M]atutino')
print('[V]espertino')
print('[N]oturno')
print()

turno = input('Digite a letra referente ao turno: ')
turno = turno.lower()
print()

if turno == 'm':
    print('Bom dia!')

elif turno == 'v':
    print('Boa Tarde!')

elif turno == 'n':
    print('Boa Noite!')

else:
    print('Valor Inválido!')

print()
