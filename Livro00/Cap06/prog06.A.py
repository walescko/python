Z = []
Z = [15, 8, 9]

print(Z[0])
length = len(Z)

print(f"Comprimento da lista é {length}")

i = 0
while i < length:
    print(f"Elemento {i} é {Z[i]}")
    i += 1

print(Z[1])
Z[1] = 3
print(Z[1])

i = 0
while i < length:
    print(f"Elemento {i} é {Z[i]}")
    i += 1
