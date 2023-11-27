#Programa 8.15 - função que mostra o mairo valor com número inderminado de parâmetros
def printMajor(mesage, *numbers):
    major = None
    for e in numbers:
        if major is None or major < e:
            major = e
    print(mesage, major)


printMajor("Maior", 5, 6 ,7 ,3, 9, 33, 4 , 1)
printMajor("Max", 2, 64, 32, 1024, 512, 128, 16, 4)