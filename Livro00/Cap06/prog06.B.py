#Fatiamento e Cópia de Listas
#Usando o operador atribuição damos um apelido para a lista.
L = [1, 2, 3, 4, 5]
V = L
print(f"Lista original: {L}")
print(f"Lista cópia (alias) {V}")

V[0] = 99
print(L[0])
print(f"Lista original: {L}")
print(f"Lista cópia (alias): {V}")

#Para fazer uma cópia de uma lista, não apenas um apelido
L = [1, 2, 3, 4, 5]
V = L[:]
print(f"Lista original: {L}")
print(f"Lista cópia: {V}")
V[0] = 99
print(L[0])
print(f"Lista original: {L}")
print(f"Lista cópia: {V}")
#Fatiamento de Lista
print(L[0:5])
print(f"Apresetnando a lista usando len: {L[0:len(L)]}")
print(f"Apresetando a lista com len com [:n]: {L[:len(L)]}")
print(f"Apresetando as posições 1 a 3: {L[1:3]}")
print(f"Apresetando as posições 1 a 4: {L[1:4]}")
print(f"Apresetando as 3 posições finais: {L[:3]}")
print(f"Apresetando as 3 posições iniciais: {L[3:]}")
print(f"Apresetando o último elemento: {L[-1]}")
print(f"Apresetando o penúltimo elemento: {L[-2]}")



