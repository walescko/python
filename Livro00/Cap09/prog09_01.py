#Programa 9.01 - Abrindo, lendo e fechando um arquivo
file = open("numbers.txt", "r")

for line in file.readlines():
    print(line)

file.close()
