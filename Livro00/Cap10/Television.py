class Television:
    def __init__(self): #método que é chamado quando um objeto televisão é criado.
        self.on = False
        self.chanel = 2
        self.size = 0
        self.brad = ""
    def change_chanel_up(self):
        self.chanel += 1
    def change_chanel_down(self):
        self.chanel -= 1

tv = Television()
tv.size = 24
tv.brad = "LG"
print(tv.on)
print(tv.chanel)
print(tv.brad)
print(tv.size)
tv.on = True
tv.change_chanel_up()
print(tv.chanel)
tv.change_chanel_down()
# tv.change_chanel_down()
print(tv.chanel)
tv_livingRoom = Television()
tv_livingRoom.on = True
tv_livingRoom.chanel = 4

# print(tv.chanel)
print(tv_livingRoom.chanel)
