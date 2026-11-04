def remove_duplicates(x: list):
    new_list = []
    for i in x:
        if i not in new_list:
            new_append(i)
    return new_list


print(remove_duplicates([1, 1, 2, 2]))
