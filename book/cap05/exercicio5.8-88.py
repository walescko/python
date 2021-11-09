#Python - Exercício 5.8 página 88
#Escrever um programa que leia dois números e apresente o resultado da multiplicação entre eles.
#Essa multiplicação deve ser feita não multiplicando dois números mas sim com soma ou subtrações.
print("WADAJU SOFTWARE SOLUTIONS")
print("Multiplicação de dois números")
print("Entre com dois valores inteiros:")
a = int(input("A = "))
b = int(input("B = "))
soma = 0
i = 1
while i <= b:
    soma = soma + a
    i = i + 1
print(f"A multiplicação de {a} por {b} é {soma}")
print(f"de forma matemática: {a} * {b} = {soma}")
print('fim')