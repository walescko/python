T = [-10, -8, 0, 1, 2, 5, -2, -4]
maximum = T[0]
minimum = T[0]
sum01 = 0
i = 0
for e in T:
    if e > maximum:
        maximum = e

for e in T:
    if e < minimum:
        minimum = e

while i < len(T):
    sum01 += T[i]
    i += 1

print(maximum)
print(minimum)
print(sum01)
print(sum01 / len(T))
