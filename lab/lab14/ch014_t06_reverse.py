def reverse(text):
    text_list = list(text)
    reversed_text_list = []
    for i in range(len(text_list) - 1, -1, -1):
        reversed_text_list.append(text_list[i])
    print(str(reversed_text_list)


reverse('abcd')
