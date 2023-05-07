L = [8, 9, 15]
for e in L: #for
    print(e)

x = 0
while x < len(L): #while, mesma função do for
    e = L[x]
    print(e)
    x += 1

#For + Brek + Else
L = [7, 9, 10, 12]
p = int(input("Digite um número a pesquisar: "))
for e in L:
    if e == p:
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado.")

#Range
for v in range(10):
    print(v)

for v in range (5, 8):
    print(v)

for t in range(3, 33, 3):
    print(t, end=" ")
print()
