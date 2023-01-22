#Escreva um programa que leia dois número e efetue a multiplicação entre eles.
#Pode-se usar apenas somas e subtrações.
print("Walescko Loma Linda - 2023")
print("Multiplicação de dois números")
n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))
i = 1
sum = 0
while i <= n2:
    sum = sum + n1
    i = 1 + i

print(f"{n1} x {n2} = {sum}")
