print("Walescko Loma Linda - 2023")
print("Rendimento Mensal")
deposito = float(input("Qual o valor do depósito? "))
juros = float(input("Qual o valor do juros a receber em %? "))
taxa = juros/100
i = 1
montante = deposito
while i <= 24:
    print(f"Mês {i}: Valor  R$ {montante:5.2f}")
    montante = montante*(1+taxa)
    i = i + 1
