#add elements - append: adiciona elemento no final da lista
L = []
L.append("a")
print(f"Lista {L}")
L.append("b")
print(f"Lista {L}")
L.append("c")
print(f"Lista {L}")
print(f"A lista L tem tamanho {len(L)}")

#Podemos também adiconar listas na lista:
Z = []
Z = Z + [1]
print(f"Lista {Z}")
Z = Z + [2]
print(f"Lista {Z}")
Z = Z + [3 , 4, 5]
print(f"Lista {Z}")

#append vs extends, extend apenas para adicionar oe elementos da lista dentro de uma lista, se usar o append adicionara na posição uma lista de elementos.
X = []
X.append("a")
print(f"Lista {X}, comprimento da lista: {len(X)}")
X.append("b")
print(f"Lista {X}, comprimento da lista: {len(X)}")
X.extend(["c"])
print(f"Lista {X}, comprimento da lista: {len(X)}")
X.append(["d", "e"])
print(f"Lista {X}, comprimento da lista: {len(X)}")
X.extend(["f", "g", "h"])
print(f"Lista {X}, comprimento da lista: {len(X)}")
print(f"Elementos da Lista na posição 3: {X[3]}, comprimento da lista interna: {len(X[3])}")
print(f"Elemento 1 da posição 3 da lista: {X[3][1]}")
