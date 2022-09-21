""" 2) Escreva um software para calcular o consumo médio de um automóvel (medido em
Km/I), dado que são conhecidos (digitados pelo usuário) a distância total percorrida e
o volume de combustível consumido para percorrê-la (medido em litros). """


km = float(input("Digite a kilometragem: "))
volume = float(input("Digite o volume do combustivel: "))

kml = km / volume

print(f"{kml=}")