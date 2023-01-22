print("Walescko Loma Linda")
print("Eitcha devedor")
divida = float(input("Qual o valor da inicial da dívida em R$? "))
juros = float(input("Qual a taxa de juros em %? "))
parcela = float(input("Qual o valor da parcela que deseja pargar em R$ (mínimo R$ 50)? "))
meses = (divida*(1+juros/100))//parcela
print(f"Total de meses a pagar: {meses:2.0f}")
parcelado = (divida*(1+juros/100))/meses
print(f"Valor mensal da parcela: R$ {parcelado:5.2f}")
print(f"O valor total a pagar será de R$ {parcelado*meses:5.2f}")
