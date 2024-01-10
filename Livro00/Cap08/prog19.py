import prog18
L=[]
for x in range(10): #Número de solicitações de entrada
    L.append(prog18.intValue("Digite um número: ", 0, 20))
print(f"Soma: {sum(L)}")
