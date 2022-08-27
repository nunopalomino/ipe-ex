# Faca um programa que leia em valor representando o gasto realizado por um cliente do
# restaurante do COMABEM e imprima o valor total a ser pago, considerando os 10% do garcom

import os

os.system("cls")
gasto = float(input("Digite o valor de gastos do cliente: "))
dezporcento = gasto * 0.10
total = gasto + dezporcento

print(f"O total a pagar é R$ {total:.2f}")