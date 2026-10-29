def censor(text, word):
    newText = list()
    for wrd in text:
        if wrd.lower() == word:
