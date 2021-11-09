#Python - Exercício 4.2, página 77
print('WADAJU SOFTWARE SOLUTIONS')
print('Programa multa por excesso de velocidade')
velocidade = float(input('Qual a velocidade? '))
if velocidade > 80 :
    excesso = velocidade - 80
    multa = (excesso) * 5
    print(f"Você ultrapassou em {excesso:5.2}km/h")
    print(f'Valor da multa a pagar é R$ {multa}.')
if velocidade <= 80:
    print('Você é um bom motorista! Parabéns!')
print('Fim')