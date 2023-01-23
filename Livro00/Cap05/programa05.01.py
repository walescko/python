#Programa 5.1 - Contagem de Cédulas
value = int(input("Digite o valor a pagar: "))
cedule = 0
actual = 50
clear = value
while True:
    if actual <= clear:
        clear -= actual
        cedule += 1
    else:
        print(f"{cedule} cedula(s) de R$ {actual}")
        if clear == 0:
            break
        if actual == 50:
            actual = 20
        elif actual == 20:
            actual = 10
        elif actual == 10:
            actual = 5
        elif actual == 5:
            actual = 2
        cedule = 0