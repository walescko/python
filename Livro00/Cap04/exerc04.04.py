print("Walescko Software")
print("Ajuste salarial")

salarioAtual = float(input("Entre com o valor do salario: R$ "))
aumentoSalario = 0

if (salarioAtual < 1250):
    aumentoSalario = (salarioAtual * 0.15)

if (salarioAtual >= 1250):
    aumentoSalario = (salarioAtual * 0.1)

print(f"Para o salario de R$ {salarioAtual} o aumento sera de R$ {aumentoSalario}.")