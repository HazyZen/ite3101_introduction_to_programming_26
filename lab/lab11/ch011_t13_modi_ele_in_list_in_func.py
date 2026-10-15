n = [3, 5, 7]

# Don't forget to return your new list!
for i in range(0, len(x)):
    x[i] = x[i] * 2


def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x


print(double_list(n))
