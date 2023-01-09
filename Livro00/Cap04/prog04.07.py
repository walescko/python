#Programa 4.7 - Categoria x preço: if elif else
category = int(input("Digite a categoria do produto: "))

if category == 1:
    price = 10
elif category == 2:
    price = 18
elif category == 3:
    price = 23
elif category == 4:
    price = 26
elif category == 5:
    price = 31
else:
    print("Categoria inválida, digite um valor de 1 a 5!")
    price = 0

print(f"O preço do produto é R$ {price:6.2f}")