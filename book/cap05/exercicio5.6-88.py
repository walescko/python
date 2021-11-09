#Python - Exercício 5.6
#Faça um programa que apresente a tabuada de um número informado pelo usuário.
print('WADAJU SOFTWARE SOLUTIONS')
a = int(input('Entre com um número: '))
print('A tabuada do número {a} é:')
i = 1 #contador - controle do while (loop)
r = 0
while i <= 10:
    r = a * i
    print(f'{a} * {i} = {r}')
    i = i + 1
print('Fim')