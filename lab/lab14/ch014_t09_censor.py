def censor(text, word):
    newText = list()
    for wrd in text:
        if wrd.lower() == word:
            print(wrd)
            len(wrd)


censor("this hack is wack hack", "hack")
