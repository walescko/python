#Escreva um programa que leia dois números e pergunte qual operação deseja realizar.
print("Walescko Loma Linda")
print("Mudamos de Walescko Software para Walescko Loma Linda")
number01 = int(input("Entre com um número: "))
number02 = int(input("Entre com um número: "))
print("Qual operação quer realizar?")
print("Adicação ....... 1")
print("Subtraçao ...... 2")
print("Multiplicação .. 3")
print("Divisão ........ 4")
choice = input("Operação? ")
result = 0
op = ""

if choice == "1":
    result = number01+number02
    op = "+"
elif choice == "2":
    result = number01 - number02
    op = "-"
elif choice == "3":
    result = number01 * number02
    op = "*"
elif choice == "4":
    if number02 != 0:
        result = number01/number02
        op = "/"
    else:
        print("Divisão por zero!")

if number02 != 0:
print(f"{number01} {op} {number02} = {result}")


