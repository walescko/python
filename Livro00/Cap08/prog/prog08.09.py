# Programa 8.9 - Validação de inteiro usando função
def faixa_int(question, min, max):
   while True:
        v = int(input(question))
        if v < min or v > max:
            print(f"Valor inválido. Digite um valor entre {min} e {max}")
        else:
            return v


faixa_int(9, 1, 6)