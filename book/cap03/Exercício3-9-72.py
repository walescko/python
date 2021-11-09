#Python Exercício 3.9 - página 72
print("WADAJU SOFTWARE SOLUTIONS")
print('Tempo em segundos')
dia = float(input('Dia = '))
hora = float(input("Hora = "))
minuto = float(input("Minutos = "))
segundo = float(input("segundos = "))
#conversão
d1 = dia*24*3600 #Cada hora tem 60 minutos e cada minuto tem 60s 1h = 60min, 1min = 60s
h1 = hora*3600
m1 = minuto*60
total = d1 + h1 + m1 + segundo
print(f"Total em segundo {total} s")
print("fim")
