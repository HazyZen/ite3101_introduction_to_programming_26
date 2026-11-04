def remove_duplicates(x: list):
    new_list = []
    for i in x:
        if not new_list:
            print('empty')
            new_list.append(i)
        
    # for n in new_list:
    #     # if list doesn't have it, append it
    #     elif n != i:
    #         new_list.append(i)
    return new_list


print(remove_duplicates([1, 1, 2, 2]))
