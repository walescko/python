# Programa 8.2 - with no write a function

def sum(L):
    total = 0
    x = 0
    while x < 5:
        total += L[x]
        x += 1
    return total

L = [1, 7, 2, 5, 15]
print(sum(L))
S = [1, 7, 2, 6, 15, 7 ,8]
print(sum(S))