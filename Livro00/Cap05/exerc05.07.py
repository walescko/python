#Escreva uma tabuada onde o usuário pode escolher a número da tabuada e o intervalo.
print("Walescko Loma Linda")
print("Tabuada com escolha de intervalo")

n = int(input("Escolha o número para a tabuada: "))
i = int(input("Qual o inicio do intervalo da tabuada? "))
x = int(input("Qual o final do intervadlo da tabuada? "))

while i <= x:
    print(f" {n} x {i} = {i*n}")
    i = i + 1

print("end program")
