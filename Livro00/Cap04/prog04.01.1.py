#Programa 4.1.1 - Lê dois valores e imprime o maior deles, ou informa que os dois são iguais
number01 = int(input("Entre com um valor inteiro: "))
number02 = int(input("Entre com outro valor inteiro: "))

if number01 > number02:
    print("O primeiro valor é o maior!")
if number01 < number02:
    print("O segundo valor é o maior!")
if number01 == number02:
    print("Os valores são iguais")