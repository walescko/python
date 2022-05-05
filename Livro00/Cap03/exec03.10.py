#Exercio 3.10 - Inforar o Salario e o aumento percentual e exibir o o valor do aumento e o salario novo
print("Walescko Software")

salario = float(input("Salario atual: R$ "))
taxaAumento = float(input("Percentual de aumento (%): "))

aumentoSalario = salario * taxaAumento/100
salario = aumentoSalario + salario

print(f"Aumento: R$  {aumentoSalario:.2f}")
print(f"Novo Salario {salario:.2f}")
