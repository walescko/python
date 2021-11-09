#python - Exercício 5.11 - página 90
#Escreva um programa que pergunte o depósito inicial
#e a taxa de juros de uma poupança. Exiba os valores
#mês a mês para os 24 primeiros meses.
#Escreva o total ganho no período.
print('WADAJU SOFTWARE SOLUTIONS')
print('Redimentos de uma aplicação')
deposito = float(input('Qual o valor do depósito? '))
jurosm = float(input('Entre com o valor da taxa de juros em %: '))
saldo = deposito #variável para o dar o saldo final
m = 0 #variável para o comando while - número de meses
depositado = 0
while m <= 24:
    saldo = saldo * (1+(jurosm/100))
    print(f'Saldo no {m}º mês R$ {saldo:6.2f}.')
    m = m + 1
print(f"O saldo da poupança é de R$ {saldo:6.2f}")
rendimento = saldo - deposito
print(f"O rendimento foi de R$ {rendimento:6.2f}")
