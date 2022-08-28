# Construa um software que informe as raizes de uma equacao do segundo grau.
# Sendo que os valores a, b e c sao fornecidos pelo usuario se for possivel
# Caso contrario apresentar mensafem conveninte para o usuario.

import os

os.system("cls")

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

if a == 0:
    print('O valor de a não pode ser 0')
else:
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('Delta é menor que 0')
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print('x1 = {0:.2f}'.format(x1))
        print('x2 = {0:.2f}'.format(x2))
