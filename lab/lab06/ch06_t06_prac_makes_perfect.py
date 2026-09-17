def cube(number):
    return print(number ** number)


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


cube(10)
