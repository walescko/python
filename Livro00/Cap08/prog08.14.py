#Programa 8.14 - Função soma com número indeterminado de parâmetros
def sum(*args):
    s = 0
    for x in args:
        s += x
    return s

print(sum(2, 3))
print(sum(1, 4, 7))
print(sum(6, 7 , 3, 5, 9, 1))
print(sum(1, 1, 2, 3, 5, 8, 13, 21, 34))
print(sum(2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048))