# verificação do tipo de conteúdo
s = "125"
p = "hello world"
print(s.isalnum)
print(p.isalnum)
print(s.isalpha)
print(p.isalpha)

print("777".isdigit())
print("10.4".isdigit())
print("+10".isdigit())
print("-5".isdigit())

terco = "\u2153"
tibetNine = "\u0f29"
print(terco)
print(tibetNine)
print(terco.isdigit())
print(terco.isnumeric())
print(tibetNine.isnumeric())
print(tibetNine.isdigit())
print(tibetNine.isnumeric())


