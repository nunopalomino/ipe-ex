# 3) Criar uma função que receba dois números float e retorne um float com o maior valor recebido.
# No bloco principal chame esta função e exiba o resultado. Com retorno e com parâmetros.

def maior(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print(f'O maior número é {maior(num1, num2)}')
