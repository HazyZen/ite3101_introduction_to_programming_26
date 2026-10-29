def censor(text, word):
    text_list = text.split(' ')
    new_text_list = list()
    for item in text_list:
        if item == word:
            new_text_list.append(len(item) * '*')
        else:
            new_text_list.append(item)
    print(new_text_list)
    return new_text_list


censor("this hack is wack hack", "hack")
