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
