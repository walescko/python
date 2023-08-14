# Programa 8.5 - factorial with recursive function
#Função recursiva é um saco, se errar o programa pode entrar em um loop infinito

def factorial(n):
    if n == 0 or n == 1: # casos bases
        return 1
    else:
        return n * factorial(n-1) # caso recursivo

n = float(input("Entre um número para calcular o fatorial: "))
print(f"O fatotial de {n} é {factorial(n)}")