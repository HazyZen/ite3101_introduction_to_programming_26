def anti_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    newtext = ''

    for char in text:
        if char not in vowels:
            newtext += char

    print(newtext)
    return newtext


print(anti_vowels('hello'))
