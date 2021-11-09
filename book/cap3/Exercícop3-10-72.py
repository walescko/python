#Python - Exercício 3.10 - página 72
print('WADAJU SOFTWARE SOLUTIONS')
print('Aumento de Salário')
salario = float(input('Qual o salario? '))
aumento = float(input('Qual o percentual de aumento? '))
salarion = (1+ (aumento/100))*salario
variacao = salarion - salario
print(f"Salário atual é de R$ {salario}, com o aunento de {aumento}% o novo salario será de R$ {salarion}.")
print(f"O aumento foi de R$ {variacao}")
print("Fim")