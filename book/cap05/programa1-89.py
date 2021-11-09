#Python - programa 1, página 90
#Programa que soma uma sequência de 10 números digitados pelo usurário
n = 1 #variável de controle
soma = 0 #iniciando a soma
while n <=10:
    x = int(input(f"Digite o {n}º número: "))
    soma = soma + x #acumulando a variável soma
    n = n + 1 #controle do contador para o comando while
print(f'Soma = {soma}')
