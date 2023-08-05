S = "Alô Mundo"
print(S[0])
print(S)
L = list(S)
L[0] = "a"
print(L)
s = "".join(L)
print(s)

name = "João da Silva"
print(f"string = {name}")
print("find João:", name.startswith("João"))
print("find Juão:", name.startswith("Juão"))
print("find Silva: ", name.endswith("Silva"))

s = "Maria Amélia Souza"
print("Amélia" in s)
print("Maria" in s)
print("Souza" in s)
print("amália" in s)

s = "O Rato roeu a roupa do rei de Roma"
print(s.lower())
print(s.upper())
print(s.lower().startswith("o rato"))
print(s.lower().startswith("O RATO"))

s = "Todos os caminhos levam a Roma"
print("leva" not in s)
print("Caminhos" not in s)
print("AS" not in s)

s = "João comprou um carro"
print("joão" in s.lower())
print("CARROS" in s.upper())
print("comprou" not in s.lower())
print("barco" not in s.lower())


