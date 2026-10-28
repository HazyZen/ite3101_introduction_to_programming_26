def is_prime(x):
    for n in range(2, x-1):
        if x % n == 0:
            return False


print(is_prime(11))

