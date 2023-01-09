#Exercicio 4.6 - Escreva um programa que pergunte a distância que um passageiro  deseja percorrer em quilometros. Calcule o preço da viagem, cobrando R$ 0.50 por km para viagens de até 200km, e R$ 0,45 para viagens mais longas
print("Walescko Software")

distance = int(input("Qual a distância a ser percorrida? "))

if distance <= 200:
    price = 0.50
if distance > 200:
    price = 0.45

print(f"O valor a ser pago para percorrer a distâncias de {distance} é R$ {distance*price:6.2f}")
