def factorial(x):
    total = 0
    i = 0
    while i < x:
        if total == 0:
            i += 1
            total = x * (x - i)
        else:
            i += 1
            total *= (x - i)

    return print(total)


factorial(3)
