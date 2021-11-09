#Python - Canais de comunicação em um projeto de Software
#inspirado no vídeo do Fábio Akita sobre o livro Mythical Man-Month
print('WALESCKO SOFTWARE SOLUTION')
print('Canais de comunicação em projeto de software')
pessoas = int(input("Quantas pessoas tem no projeto? "))
while True:
    if pessoas == 0:
        break
    else:
        channel = (pessoas*(pessoas-1))/2
        print(f"O projeto de software de {pessoas} tem {channel} canais de comunicação")
        pessoas = int(input("Quantas pessoas tem no projeto? "))