#Python - Exercício 3.15, página 72
print('WADAJU SOFTWARE SOLUTIONS')
print('Redução do tempo de vida de um fumante')
cigarros = float(input('Quantos cigarros fuma diariamente? '))
anos = float(input('Quantos anos é fumante? '))
tcigarros = cigarros*100
tvida = tcigarros*anos/(365*24)
print(f'O tempo de vida será reduzido em {tvida:.2f} anos')