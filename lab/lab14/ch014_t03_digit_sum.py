def digit_sum(n):
    to_str = str(n)
    total = 0
    for num in to_str:
        print(num)
        total += int(num)
    print(total)


digit_sum(1234)
