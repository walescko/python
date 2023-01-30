#Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
print("WALESCKO LIMA LINDA")
print("Lista 01:")
List01 = []
print("Digite os valores da Lista 1 (0 para sair): ")
i = 0
while True:
    number = int(input(f" Entre com o {i+1} elemento: "))
    if number == 0:
        break
    List01.append(number)
    i += 1

print("Lista 02:")
List02 = []
print("Digite os valores da Lista 2 (0 para sair): ")
i = 0
while True:
    number = int(input(f" Entre com o {i+1} elemento: "))
    if number == 0:
        break
    List02.append(number)
    i += 1

List03 = []
List04 = List01[:]
List04.extend(List02)

i = 0
while i < len(List04):
    j = 0
    while j < len(List03):
        if List04[i] == List03[j]:
            break
        j += 1
    if j == len(List03):
        List03.append(List04[i])
    i += 1
i = 0

print(f"Lista 01: {List01}")
print(f"Lista 02: {List02}")
print(f"Lista Resultante: {List03}")
