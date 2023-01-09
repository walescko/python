#Programa 4+5 - Conta telefone com três faixas de preço
minutes = int(input("Quantos minutos você utilizou este mês"))

if minutes < 200:
    price = 0.20
else:
    if minutes < 400:
        price = 0.18
    else:
        price = 0.15

print(f"Você vaio pagar este mês: R$ {minutes*price:.2f}")
