#Exercicio 3.11 - Ler o valor de uma mercadoria e o desconto, depois informar o valor do desconto e o preco final
print("Walescko Software")

preco = float(input("Preço da Mercadoria: R$ "))
desconto = float(input("Percentual de Desconto (%): "))

valorDesconto = preco * desconto/100
preco = preco - valorDesconto

print(f"Desconto R$ {valorDesconto:.2f}")
print(f"Preço final R$ {preco:.2f}")