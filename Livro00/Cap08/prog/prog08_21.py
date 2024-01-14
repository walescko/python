#Programa 8.21 - Navegando listas a partir do tipo de seus elementos
L = ["a", "Alô", ["!"], {"a": 1, "b": 2}]
for x in L:
    if type(x) is str:
        print(x)
    else:
        print("Lista", end="")
        for z in x:
            print(f"{z}", end="")
        print()