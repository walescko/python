#Python - Exercício 4.3, página 79
#Classificação Maior e menor de três
print('WADAJU SOFTWARE SOLUTIONS')
print('Maior e menor de três')
print('Entre com três valores inteiros:')
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
#maior = 0
menor = 0
if a > b and a > c:
    maior = 0
    maior = a
if b > a and b > c:
    maior = 0
    maior = b
if c > a and c > b:
    maior = 0
    maior = c
if a < c and a < b:
    menor = 0
    menor = a
if b < c and b < a:
    menor = 0
    menor = b
if c < a and c < b:
    menor = 0
    menor = c
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
