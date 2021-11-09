#Python - Exercício 5.23, página 94
#Escreva um programa que leia um número e verifique se é primo ou não.
print('WADAJU SOFTWARE SOLUTIONS')
print('Teste de número primo')
numero = int(input('Qual o número inteiro e positivo para ser testado? '))
teste = numero
if numero == 0 or numero == 1:
    print('Número não pode ser testado.')
elif numero == 2:
    print(f'O número {numero} é primo.')
else:
    resto = 0
    resto = teste % 2 #se o número for par e maior que 2 não é primo.!!
    if resto == 0:
        print(f'O número {numero} não é primo.')
    else: #bloco do programa para testar se um número ímpar é primo.
        i = 3
        while i <= numero:
            resto = 0
            resto = teste % i
            if resto == 0 and i == numero:
                print(f'O número {numero} é primo.')
            elif resto == 0 and i <= numero:
                print(f'O número {numero} não é primo.')
                break
            i += 1
