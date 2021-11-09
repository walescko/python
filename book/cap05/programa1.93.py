#programa de gera a tabuada dos 10 primerios números de 1 até 10
tabuada = 1
while tabuada <= 10 :
    numero = 1
    while numero <= 10 :
        resultado = tabuada * numero
        print(f'{tabuada} x {numero} = {resultado}')
        numero += 1
    tabuada += 1