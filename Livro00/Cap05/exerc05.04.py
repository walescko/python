#Imprimir os números ímpares do zero até o número que o usuário escolher
print("Walescko Loma Linda")
end = int(input("Qual o último número da sequência númerica? "))
x = 0
while x <= end:
    if x % 2 != 0:
        print(f"{x}")
    x = x + 1

print("end program")
