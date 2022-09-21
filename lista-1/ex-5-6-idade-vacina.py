""" 5) Faça um programa que receba uma idade qualquer e mostre a mensagem
de acordo com ela. Se a idade for igual ou menor que 5 anos, exibir em tela
que a criança deve ser vacinada. """

import os

os.system("cls")

idade = int(input("Digite a idade da criança: "))
if idade <= 5:
    print("Criança deve ser vacinada.")
    """ 6) Alterar o programa acima para que mostre a mensagem que criança não
precisa ser vacinada se a idade for maior que 5. """
else:
    print("Criança não precisa ser vacinada. Confira se as vacinas estão em dia.")
