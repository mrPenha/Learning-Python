"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1."""
import os
os.system('clear')


#  ainda tentando resolver isso


# cont = 1
# while cont > 0:
#     n = input('Insira um número inteiro: ')

#     if ',' or '.' not in n:
#         n = int(n)

#         if n != 0 and n != 1:

#             if n % 2 != 0 and n is not 2:

#                 x = 0  # número de vezes que é divisível
#                 c = 1  # divisor
#                 q = 0  # quociente
#                 r = 0  # resto da divisão
#                 while c > 0:

#                     #  quociente
#                     q = n/c

#                     r = n % c

#                     if c == 1 and n/c == n and q is not float:
#                         print('\nEste número é primo\n')
#                         x += 1
#                         c + 1

#                     else:
#                         print('\nEste número não é primo\n')

#                     if c == n and n/c == 1 and q is not float:
#                         print('\nEste número é primo\n')
#                         x += 1
#                         c += 1

#                     else:
#                         print('\nEste número não é primo\n')

#                     if x >= 2:
#                         print('\nEste número não é primo\n')
#                         break

#                     else:
#                         pass

#             else:
#                 print('\nNúmeros pares não são primos, exceto o número 2\n')
#                 tentar = input('Gostaria de tentar novamente? [S][N]: ')
#                 tentar = tentar.lower()

#                 if tentar == 's':
#                     os.system('clear')
#                     print()
#                     cont = 1
#                 else:
#                     print()
#                     quit()

#         else:
#             print('\n0 e 1 não são números primos\n')
#             tentar = input('Gostaria de tentar novamente? [S][N]: ')
#             tentar = tentar.lower()

#             if tentar == 's':
#                 os.system('clear')
#                 print()
#                 cont = 1
#             else:
#                 print()
#                 quit()

#     else:
#         print('\nInsira apenas números inteiros\n')
#         tentar = input('Gostaria de tentar novamente? [S][N]: ')
#         tentar = tentar.lower()

#         if tentar == 's':
#             os.system('clear')
#             print()
#             cont = 1
#         else:
#             print()
#             quit()

#     sair = input('Gostaria de continuar? [S][N]: ')
#     sair = sair.lower()

#     if sair == 's':
#         os.system('clear')
#         print()
#         cont += 1
#     else:
#         print('\nVolte Sempre! \n')
#         quit()
