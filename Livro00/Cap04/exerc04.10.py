# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R - Residências, I - Industrias e C - Comércios.
# Calcule o preço a pagar.
print("Walescko Loma Linda")
print("Consumo de Energia Elétrica")
consumption = int(input("Consumo de kWh/mês? "))
print("Tipo de Imóvel")
print("Residencial ..... R")
print("Industrial ...... I")
print("Comercial ....... C")
typeImmobile = input("Qual o tipo de imóvel? ")

amountToPay = 0
immobile = ""

#local onde temos os valores do kWh, melhor deixar esses valores fora do bloco de seleção para ficar mais fácil alteração dos valores durante a manutenção do código.
price = 0.40
residencial02 = 0.65
noResidencialPrice01 = 0.55
noResidencialPrice02 = 0.60

if typeImmobile == "R" or typeImmobile == "r":
    immobile = "residencial"
    if consumption > 500:
        price = residencial02
elif typeImmobile == "C" or typeImmobile == "c":
    immobile = "comercial"
    if consumption <= 1000:
        price = noResidencialPrice01
    else:
        price = noResidencialPrice02
elif typeImmobile == "I" or typeImmobile == "i":
    immobile = "industrial"
    if consumption <= 5000:
        price = noResidencialPrice01
    else:
        price = noResidencialPrice02


amountToPay = consumption * price;

print(f"O valor para  imóvel {immobile} de consumo energia elétrica é  R$ {amountToPay:6.2f}")