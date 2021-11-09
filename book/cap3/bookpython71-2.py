#Exemplo pág 71 - Python
#Entrada de dados e conversão de dados.
#Por padrão a linguagem Python trata todas as
#variáveis como strings.

#Programa Calculo de Bônus por Tempo de Serviço.
print("Bônus por tempo de serviço")
ano = int(input("Quantos anos de serviço? "))
valor_por_ano = float(input("Valor por ano: "))
bonus = ano * valor_por_ano
print(f"Bônus de R$ {bonus:5.2f}")
