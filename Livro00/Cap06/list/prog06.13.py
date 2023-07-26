# Programa 6.13 - Copy elements for other list
V = [9, 8, 7, 12, 0, 13, 21]
P = []
O = []
for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        O.append(e)
print('Pares: ', P)
print('Ímpares: ', O)