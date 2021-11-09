#Python - Exercício 4.4 - página 79
#Programa aumento de salário
print('WADAJU SOFTWARE SOLUTIONS')
print('Aumento de Salário')
salario = float(input('Qual o salario? '))
base = salario
if base > 1250:
    new_salario = 1.1*base
if base <= 1250:
    new_salario = 1.15*base
print(f'Seu salário atual é R${salario:5.2f}')
print(f'Ele passará a ser de R$ {new_salario:5.2f}')
aumento = new_salario - salario
print(f'Você ganhou um aumento de R$ {aumento:5.2f}')
print('Fim')