# Programa 6.23 - Exemplo de dicionário sem valor padrão
d = {}
for letter in "Jesus is the Savior":
    if letter in d:
        d[letter] = d[letter] + 1
    else:
        d[letter] = 1
print(d)
