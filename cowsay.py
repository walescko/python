text = input("Qual a mensagem da vaca? ")
comp = len(text)
n = 0
underline = ""
tracked = ""
while n < comp + 4:
    underline += "_"
    tracked += "-"
    n += 1

print(underline)
print("< " + text + " >")
print(tracked)
print("     \   ^__^")
print("      \  (oo)\_______")
print("         (__)\       )\/\ ")
print("             ||----w | ")
print("             ||     || ")