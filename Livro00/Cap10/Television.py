class Television:
    def __init__(self): #método que é chamado quando um objeto televisão é criado.
        self.on = False
        self.chanel = 2

tv = Television()
print(tv.on)
print(tv.chanel)

tv_livingRoom = Television()
tv_livingRoom.on = True
tv_livingRoom.chanel = 4

print(tv.chanel)
print(tv_livingRoom.chanel)
