#Python - Exercício 5.21, página 93 - Programa 5.1, página 92 modificado
#programa que indica o número de células a usar para pagar a conta.
#ele deve repetir até que o usuário digite zero (0)
valor = 1
cedulas = 0
atual = 50 
apagar = valor
while valor != 0:
    valor = 0
    valor = int(input('Digite o valor a pagar: '))
    cedulas = 0
    atual = 50
    apagar = valor
    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            print(f'{cedulas} cédula(s) de R$ {atual}')
            if apagar == 0:
                break
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 2
            cedula = 0
