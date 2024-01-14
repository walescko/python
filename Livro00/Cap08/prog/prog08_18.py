#Programa 8.18 = Enter Module (entrada.py)
def intValue(message, min, max):
    while True:
        try:
            v = int(input(message))
            if v >= min and v <= max:
                return v
            else:
                print(f"Digite um valor entre {min} e {max}")
        except ValueError:
            print("você deve digitar um número inteiro")