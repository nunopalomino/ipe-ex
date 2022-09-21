""" 2) Faça um programa que calcule a média aritmética entre três números
recebidos em tela.
Média aritimética: soma dos valores dividido pelo número de valores somados.
"""

import os

os.system("cls")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))
media = (num1 + num2 + num3) / 3

print(f"A média é {media}")