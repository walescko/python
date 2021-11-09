#Python - Exercício 5.4 - página 87
#Modifique o programa anterior (segundo exemplo do livro, página 87) para
#imprimir de 1 até o número digitado pelo usuário, mas dessa vez, apenas os números ímpares.
print('WADAJU SOFTWARE SOLUTIONS')
print('Enumeração de números ímpares de 1 até n')
fim = int(input('Qual o último número? '))
n = 0
while n <= fim:
    teste = n % 2
    if teste != 0:
        print(n)
    n = n + 1
print('fim')