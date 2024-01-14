#escreva um programa para validar uma variável string.
#Essa função recebe como parâmetro a string, o número máximo e o número mínimo de caracteres.
#Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo, e falso,
#caso contrário

def validation(string, max, min):
    while True:
        s = input(string)
        length = len(s)
        if length > max or length < min:
            print("String de tamanho inválido!")
        else:
            return f"A strinf {s} tem comprimento de {len(s)}"


