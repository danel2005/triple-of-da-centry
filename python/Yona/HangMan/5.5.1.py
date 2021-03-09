def is_valid_input(letter_guessed):

    if((len(letter_guessed) > 1) or not letter_guessed.isalpha()):
        return 0

    else:
        return 1