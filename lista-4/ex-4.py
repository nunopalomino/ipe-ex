# Criar uma lista e usando for preencher com os 3000 primeiros valores pares.

lista = []

for i in range(3000):
    lista.append(i*2)
print(lista)


# Criar uma lista e usando while preencher com os 3000 primeiros valores pares.

lista = []
i = 0

while i < 3000:
    lista.append(i*2)
    i += 1
print(lista)
