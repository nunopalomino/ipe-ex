# 4) Criar uma função que receba três números float e retorne um float com o maior valor recebido.
# No bloco principal chame esta função e exiba o resultado. Com retorno e com parâmetros.

def maiorValor(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

print("O maior número é: ", maiorValor(n1, n2, n3))
