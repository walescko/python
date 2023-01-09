print("Walescko Software")

number01 = int(input("Informe o primeiro numero: "))
number02 = int(input("Informe o segundo numero: "))
number03 = int(input("Informe o terceiro numero: "))

maior = 0
menor = 0

if (number01 > number02 and number01 > number03):
    maior = number01
if (number01 < number02 and number01 < number03):
    menor = number01

if (number02 > number01 and number02 > number03):
    maior = number02
if (number02 < number01 and number02 < number03):
    menor = number02

if (number03 > number01 and number03 > number02):
    maior = number03
if (number03 < number01 and number03 < number02):
    menor = number03

print("Maior = ", maior)
print("Menor = ", menor)

