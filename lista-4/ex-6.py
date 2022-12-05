# Criar uma lista e usando while gerar valores inteiros aleatórios de 1 a 10 exibindo estes valores gerados,
# preencher a lista com 10 inteiros diferentes na ordem em que são gerados.
# Ao final exibir a lista, depois ordenar os valores do menor para o maior e exibir a lista ordenada

import random

lista = []
i = 0

while i < 10:
    valor = random.randint(1, 10)
    if valor not in lista:
        lista.append(valor)
        i += 1

print(lista)
lista.sort()
print(lista)