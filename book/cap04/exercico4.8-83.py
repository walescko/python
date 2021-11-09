#Python - Exercício 4.8, página 83
#Calculadora Simples
print('WADAJU SOFTWARE SOLUTIONS')
print('Calculadora Simples - versão 1.0')
print('Digite dois valores:')
a = float(input('A = '))
b = float(input('B = '))
print('Qual a operação que deseja faze?')
print('Adição .......... 1')
print('Subtração ....... 2')
print('Multiplicação ... 3')
print('Divisão ......... 4')
opcao = 0
resultado = 0
opcao = input('Qual a sua escolha? ')
if opcao == '1':
    resultado = a + b
    print(f"O resultado é {resultado:6.2f}")
elif opcao == '2':
    resultado = a - b
    print(f"O resultado é {resultado:6.2f}")
elif opcao == '3':
    resultado = a * b
    print(f"O resultado é {resultado:6.2f}")
elif opcao == '4' and b != 0:
    resultado = a / b
    print(f"O resultado é {resultado:6.2f}")
elif opcao == '4' and b == 0:
    print("Divisão por zero!")
else:
    print("Opção Inválida.")
