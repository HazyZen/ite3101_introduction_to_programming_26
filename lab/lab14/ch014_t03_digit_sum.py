def digit_sum(n):
    to_str = str(n).split()
    total = 0
    for str in to_str:
        total += int(str)
    return total


digit_sum(1234)
