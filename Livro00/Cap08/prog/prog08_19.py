import prog08_18
#from prog08_18 import intValue
L=[]
for x in range(10): #Número de solicitações de entrada
    L.append(prog08_18.intValue("Digite um número: ", 0, 20))
    #L.append(intValue("Digite um número: ", 0, 20))
print(f"Soma: {sum(L)}")
#uma boa pratica é usar o 'import' com o nome do módulo apenas, assim as chamadas ficam com o nome do módulo + função/método