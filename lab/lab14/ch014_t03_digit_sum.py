def digit_sum(n):
    to_str = str(n).split()
    total = 0
    for num in to_str:
        total += int(num)
    return total


digit_sum(1234)
