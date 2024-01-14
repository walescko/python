#Programa 8.12 - funções como parâmetro
def sum(a, b):
    return a + b

def odd(a, b):
    return a - b

def printReturn(a, b, foper):
    print(foper(a, b))

printReturn(5, 4, sum)
printReturn(10, 2, odd)