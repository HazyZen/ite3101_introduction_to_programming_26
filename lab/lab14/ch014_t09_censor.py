def censor(text, word):
    text_list = text.split(' ')
    for item in text_list:
        if item == word:
            print(len(item) * '*')


censor("this hack is wack hack", "hack")
