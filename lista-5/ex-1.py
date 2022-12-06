# 1) Criar uma função que receba três valores do tipo float e retorne um float
# com o quadrado do 1º mais a soma dos outros dois. No bloco principal chame
# esta função e exiba o resultado.(Com retorno e com parâmetros)

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))


def quadrado(valor1, valor2, valor3):
    return valor1**2 + valor2 + valor3


print(quadrado(valor1, valor2, valor3))
