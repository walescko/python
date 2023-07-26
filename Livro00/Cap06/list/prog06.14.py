# Programa 6.14 - Lendo e imprimindo uma lista de compras
shopping = []
while True:
    product = input("Produto: ")
    if product == "fim":
        break
    shopping.append(product)
for p in shopping:
    print(p)

