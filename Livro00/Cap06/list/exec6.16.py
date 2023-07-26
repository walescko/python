# Programa 6.20 - Buble Sort

L = [1, 2, 3, 4, 5]
end = len(L)

print(f"Quantidade de elementos a ser ordenado {end}")
print(f"Vetor não ordenado: {L}")
while end > 1:
    change = False
    x = 0
    while x < (end - 1):
        if L[x] < L[x+1]:
            change = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
            print(L)
        x += 1
    if not change:
        break
    end -= 1

print(f"Vetor ordenado descrescente: {L}")