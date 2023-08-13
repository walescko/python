# Programa 8.1 - Pesquisa em uma lista

def search(list, value):
    for x, e in enumerate(list):
        if e == value:
            return value
    return None

#Boa prática de programação - código limpo: uma função deve fazer apenas uma coisa.
def sum(L):
    total = 0
    for e in L:
        total += e
    return total
def average(L):
    return sum(L)/len(L)

#Quando se usa uma vez apenas
def average2(L):
    total = 0
    for e in L:
        total += e
    return total/len(L)


L = [10, 20, 25, 30]
print(search(L, 25))
print(search(L, 27))
print(sum(L))
print(average(L))
print(average2(L))
