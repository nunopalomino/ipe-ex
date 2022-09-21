""" 10) Construa um algoritmo que calcule o IMC — Índice de Massa Corporal. Receba
como dado PESO e ALTURA. O IMC para adultos é calculado com a fórmula:
IMC = peso / (altura)2

EE IMC em IMC em
Condição Mulheres Homens
abaixo do peso ideal <19,1 <20,7
no peso ideal 19,1 - 25,8 20,7 - 26,4
marginalmente acima do
peso 25,8 - 27,3 26,4 - 27,8
acima do peso ideal 27,3- 32,3 27,8-31,1

Obeso > 32,3 >31,1 """

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

if imc < 19.1 or imc < 20.7:
    print("Abaixo do peso ideal.")
elif imc >= 19.1 and imc <= 25.8 or imc >= 20.7 and imc <= 26.4:
    print("No peso ideal.")
elif imc >= 25.8 and imc <= 27.3 or imc >= 26.4 and imc <= 27.8:
    print("Marginalmente acima do peso.")
elif imc >= 27.3 and imc <= 32.3 or imc >= 27.8 and imc <= 31.1:
    print("Acima do peso ideal.")
else:
    print("Obeso.")
