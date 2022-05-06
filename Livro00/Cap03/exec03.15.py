print("Walescko Software")
print("Redução do tempo de vida de um fumante")
timeSmoke = float(input("Quanto tempo de fumente? "))
cigarDays = int(input("Quantos cigarros dia? "))

timeReduction = ((10*cigarDays)/(24*60))*(timeSmoke*365)

print(f"Estimativa de redução de tempo de vida é {timeReduction:.2f} dias")