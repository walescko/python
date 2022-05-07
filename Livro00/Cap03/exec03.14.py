#Valor de pagar do aluguel de um veículo
print("Walescko Software")
print("Cálculo do valor a pagar de Aluguel de veículo")

rentDays = int(input("Quantos dias ficou alugado do veículo? "))
runKilometers = int(input("Quando quilometros foram percorridos? "))

payCar = rentDays * 60 + runKilometers * 0.15

print(f"O valor a pagar para {rentDays} dias de alguel e {runKilometers} km rodados será de {payCar:.2f}")


