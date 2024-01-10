#Programa 8.20 - Quess number
import random
min = 1
max = 10
n = random.randint(min, max)
x = int (input(f"Escolha um número entre {min} e {max}: "))

if x == n:
    print("Você acertou!")
else:
    print("você errou!")
