# Programa 6.19 - Criação e impressão da lista de compras

shop = []

while True:
    product = input("Produto: ")
    if product == "fim":
        break
    amount = int(input("Quantidade: "))
    price = float(input("Preço: R$ "))
    shop.append([product, amount, price])

sum = 0.0

for e in shop:
    print(f"Produto: {e[0]:20s} Quantidade: {e[1]:5d} Preço Unitário: R$ {e[2]:6.2f} Total: R$ {e[1]*e[2]:6.2f}")
    sum += e[1]*e[2]
print(f"Total: R$ {sum:7.2f}")
