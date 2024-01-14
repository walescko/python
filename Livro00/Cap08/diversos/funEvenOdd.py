def even(x):
    return x%2 == 0
print(even(2))
print(even(5))
print(even(10))

def evenOdd(x):
    if even(x):
        return "par"
    else:
        return "ímpar"

print(evenOdd(4))
print(evenOdd(5))
