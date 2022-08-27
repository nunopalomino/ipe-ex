# Crie um programa que receba o salário bruto, calcule a gratificação (5% do salário), calcule
# o imposto (7% do salário), calcule o salário líquido (salBruto - imposto + gratif) e exiba o salário líquido

import os
from os import system

system("cls")
salBruto = float(input('Digite o salário bruto: '))
gratif = ( 5 / 100 ) * salBruto # 0.5
imposto = ( 7 / 100 ) * salBruto # 0.7
salLiquido = salBruto - imposto + gratif

print('O salário bruto é: {0:.2f}'.format(salBruto)) # :.2f = Formata com duas casas depois da vírgula, para ficar em real
print('O salário líquido é: {0:.2f}'.format(salLiquido))
print('A gratificação é: {0:.2f}'.format(gratif))
print('O imposto é: {0:.2f}'.format(imposto))
print(f"O imposto é {imposto:.2f}")