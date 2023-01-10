#Desenvolva um programa para aprovar o empréstimo bancṕario para compra de uma casa.
#O programa deve perguntar o valor da casa, o salário e a quantidade de anos para pagar.
#O valor da prestação não pode ser superior a 30% do salário.
#Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
print("Walescko LomaLinda")
print("Simulação de Finaciamento")
price = float(input("Qual o valor do imóvel?"))
sale = float(input("Qual o salário? "))
timeYears = int(input("Quantos anos de financiamento?"))

time = timeYears*12
prestacao = price / (time)

maxPrestecao = sale*0.3

if(maxPrestecao <= prestacao):
    print(f"Prestação R$ {prestacao} durante {time}")
else:
    print("Finaciamento negado.")