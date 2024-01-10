#import prog18
from prog18 import intValue
L=[]
for x in range(10): #Número de solicitações de entrada
    #L.append(prog18.intValue("Digite um número: ", 0, 20))
    L.append(intValue("Digite um número: ", 0, 20))
print(f"Soma: {sum(L)}")
