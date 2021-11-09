#Python - Exercício 6.1, página 99
#Faça um programa que leia 7 notas e apresente as notas e a média.
notas= [0, 0, 0, 0, 0, 0, 0]
soma = 0
i = 0
while i < 7:
    notas[i] = float(input(f'Nota {i+1}: '))
    soma += notas[i]
    i += 1
i = 0
while i < 7:
    print(f'Nota {i+1}: {notas[i]:6.2f}')
    i += 1
media = soma / 7
print(f'Média: {media:6.2f}')