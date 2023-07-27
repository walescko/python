# Programa 6.24 - Exemplo de dicionário com valor padrão
d = {}
for letter in "Jesus Is the Savior":
    d[letter] = d.get(letter, 0) + 1
print(d)