#Exercicio 4.2 - Calculo de multa, R$ 5,00/km quando acima de 80km/h.
print("Walescko Software")
speed = float(input("Entre com o valor da velocidade ekm km/h: "))

if speed > 80:
    excesso = speed - 80
    multa = excesso*5
    print(f"Você deverá pagar uma multa de R$ {multa:.2f} devido a velocidade de {speed} km/h, excedendo em {excesso:.2f} km/h.")
if speed <= 80:
    print(f"A sua velocidade de {speed:.2f} km/h está em conformidade com o limite de 80km/h.")

