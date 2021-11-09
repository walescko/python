#Python - Exercício 5.14, página 91
#Escreva um programa que leia números inteiros do teclado.
#O programa deve ler os números até que o usuário digite 0 (zero).
#No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritimética
print('WADAJU SOFTWARE SOLUTIONS')
print('Soma de n números até digitar zero')
soma = 0 #soma dos números digitados
i = 0 #quantidade de números digitados
while True:
    a = int(input("Digite um inteiro ou 0 (zero) para terminar: "))
    if a == 0:
        break
    soma += a
    i += 1
media = soma / i
print(f'A quantidade de números digitados foi de {i}')
print(f'Soma = {soma}')
print(f'Média = {media}')
