# Programa 6.12 - Controle da utilizaçõa de salas de um cinema
vacantSeats = [10, 2, 1, 3, 0]
while True:
    room = int(input("Sala (0 sai): "))
    if room == 0:
        print('Fim')
        break
    if room > len(vacantSeats) or room < 1:
        print('Sala inexistente')
    elif vacantSeats[room-1] == 0:
        print('Sala Lotada, desculpe!')
    else:
        seat = int(input(f"Quantos lugares você deseja ({vacantSeats[room-1]} vagos): "))
        if seat > vacantSeats[room-1]:
            print('Este número de lugares não está disponível.')
        elif seat < 0:
            print('Número inválido')
        else:
            vacantSeats[room-1] -= seat
            print(f"{seat} lugares vendidos")
print('Utilização das salas')
for x, l in enumerate(vacantSeats):
    print(f"Sala {x + 1} - {l} lugar(es) vazio(s)")
