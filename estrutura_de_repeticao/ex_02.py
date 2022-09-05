"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""
print()

usuario = input('Usuário: ')
senha = input('Senha: ')
print()

cont = 0
while usuario == senha:
    print('USUÁRIO e SENHA devem ser diferentes \n')
    usuario = input('Usuário: ')
    senha = input('Senha: ')
    print()
    cont += 1
