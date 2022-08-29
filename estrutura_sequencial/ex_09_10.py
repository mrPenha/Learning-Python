# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#     C = 5 * ((F-32) / 9). 
print('Fahrenheit ---> Celsius')
temp_f = int(input('Insira a temperatura em Fahrenheit: '))
temp_c = 5 * ((temp_f-32) / 9)
print(f'A temperatura convertida é de {temp_c:.0f}ºC.')
print()

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
print('Celsius ---> Fahrenheit')
temp_c = int(input('Insira a temperatura em Celsius: '))
temp_f = (temp_c * 9/5) + 32
print(f'A temperatura convertida é de {temp_f:.0f}ºF.')