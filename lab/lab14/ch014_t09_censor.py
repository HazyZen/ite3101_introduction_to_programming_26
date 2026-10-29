def censor(text, word):
    text_list = text.split(' ')
    for item in text_list:
        if item == word:
            item = len(item) * '*'
            print(text)


censor("this hack is wack hack", "hack")
