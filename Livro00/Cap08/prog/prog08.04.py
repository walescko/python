# Programa 8.4 - Fatorial again

def factorial(n):
    fat = 1
    x = 1
    while x <= n:
        fat *= x
        x += 1
    return fat

n = float(input("Entre um número para calcular o fatorial: "))
print(f"O fatotial de {n} é {factorial(n)}")
