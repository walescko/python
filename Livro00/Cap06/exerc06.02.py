#Faça um programa que leia duas listas e gere uma terceira lista com os elementos das duas listas.
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
List03.extend(List01)
List03.extend(List02)

print(f"Lista resultante: {List03}")