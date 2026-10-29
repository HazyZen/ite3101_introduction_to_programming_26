def censor(text, word):
    new_Text = list()
    for wrd in text:
        new_Text.append(wrd)
        # if wrd.lower() == word:
        #     new_Text.append(len(wrd) * '*')
        #     print(new_Text)
        # else:
        #     new_Text.append(wrd)
    return new_text


print(censor("this hack is wack hack", "hack"))
