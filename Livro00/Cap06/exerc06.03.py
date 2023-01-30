List01 = [1, 2, 3]
List02 = [2, 3, 4]

List03 = []
List04 = List01[:]
List04.extend(List02)

i = 0
while i < len(List04):
    j = 0
    while j < len(List03):
        if List04[i] == List03[j]:
            break
        j += 1
    if j == len(List03):
        List03.append(List04[i])
    i += 1
i = 0

print(f"Lista 01: {List01}")
print(f"Lista 02: {List02}")
print(f"Lista Resultante: {List03}")
