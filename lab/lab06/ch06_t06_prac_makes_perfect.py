def cube(number):
    return number ** number


def by_three(number):
    if number % 3:
        return cube(number)
    else:
        return False
