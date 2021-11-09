#Python - Exercício 5.13 - página 90
#Escreva um programa que pergunte o valor inicial de uma dívida e
#o juro mensal. Pergunte também o valor mensal que será pago.
#Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros.
print('WADAJU SOFTWARE SOLUTIONS')
print('Pagamento de Dívida')
divida = float(input('Qual o valor da dívida/empréstimo? '))
juros = float(input('Qual a taxa do juro mensal? '))
parcela = float(input('Qual o valor desejado da parcela? '))
prazo = divida // parcela
dividatotal = divida*(1+juros/100)**prazo
i = 0
pagamento = 0
jurospagos = 0
parcelapagar = dividatotal/prazo
print(f'A sua dívida será paga em {prazo} meses')
while i <= prazo:
    print(f'Mês {i}')
    print(f'A divida é de R$ {dividatotal:6.2f}')
    print(f'Total pago é R$ {pagamento:6.2f}')
    print(f'Falta pagar R$ {dividatotal:6.2f}')
    pagamento = pagamento + parcelapagar
    dividatotal = dividatotal - parcelapagar
    i = i + 1





