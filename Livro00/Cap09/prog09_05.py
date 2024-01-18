#Programa 9.5 - Processamento de um arquivo
LARGURA = 79
with open("enterdata.txt") as enter:
    for line in enter.readline():
        if line[0] == ";":
            continue
        elif line[0] == ">":
            print(line[1:].rjust(LARGURA))
        elif line[0] == "*":
            print(line[1:].center(LARGURA))
        else:
            print(line)
