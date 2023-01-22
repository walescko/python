points = 0
question = 1
while question <= 3:
    answer = input(f"Resposta da questão {question}: ")
    if question == 1 and answer == "b":
        points = points + 1
    if question == 2 and answer == "a":
        points = points + 1
    if question == 3 and answer == "c":
        points = points + 1
    question = question + 1

print(f"O aluno fez{points} pontos.")
