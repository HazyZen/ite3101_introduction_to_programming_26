def median(x: list) -> int:
    sort_list = x.sort()
    if len(sort_list) % 2 == 0:
        sort_list[len(sort_list) / 2] + sort_list[len(sort_list) / 2 - 1]


print(median([1, 1, 2]))


# Odd
# 3 / 2 = floor = 1 (0, 1, 2)
# 9 / 2 = floor = 4 (0-3, 4, 5-8)

#Even
# [1, 2, 3, 4] = len is 4 = 4 / 2 = 2 + (2-1) 