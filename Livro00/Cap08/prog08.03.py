# Programa 8.3 - Factorial

def factorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n = n - 1
    return fat

# print(factorial(3))
# print(factorial(0))
# print(factorial(1))
n = int(input("Entre um número para calcular o fatorial: "))
print(f"O fatotial de {n} é {factorial(n)}")