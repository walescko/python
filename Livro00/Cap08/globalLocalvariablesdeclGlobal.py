a = 5
def changePrint():
    global a
    a = 7
    print(f"A dentro da função :{a}")

print(f"Antes de mudar: {a}")
changePrint()
print(f"Depois de mudar{a}")
