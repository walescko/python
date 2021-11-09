# Python - Exercício 4.9 - página 80
#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
#O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de ano para pagar.
#O valor da prestação mensal não pode ser superior a 30% do salário.
#Calcule o valor da prestação como sendo o valor da casa a comprar dividio pelo número de meses a pagar
print("WADAJU SOFTWARE SOLUTIONS")
print("O sonho da casa própria - Simulação de empréstimo")
casa = float(input("Valor do imóvel: "))
salario = float(input("Salário bruto: "))
anosp = float(input("Prazo para pagamento, em anos: "))
#contas para função if else
prestacaoideal = 0.3*salario
mensal = anosp*12
prestacaopretendida = casa / (mensal)
prazosalario = casa/prestacaoideal
if prestacaopretendida > prestacaoideal:
    print(f'Não é possível financiar o imóvel de R$ {casa:8.2f} no prazo de {anosp} anos.')
else:
    print('O financiamento é autorizado')
    print(f'Valor máximo da prestação R$ {prestacaoideal:6.2f}')
    print(f'O valor do imóvel R$ {casa:8.2f} com o prazo de {anosp} anos.')
    print(f'Terá prestação R$ {prestacaopretendida:6.2f} levando um prazo de {mensal:6.2f} meses')
