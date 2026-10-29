def censor(text, word):
    new_Text = list()
    for wrd in text:
        if wrd.lower() == word:
            newText.append(len(wrd) * '*')
            print(newText)
        else:
            newText.append(wrd)


print(censor("this hack is wack hack", "hack"))
