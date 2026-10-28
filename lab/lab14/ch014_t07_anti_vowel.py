def anti_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for letter in vowels:
        for char in text:
            if letter == char:
                print(char)
                newtext = text.strip(char)
                print(newtext)


print(anti_vowels('hello'))
