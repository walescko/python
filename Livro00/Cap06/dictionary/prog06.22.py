# Programa 6.22 - Dicionário com estoque e operações de vendas
stock = {"Alface": [1000, 2.30],
         "Tomate": [500, 0.45],
         "Batata": [2001, 1.20],
         "Feijão": [100, 1.50]}

for key, datas in stock.items():
    print("Descrição: ", key)
    print("Quantidade: ", datas[0])
    print(f"Preço: {datas[1]:6.2f}\n")

shopping = [["Tomate", 5], ["Batata", 10], ["Alface", 5]]
total = 0
print("Vendas: \n")
for operation in shopping:
    product, amount = operation
    price = stock[product][1]
    cost = price * amount
    print(f"{product:12s}: {amount:3d} x { price:6.2f} = {cost:6.2f}")
    stock[product][0] -= amount
    total += cost
print(f"Custo total: {total:21.2f}\n")
print("Estoque:\n")
for key, datas in stock.items():
    print("Descrição: ", key)
    print("Quantidade: ", datas[0])
    print(f"Preço: {datas[1]:6.2f}\n")


