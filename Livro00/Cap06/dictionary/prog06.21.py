# Programa 6.21 - Obtenção do preço com um dicionário
table = {"Alface": 0.45,
         "Batata": 1.20,
         "Tomate": 2.30,
         "Feijão": 1.50}
while True:
    product = input("Digite o nome do produto, fim para terminar: ")
    if product == "fim":
        break
    if product in table:
        print(f"Preço: R$ {table[product]:5.2f}")
    else:
        print("Produto não encontrado!")
