def censor(text, word):
    text_list = text.split(' ')
    new_text_list = list()
    for item in text_list:
        if item == word:
            new_text_list.append(len(item) * '*')
        else:
            new_text_list.append(item)
    print(' '.join(new_text_list))
    return ' '.join(new_text_list)


censor("abc a a  b", "a")
