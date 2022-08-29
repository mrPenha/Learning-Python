"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = input('Digite uma letra: ')
letra = letra.lower()
print()


if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
    print('Essa letra é uma consoante.')

else:
    print('Essa letra é uma vogal.')
