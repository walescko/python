sum = 0
while True:
    value = int(input("Digite um número a somar ou 0 para sair: "))
    if value == 0:
        break
    sum += value
print(f"A soma dos números é {sum}")
