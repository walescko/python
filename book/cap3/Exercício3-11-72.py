#Python - Exercício 3.11 - página 72
#Desconto de mercadoria
print("WADAJU SOFTWARE SOLUTIONS")
print('Preço, desconto e preço a pagar')
preco = float(input("Qual o preço do produto? "))
desconto = float (input("Qual o percentual de desconto? "))
preco_final = (1-(desconto/100))*preco
print(f"O valor do produto é R$ {preco:.2f}.")
print("O desconto dado é de {descont:.2f}%")
print(f"O valor a ser pago é R$ {preco_final:.2f}")
print("Se tudo deu certo você leu essa linha")