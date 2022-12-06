# 5) Criar uma função que receba três números float e retorne um float com o maior valor recebido,
# use a função da questão 3. No bloco principal chame esta função e exiba o resultado.
# Com retorno e com parâmetros.

def maiorValor(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


maiorValor = maiorValor(300, 40, 1000)

print(f'O maior valor é: {maiorValor}')
