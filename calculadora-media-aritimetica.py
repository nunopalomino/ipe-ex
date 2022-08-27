# Faca um programa que calcule a media aritimetica entre tres numeros recebidos em tela

import os

os.system("cls")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))
media = (num1 + num2 + num3) / 3

print(f"A média é {media}")