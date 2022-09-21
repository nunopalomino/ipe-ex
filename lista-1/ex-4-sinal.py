""" 4) Escrever um programa que receba dois números e o sinal de + ou - e
efetue a soma ou subtração de acordo com o sinal. """

import os

os.system("cls")

sinal = input("Digite o sinal")
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o primeiro numero: "))

if sinal == "+":
    res = num1 + num2
elif sinal == "-":
    res = num1 - num2

print(f"{res=}")