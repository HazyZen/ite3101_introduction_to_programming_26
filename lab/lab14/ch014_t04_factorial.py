def factorial(x):
    total = x
    for num in range(x-1, 0, -1):
        total *= num
    return print(total)


factorial(1)
