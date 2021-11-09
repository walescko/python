#Python - Exercício 5.7
#Faça um programa que apresente a tabuada de um número informado pelo usuário.
#O usuário deve informar também o início e o fim da tabuada.
print('WADAJU SOFTWARE SOLUTIONS')
a = int(input('Entre com um número: '))
i = int(input('Entre com início da tabuada: '))
j = int(input('Entre com o fim da tabuada: '))
print('A tabuada do número {a} é:')
r = 0
while i <= j:
    r = a * i
    print(f'{a} * {i} = {r}')
    i = i + 1
print('Fim')