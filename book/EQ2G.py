#Programa que resolve a equação do II Grau
#O usuário deve informar os coeficentes.
#O programa dará as raízes da equação, o vértice e onde cruza o eixo das ordenadas.
print('WADAJU SOFTWARE SOLUTIONS')
print("Equação do II Grau - raízes, vértice e ordenada")
terminar = 'd'
while True:
    if terminar == 's' or terminar == 'S':
        break
    else:
        print("Entre com o valor dos coeficientes:")
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
        delta = b*b - 4 * a * c
        if a == 0 or delta < 0:
            print(f"A equação {a}x² + {b}x + {c} = 0 não tem raízes reais.")
        elif delta == 0:
            x1 = -b / 2 * a
            print(f"A equação {a}x² + {b}x + {c} tem duas raízes idênticas x1 = x2 = {x1}.")
        elif delta > 0:
            x1 = (-b + delta) / 2*a
            x2 = (-b - delta) / 2*a
            print(f"A equação {a}x² + {b}x + {c} tem duas raízes reais distintas x1 = {x1} e x2 = {x2}")
        #calculo do vértice
        xv = (-b)/(2*a)
        yv = -delta / (4*a)
        print(f'O vertice da equação é xv = {xv} e yv = {yv}')
        yx0 = c
        print(f'A equação intercepta o eixo Y no ponto y = {c}')
        terminar = input("Para terminar digite S ou pressione enter para continuar ")
