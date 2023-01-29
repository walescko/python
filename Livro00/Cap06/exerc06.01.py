#Exercício 6.1 - Cálculo da média com entrada de 7 valores
notes = [0, 0, 0, 0, 0, 0, 0]
sum = 0


i = 0
while i < len(notes):
    notes[i] = float(input(f"Nota {i+1}: "))
    sum += notes[i]
    i += 1

i = 0
while i < len(notes):
    print(f"Nota {i+1} é {notes[i]:^5.2f}")
    i += 1
print(f"A média é {sum/i:5.2f}")