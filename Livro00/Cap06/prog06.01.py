#Programa 6.1 - Cálculo da média
notes = [6, 7, 5, 8, 9]
sum = 0

i = 0
while i < len(notes):
    sum += notes[i]
    i += 1
print(f"A média é {sum/i:^5.2f}!")
