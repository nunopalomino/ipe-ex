# Faca um software que solicite o numero de horas trsabalhadas, o valor recebido por hora e o percentual de desconto 
# INSS de um funcionario que trabalha por hora. O algoritmo devera mostrar o salairo bruto, o valor descontado e o valor 
# do salario liquido

import os

os.system("cls")

horas_trab = int(input('Digite as horas trabalhadas: '))
valor_hora = float(input('Digite o valor recebido por hora: '))
percentual_desconto = ((int(input('Digite o percentual de desconto: '))) / 100) + 1

resultado = (horas_trab * valor_hora) * percentual_desconto

print(f"")
