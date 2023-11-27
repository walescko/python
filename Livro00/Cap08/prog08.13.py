#Progrma 8.13 - configuração de funções com funcções
def printList(L, fprint, fcondition):
    for e in L:
        if fcondition(e):
            fprint(e)

def printElement(e):
    print(f"Valor: {e}")

def pair(x):
    return x % 2 == 0

def odd(x):
    return not pair(x)

L = [1, 3, 4, 5, 7, 2, 11, 0, 55]
printList(L, printElement, odd)
printList(L, printElement, pair)
print(*L) #comando *L aqui o * desempacota a lista passando a imprimir L[n]

def barra(n=10, c="*"):
    print(c * n)
L01 = [[5, "-"], [10, "*"], [5], [6, "."]]
for e in L01:
    barra(*e)
