#Programa 3.1 - Sequencia e tempo
divida = 0
compra = 100
divida = divida + compra
compra = 200
divida = divida + compra
compra = 300
divida = divida + compra
compra = 0

print("Dívida R$ %5.2f" %(divida))
print("Dívida R$ {:5.2f}".format(divida))
print(f"Divida R$ {divida:5.2f}")
