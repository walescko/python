s = "um tigre, dois tigres, três tigres"
print(s.split(","))
print(s.split(" "))
print(s.split())

m = "uma linha\noutra linha \ne mais uma\n"
print(m)
print(m.splitlines())

print(s.replace("tigre", "gato"))
print(s.replace("tigre", "gato", 1))
print(s.replace("tigre", "gato", 2))
print(s.replace("tigre", ""))


