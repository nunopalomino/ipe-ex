# Criar uma lista e usando for preencher valores inteiros de 2000 a 5000.
# Solicitar que o usuário digite um valor entre 2000 e 5000.
# Exibir o índice relacionado ao valor digitado pelo usuário.

lista = []

for i in range(2000, 5001):
    lista.append(i)
valor = int(input('Digite um valor entre 2000 e 5000: '))

print(lista.index(valor))
