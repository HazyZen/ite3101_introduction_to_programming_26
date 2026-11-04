import math


def median(x: list) -> int:
    x.sort() = x.sort()
    if len(x.sort()) % 2 == 0:
        return (x.sort()[len(x.sort()) / 2] + x.sort()[len(x.sort()) / 2 - 1]) / 2
    else:
        return x.sort()[math.floor((len(x.sort()) / 2))]


median([1, 1, 2])


# Odd
# 3 / 2 = floor = 1 (0, 1, 2)
# 9 / 2 = floor = 4 (0-3, 4, 5-8)

# Even
# [1, 2, 3, 4] = len is 4 = 4 / 2 = 2 + (2-1)
