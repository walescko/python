#Programa 6.7 - Simulação de uma fila de Banco
last = 10
line = list(range(1, last+1))
while True:
    print(f"\nExistem {len(line)} clientes na fila")
    print(f"Fila atual: {line}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operator = input("Operação (F, A ou S:) ")
    if operator == "A":
        if len(line) > 0:
             atendimento = line.pop(0)
             print((f"Cliente {atendimento} atendido"))
        else:
             print("Fila Vazia!Não há ninguém para atender!")
    elif operator == "F":
        last += 1
        line.append(last)
    elif operator == "S":
        break
    else:
        print("Operação inválida! Digite F, A ou S")

