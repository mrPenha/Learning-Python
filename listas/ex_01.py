"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""
import os
os.system('clear')

lista = []

c = 0
while c < 5:
    numeros = int(input('Número inteiros: '))
    lista.append(numeros)
    c += 1

print(lista)
