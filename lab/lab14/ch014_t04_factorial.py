def factorial(x):
    total = 0
    i = 1
    while i < x:
        total = x * (x - i)
        i += 1