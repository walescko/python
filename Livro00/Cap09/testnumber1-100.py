#Esse programa grava em um arquivos os números de 1 a 100.
file = open("numbers.txt", "w")

for line in range(1, 101):
    file.write(f"{line}\n")
    print("Arquivo criado e salvo com sucesso.")

file.close()

