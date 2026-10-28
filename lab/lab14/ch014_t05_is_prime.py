def is_prime(x):
    for n in range(2, x-1):
        return x % n != 0


print(is_prime(11))

