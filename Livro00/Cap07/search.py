s = "Alô mundo"
print(s.find("mun")) #posição onde se encontra o primeiro caracter da string procurada
print(s.find("ok")) # retorna o valor -1, que significa não encontrada

s = "Um dia de sol"
print(s.rfind("d")) # pesquisa reversa
print(s.find("d"))

s = "um tigre, dois tigres, três tigres"
print(s.find("tigres"))
print(s.rfind("tigres"))
print(s.find("tigres", 7)) # inicio 7
print(s.find("tigres", 30)) # inicio 30
print(s.find("tigres", 0, 10)) #inicio 0, fim = 10
