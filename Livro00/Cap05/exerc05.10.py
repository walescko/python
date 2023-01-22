points = 0
question = 1
while question <= 3:
    answer = input(f"Resposta da questão {question}: ")
    if question == 1 and (answer == "b" or answer == "B"):
        points = points + 1
    if question == 2 and (answer == "a" or answer == "A"):
        points = points + 1
    if question == 3 and (answer == "c" or answer == "C"):
        points = points + 1
    question = question + 1

print(f"O aluno fez {points} pontos.")
