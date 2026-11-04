def median(x: list) -> int:
    sortlist = x.sort()
    print(len(x))


print(median([1, 1, 2]))


# Odd
# 3 / 2 = floor = 1 (0, 1, 2)
# 9 / 2 = floor = 4 (0-3, 4, 5-8)

#Even
# [1, 2, 3, 4] = len is 4 = 4 / 2 = 2 + (2-1) =