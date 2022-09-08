"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o enésimo termo.
"""
print()

a = 0
b = 1
c = 0
for i in range(0, 10):
    c = a+b
    print(c)
    a = b
    b = c
    c = a

print()
