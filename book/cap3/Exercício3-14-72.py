#Python - Exercício 3.14, página 72
#Programa Aluguel de Carro
print('WALESCKO SOFTWARE SOLUTIONS')
print('Aluguel de veículo')
dias = float(input('Quantos dias ficará com o carro alugado? '))
km = float(input('Quantos quilometros irá percorrer? '))
valordia = dias * 60
valorkm = km *0.15
print(f'Para {dias} de carro alugado custará R$ {valordia:.2f}.')
print(f'Para a quilometragem de {km} km o custo será R$ {valorkm:.2f}.')
total = valorkm + valordia
print(f'O valor total do aluguel será R$ {total}.')