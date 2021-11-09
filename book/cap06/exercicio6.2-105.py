#Python - Exercício 6.2, página 105
#Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras
print("WADAJU SOFTWARE SOLUTION")
print("Leitura  de 2 vetores e apresentação deles e a união deles")
vetor1 = []
while True:
    numero = int(input('Entre com um número, ou digite 0 zero para encerrar a entrada em V1: '))
    if numero == 0:
        break
    vetor1.append(numero)
vetor2 = []
while True:
    numero = int(input("Entre com um número, ou digite 0 zero para encerrar a entrada em V2: "))
    if numero == 0:
        break
    vetor2.append(numero)
i = 0
juncao = vetor1 + vetor2
while i < len(juncao):
    print(juncao[i], end = " ")
    i += 1
