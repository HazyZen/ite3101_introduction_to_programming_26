pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print(original)
    word = original.lowercase()
else:
    print('empty')
