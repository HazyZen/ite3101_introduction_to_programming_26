def factorial(x):
    if x == 0:
        return 1
    total = x
    for num in range(x-1, 0, -1):
        total *= num
    return total
