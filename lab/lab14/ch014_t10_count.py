def count(sequence, item):
    num = 0
    for i in sequence:
        if i == item:
            num += 1
        print(i)


count([1, 2, 1, 1], 1)
