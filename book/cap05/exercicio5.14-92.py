#Python - Exercício 5.15, página 92
#Escreva um programa para controlar uma pequena máquina registradora.
#Você deve solicitar ao usuário que digite o código do produto e a quantidade
#comprada. Utilize a tabela de códigos da página 91 para o preço de cada produto
#O programa deve exibir o total das compras depois que o usuário digitar 0 (zero).
#Qualquer outro código deve gerar a mensagem de erro "Cógido Inválido"
print('WADAJU SOFTARE SOLUTIONS')
print('Caixa registradora simples')
soma = 0
while True:
    codigo = int(input('Qual o código do produto: '))
    if codigo == 0:
        break
    elif codigo == 1:
        n = int(input('Qual a quantidade do produto: '))
        parcela = n*0.50
    elif codigo == 2:
        n = int(input('Qual a quantidade do produto: '))
        parcela = n*1
    elif codigo == 3:
        n = int(input('Qual a quantidade do produto: '))
        parcela = n*4
    elif codigo == 5:
        n = int(input('Qual a quantidade do produto: '))
        parcela = n*7
    elif codigo == 9:
        n = int(input('Qual a quantidade do produto: '))
        parcela = n*8
    else:
        print('Código Inválido')
    soma += parcela
    parcela = 0 #zerar a parcela para não somar se código digitato for 0 (zero)
print(f'Total da compra {soma:6.2f}')