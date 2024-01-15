#Programa 9.03 - Gravação de números pares e ímpares em arquivos diferentes
with open("odd.txt", "w") as odd:
    with open("even.txt", "w") as even:
        for n in range(0, 1000):
            if n % 2 == 0:
                even.write(f"{n}\n")
            else:
                odd.write(f"{n}\n")

print("Program ran successfully")