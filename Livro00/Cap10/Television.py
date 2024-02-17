class Television:
    def __init__(self, min, max): #método que é chamado quando um objeto televisão é criado.
        self.on = False
        self.chanel = 2
        self.cmin = min
        self.cmax = max
        self.size = 0
        self.brad = ""
    def change_chanel_up(self):
        if self.chanel + 1 <= self.cmax:
            self.chanel += 1
    def change_chanel_down(self):
        if self.chanel - 1 >= self.cmin:
            self.chanel -= 1


tv = Television(1, 99)
print(tv.chanel)
for x in range(0, 120):
    tv.change_chanel_up()

print(tv.chanel)

for x in range(0, 120):
    tv.change_chanel_down()

print(tv.chanel)


#tv.size = 24
#tv.brad = "LG"
#print(tv.on)
#print(tv.chanel)
#print(tv.brad)
#print(tv.size)
#tv.on = True
#tv.change_chanel_up()
#print(tv.chanel)
#tv.change_chanel_down()
# tv.change_chanel_down()
#print(tv.chanel)
#tv_livingRoom = Television()
#tv_livingRoom.on = True
#tv_livingRoom.chanel = 4

# print(tv.chanel)
#print(tv_livingRoom.chanel)
