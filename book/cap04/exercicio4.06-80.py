#Python - Exercício 4.6 - página 80
#Preço da passagem dependente da quilometragem
print('WADAJU SOFTWARE SOLUTIONS')
distancia = float(input('Qual a distância a percorrer? '))
#passagem = 0
if distancia <= 200:
    passagem = distancia*0.50
else:
    passagem = distancia*0.45
print(f'A o valor a ser pago é {passagem:5.2f}')
