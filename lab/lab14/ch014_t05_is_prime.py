def is_prime(x):
    # is divisible by iself and 1
    for n in range(x-1, 1, -1):
        return x % n == 0

is_prime(11)