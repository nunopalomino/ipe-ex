""" 7) Faça um programa que receba a idade de uma pessoa. Se a idade for maior
que 11 e menor 18 anos, exibir a mensagem: adolescentes. (Usar o
operador OU para fazer esta comparação). """

idade = float(input("Digite a idade: "))

if idade > 11 or idade < 18:
  print("Adolescente.")
