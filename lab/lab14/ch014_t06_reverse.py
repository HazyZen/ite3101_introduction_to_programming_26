def reverse(text):
    text_list = list(text)
    reversed_text_list = []
    for i in range(len(text_list) - 1, -1, -1):
        reversed_text_list.append(text_list[i])
    reversed_text = ''.join(reversed_text_list)
    return reversed_text
