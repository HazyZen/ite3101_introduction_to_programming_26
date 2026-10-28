def is_prime(x):
    for n in range(x-1, 1, -1):
        return x % n != 0


print(is_prime(11))
