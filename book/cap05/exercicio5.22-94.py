#Python - Exercício 5.22 - página 94
#Escreva um programa que exiba um menu de operações : adição, subtração,
#multiplicação, divisão e sair. Imprima a tabuada da operação escolhinda.
#Repita até que a opção sair seja escolhida.
while True:
    print(' WADAJU SOFTWARE SOLUTIONS ')
    print('Calculadora simples - Python')
    print('-' * 29)
    print('Escolha uma opção:')
    print('1 ................... Adição')
    print('2 ................ Subtração')
    print('3 ............ Multiplicação')
    print('4 .................. Divisão')
    print('5 ..................... Sair')
    print('-' * 29)
    opcao = int(input('Qual a opção desejada? '))
    if opcao == 5:
        break
    else:
        numero = int(input('Entre com um número: '))
        i = 1
        if opcao == 1:
            while i <= 10:
                r = 0
                r = i + numero
                print(f'{numero} + {i} = {r}')
                i = i + 1
        elif opcao == 2:
            while i <= 10:
                r = 0
                r = numero - i
                print(f'{numero} - {i} = {r}')
                i = i + 1
        elif opcao == 3:
            while i <= 10:
                r = 0
                r = numero * i
                print(f'{numero} * {i} = {r}')
                i = i + 1
        elif opcao == 4:
            while i <= 10:
                r = 0
                r = numero / i
                print(f'{numero} / { i } = {r:6.2f}')
                i = i + 1



