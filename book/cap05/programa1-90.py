#Python - programa 1, página 90
#Programa que soma uma sequência de 5 números digitados pelo usurário
#e mostra a soma e a média dos números digitados
n = 1 #variável de controle
soma = 0 #iniciando a soma
while n <=5:
    x = int(input(f"Digite o {n}º número: "))
    soma = soma + x #acumulando a variável soma
    n = n + 1 #controle do contador para o comando while
print(f'Soma = {soma:5.2f}')
print(f'Média = {soma/5:5.2f}')
