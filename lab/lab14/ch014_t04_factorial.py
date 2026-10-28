def factorial(x):
    total = 0
    i = 1
    while i < x:
        if total == 0:
            total = x * (x - i)
            i += 1
            print(total)
        else:
            total *= (x - i)
            i += 1
            total
    return total


factorial(4)
