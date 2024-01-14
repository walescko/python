# Programa 8.10 - Função soma com parâmetros obrigatório e opcionais
def sum(a, b, printer=False):
    s = a + b
    if printer:
        print(s)
    return s

print(sum(4, 3))
print(sum(3, 5, False))
print(sum(3, 5, True))