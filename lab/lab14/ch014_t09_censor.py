def censor(text, word):
    newText = list()
    for wrd in text:
        if wrd.lower() == word:
            newText.append(len(wrd) * '*')
            print(newText)


censor("this hack is wack hack", "hack")
