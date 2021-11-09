#Python - Exercício 00
#Faça um programa para ler números e armazená-los em uma lista.
#Depois mostre a lista montada.
print("WADAJU SOFTWARE SOLUTION")
print("Leitura e apresentação de Vetor")
vetor = []
while True:
    numero = int(input('Entre com um número, ou digite 0 zero para encerrar: '))
    if numero == 0:
        break
    vetor.append(numero)
i = 0
while i < len(vetor):
    print(vetor[i], end = " ")
    i += 1
