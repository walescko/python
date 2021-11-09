#Python - Exercício 3.12 - página 72
#Calculo do tempo de viagem
print('WADAJU SOFTWARE SOLUTIONS')
print('Previsão de tempo de viagem')
velocidade = int(input('Qual a velocidade média prevista em km/h? '))
distancia = int(input('Qual a distância a ser percorrida, em km? '))
tempo = distancia // velocidade
tempor = (distancia % velocidade)
print(f'para a viagem de {distancia:.1f} km com velocidade média de {velocidade:.1f}km/h')
print(f"o tempo previsto de viagem será  {tempo} h {tempor} minutos")