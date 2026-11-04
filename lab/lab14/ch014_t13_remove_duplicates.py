def remove_duplicates(x: list):
    new_list = []
    for i in x:
        print(i)
        for n in new_list:
            if not new_list:
                print(empty)
            # if list doesn't have it, append it
            elif n != i:
                new_list.append(i)
    return new_list


print(remove_duplicates([1, 1, 2, 2]))
