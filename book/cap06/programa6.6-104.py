#Programa 6.6 - Adição de elementos a lista
L = []
while True:
        n = int(input('Digite um número (0 sai): '))
        if n == 0:
            break
        L.append(n)
x = 0
while x < len(L):
    print(L[x], end = ' ')
    x += 1
