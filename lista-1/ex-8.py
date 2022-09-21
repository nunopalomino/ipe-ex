""" 8) Faça um programa que leia o nome, sexo e idade. Se sexo for feminino e
idade menor que 25, imprimir em tela o nome da pessoa e a palavra
ACEITA. Caso contrário exibir NÃO ACEITA. """

nome = input("Digite o nome: ")
sexo = input("Digite o sexo: ")
idade = float(input("Digite a idade: "))

if sexo == "feminino" and idade < 25:
    print(f"{nome} ACEITA")
else:
    print("NÃO ACEITA")
