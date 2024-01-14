#Programa 8.11 - Função retângulo com parâmetro obrigatórios e opcionais
def retangle(width, length, character="*"):
    line = character * width
    for i in range(length):
        print(line)

retangle(8,6)
print("Vamos a outro retângulo:")
retangle(50,6)