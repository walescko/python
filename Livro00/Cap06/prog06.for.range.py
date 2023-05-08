L = [8, 9, 15]
print("FOR")
for e in L: #for
    print(e)

x = 0
print("WHILE")
while x < len(L): #while, mesma função do for
    e = L[x]
    print(e)
    x += 1

#For + Brek + Else
print("Pesquisa de números - pesquisa sequencial")
L = [7, 9, 10, 12]
p = int(input("Digite um número a pesquisar: "))
for e in L:
    if e == p:
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado.")

#Range
print("Range 1 a 10")
for v in range(10):
    print(v)
print("Range 5 a 8")
for v in range (5, 8):
    print(v)

print("Range multiplos de 3")
for t in range(3, 33, 3):
    print(t, end=" ")
print()
