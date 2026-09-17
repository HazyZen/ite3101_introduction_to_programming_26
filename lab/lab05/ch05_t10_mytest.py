pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()  # all lowercase
    first = word[0]  # gets the first letter of the word
    new_word = word + first + pyg
    # slices out the first letter and gives the rest
    new_word = new_word[1:len(new_word)]
    print(new_word)
else:
    print('empty')
