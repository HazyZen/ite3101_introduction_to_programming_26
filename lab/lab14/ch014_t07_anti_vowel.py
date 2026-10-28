def anti_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    text = text

    for letter in vowels:
        for char in text:
            if letter == char:
                print(char)
                text = text.strip(char)
    print(text)


print(anti_vowels('hello'))
