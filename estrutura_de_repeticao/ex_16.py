"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500."""
print()

a = 0
b = 1
c = 0
while True:
    c = a+b
    if a+b > 500:
        break
    else:
        print(c, end=', ')
        a = b
        b = c
        c = a


print()
