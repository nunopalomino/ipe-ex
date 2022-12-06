# 2) Um número natural é um número primo quando ele tem exatamente dois divisores:
# o número um e ele mesmo. Criar uma função que receba um número inteiro(positivo)
# e retorne um caractere 's' se ele for primo e 'n' caso contrário. No bloco principal
# chame esta função e exiba o resultado. (Com retorno e com parâmetro)

def primo(num):
    cont = 0
    for i in range(1, num+1):
        if num % i == 0:
            cont += 1
    if cont == 2:
        return 's'
    else:
        return 'n'


num = int(input('Digite um número: '))
print(f'O número {num} é primo? {primo(num)}')
