def anti_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    text_list = list(text)

    for letter in vowels:
        for char in text:
            if letter == char:
                



anti_vowels('hello')
