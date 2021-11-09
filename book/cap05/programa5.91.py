#Python - Programa da função break - página 91
#O programa soma os números digitados até que se digite '0'.
#no fim ele apresenta a soma.
s = 0
while True:
    v = int(input('Digite um número a somar ou 0 para encerrar: '))
    if v == 0:
        break #função para encerrar o while
    s +=v
print(f'A soma dos número digitados é {s}')