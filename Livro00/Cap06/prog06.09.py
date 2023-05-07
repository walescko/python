#Programa 6.9 - Sequential Search
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
find = False
x = 0
while x < len(L):
    if L[x] == p:
        find = True
        break
    x += 1
if find:
    print(f"{p} achado na posição {x}.")
else:
    print(f"{p} não encontrado.")
    