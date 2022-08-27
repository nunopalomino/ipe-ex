# Faca um software que solicite o numero de horas trsabalhadas, o valor recebido por hora e o percentual de desconto (INSS)
# de um funcionario que trabalha por hora. O algoritmo devera mostrar o salairo bruto, o valor descontado e o valor do salario liquido

import os

os.system("cls")

horas_trab = int(input('Digite as horas trabalhadas: '))
valor_hora = float(input('Digite o valor recebido por hora: '))
percentual_desconto = (
    (int(input('Digite o percentual de desconto: '))) / 100) + 1

salario_bruto = horas_trab * valor_hora
valor_descontado = salario_bruto * percentual_desconto
salario_liquido = salario_bruto - valor_descontado

print('O salário bruto é: {0:.2f}'.format(salario_bruto))
print('O valor descontado é: {0:.2f}'.format(valor_descontado))
print('O salário líquido é: {0:.2f}'.format(salario_liquido))
