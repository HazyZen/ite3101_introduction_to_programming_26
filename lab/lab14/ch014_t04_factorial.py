def factorial(x):
    total = x
    i = 1
    while i < x:
        if total == 0:
            total = x * (x - i)
            i += 1
        else:
            total *= (x - i)
            i += 1

    return print(total)


factorial(3)

for n in range(5, 0, -1):
    print(n)
