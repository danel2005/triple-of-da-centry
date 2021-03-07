def is_valid_input(letter_guessed):
    """
    Checks if the guess is valid or not
    :param letter_guessed: the guess that the user inputing
    :type letter_guessed: string
    :return: true or false, the letter is valid or not
    :rtype: bool
    """
    if len(letter_guessed) >= 2 or not (letter_guessed >= "a" and letter_guessed <= "z" or letter_guessed >= "A" and letter_guessed <= "Z"):
        return False
    return True
