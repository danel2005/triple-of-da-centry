def check_valid_input(letter_guessed, old_letters_guessed):
    return not((len(letter_guessed) > 1) or not (letter_guessed.isalpha()) or (old_letters_guessed.count(letter_guessed.lower()) != 0))