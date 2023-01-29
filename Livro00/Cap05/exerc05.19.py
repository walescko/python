value = float(input("Digite o valor a pagar: "))
cedule = 0
actual = 200.00
clear = value
while True:
    if actual <= clear:
        clear -= actual
        cedule += 1
    else:
        print(f"{cedule} cedula(s)/moeda(s) de R$ {actual:5.2f}")
        if clear == 0:
            break
        if actual == 200:
            actual = 100
        elif actual == 100:
            actual = 50
        elif actual == 50:
            actual = 20
        elif actual == 20:
            actual = 10
        elif actual == 10:
            actual = 5
        elif actual == 5:
            actual = 2
        elif actual == 2:
            actual = 1
        elif actual == 1:
            actual = 0.50
        elif actual == 0.50:
            actual = 0.25
        elif actual == 0.25:
            actual = 0.10
        elif actual == 0.10:
            actual = 0.05
        elif actual == 0.05:
            actual = 0.01
        cedule = 0
