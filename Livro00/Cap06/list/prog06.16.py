# Programa 6.16/6.17/6.18 - Listas com elementos de tipos diferentes

product01 = ["maçã", 10, 0.30]
product02 = ["kiwi", 5, 0.75]
product03 = ["pêra", 4, 0.98]

print(product01)
print(product02)
print(product03)

shopping = [product01, product02, product03]

print(shopping)

for e in shopping:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: R$ {e[2]:5.2f} /kg\n")
