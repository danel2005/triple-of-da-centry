def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if not((len(letter_guessed) > 1) or not (letter_guessed.isalpha()) or (old_letters_guessed.count(letter_guessed.lower()) != 0)):
        old_letters_guessed += [letter_guessed]
        return 1
    print("X")
    old_letters_guessed = sorted(old_letters_guessed, key=str.lower)
    for i in old_letters_guessed[ :-1]:
        print(i,end = " -> ")
    print(old_letters_guessed[-1])
    return 0
