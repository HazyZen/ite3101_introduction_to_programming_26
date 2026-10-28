def digit_sum(n):
    to_str = str(n)
    total = 0
    for num in to_str:
        total += int(num)
    return total
