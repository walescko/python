end = int(input("Digite o último número a imprimir: "))
x = 0
while x <= end:
    if x % 2 == 0:
        print(f"{x}")
    x = x + 1