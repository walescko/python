def register(cod):
    if cod == 1:
        price = 0.5
    if cod == 2:
        price = 1.00
    if cod == 3:
        price = 4.00
    if cod == 5:
        price = 7.00
    if cod == 9:
        price = 8.00
    return price

print("Walescko Loma Linda")
print("Single box register")
sum = 0
cod = 1
while cod != 0:
    print("Código dos produtos/valor:")
    print("Cód 1 .... R$ 0,50")
    print("Cód 2 .... R$ 1,00")
    print("Cód 3 .... R$ 4,00")
    print("Cód 5 .... R$ 7,00")
    print("Cód 9 .... R$ 8,00")
    print("Cód 0 .... Encerrar")
    cod = int(input("Qual produto a registrar? "))
    if cod == 1 or cod == 2 or cod == 3 or cod == 5 or cod == 9:
        sum = sum + (register(cod))
    elif cod == 0:
        print(f"Total da compra é R$ {sum:5.2f}")
        print("End Program")
    else:
        print("Código inválido, diginte novamente!")



