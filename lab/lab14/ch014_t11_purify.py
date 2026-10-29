def purify(nums):
    new_list = []
    for i in nums:
        if i % 2 != 0:
            new_list.append(i)
    return new_list


purify([1, 2, 3, 4])
