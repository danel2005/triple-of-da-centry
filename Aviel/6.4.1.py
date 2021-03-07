def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the guess is valid or not
    :param letter_guessed: the guess that the user inputing
    :param old_letters_guessed: all the letters the user already guessed
    :type letter_guessed: string
    :type old_letters_guessed: array
    :return: true or false, the letter is valid or not and if its already been guessed
    :rtype: bool
    """
    if len(letter_guessed) >= 2 or not (letter_guessed >= "a" and letter_guessed <= "z" or letter_guessed >= "A" and letter_guessed <= "Z") or (letter_guessed.lower() in old_letters_guessed):
        return False
    return True