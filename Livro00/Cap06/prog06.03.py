#Program 6.3 - Apresentação de números
numbers = [0, 0, 0, 0, 0]
i = 0
while i < len(numbers):
    numbers[i] = int(input(f"Número {i+1}: "))
    i += 1

while True:
    choice = int(input("Qual a posição que quer pesquisar (0 para sair)? "))
    if choice == 0:
        break
    elif choice > len(numbers):
        print(f"Não tem número na posição {choice}! Tente Novamente")
    else:
        print(f"Você escolhei o número: {numbers[choice - 1]}")

print("END PROGRAM")
