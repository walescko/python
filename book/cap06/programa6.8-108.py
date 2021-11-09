#Programa 6.8 - Pilha de pratos
prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite E ára empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S): ")
    if operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado.")
        else:
            print("Pilha vazia. Nenhum prato para lavar.")
    elif operacao == "E":
        prato += 1 #Novo prato.
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("Opção inválida. Digite E, D ou S!")