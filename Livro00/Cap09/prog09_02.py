#Programa 9.02 - Uso do With
with open("numbers.txt", "r") as file:
    for line in file.readlines():
        print(line)
