def anti_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    text_list = list(text)

    for letter in vowels:
        for char in text_list:
            if letter == char:
                print(char)
                text_list.remove(char)
    print(text_list)


print(anti_vowels('hello'))
