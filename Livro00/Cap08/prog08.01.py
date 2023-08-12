# Programa 8.1 - Pesquisa em uma lista

def search(list, value):
    for x, e in enumerate(list):
        if e == value:
            return value
    return None

L = [10, 20, 25, 30]
print(search(L, 25))
print(search(L, 27))
