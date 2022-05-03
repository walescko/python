#Exercicio 3.9 - calcular o tempo em segundos
print("Walescko Software")
dia = int(input("Entre com o número de dias: "))
horas = int(input("Entre com o número de horas: "))
minutos = int(input("Entre com o número de minuto: "))
segundos = int(input("Entre com o número de segundos: "))

tempoTotal = (((dia*24 + horas)*60)+minutos)*60 + segundos

print(f"Tempo total {tempoTotal} segundos")