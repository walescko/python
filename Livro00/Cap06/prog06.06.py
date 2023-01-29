#Programa 6.6 - Adição de elementos à uma lista
L = []

while True:
    number = int(input("Digite um número (0 para sair): "))
    if number == 0:
        break
    L.append(number)

i = 0
while i < len(L):
    print(L[i])
    i += 1
