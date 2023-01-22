sum = 0
i = 0
while True:
    value = int(input("Digite um número a somar ou 0 para sair: "))
    if value == 0:
        break
    sum += value
    i += 1
print(f"A soma dos números é {sum}")
average = sum/i
print(f"A média dos números digitados é {average}")
