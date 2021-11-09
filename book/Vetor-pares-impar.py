#Programa simples que lê dois números inteiros positivos.
#O programa deve armazenar os números do intervalo em pares e impares em vetores/listas.
#No fim o programa deve apresentar os números pares e ímpares separados e a soma deles.
print('WADAJU SOFTWARE SOLUTIONS')
print('Números pares e ímpares de um intervalo.')
print('Soma dos números pares e dos números ímpares')
inicio = int(input('Qual o número inicial do intervalo? '))
final = int(input('Qual o número final do intervalo? '))

intervalo = final - inicio
n1 = inicio
n2 = final
print(f'A quantidade de elementos no intervalo é {intervalo + 1}')
#montando o vetor
v = list(range(n1,n2+1))
par =[]
impar = []
sumPar = 0
sumImpar = 0
for i in v:
    if i % 2 == 0:
        par.append(i)
        sumPar = sumPar + i
    else:
        impar.append(i)
        sumImpar = sumImpar + i
print("Números pares: ", par)
print(f"Soma dos pares {sumPar}")
print('Números ímpares: ', impar)
print(f"Soma dos ímpares {sumImpar}")