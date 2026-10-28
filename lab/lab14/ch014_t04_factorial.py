def factorial(x):
    total = x
    for num in range(x-1, 0, -1):
        total *= num

    return print(total)


factorial(3)

for n in range(5-1, 0, -1):
    print(n)
