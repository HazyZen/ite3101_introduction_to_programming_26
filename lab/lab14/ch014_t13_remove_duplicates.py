def remove_duplicates(x: list):
    new_list = []
    for i in x:
        print(i)
        for n in new_list:
            # if list doesn't have it, append it
            new_list.append(i)
            return print(i)


print(remove_duplicates([1, 1, 2, 2]))
