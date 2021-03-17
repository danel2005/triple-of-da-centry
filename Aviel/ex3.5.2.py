word = input("Please enter a word: ")
word_len = len(word)
new_word = (("_" * word_len).replace(""," ")[1:-1])
print(new_word)