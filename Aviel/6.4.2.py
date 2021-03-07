def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Adds the letter guessed to the array of letters that has already been guessed
    :param letter_guessed: the guess that the user inputing
    :param old_letters_guessed: all the letters the user already guessed
    :type letter_guessed: string
    :type old_letters_guessed: array
    :return: true or false, the letter is valid or not and if its already been guessed
    :rtype: bool
    """
    if len(letter_guessed) >= 2 or not (letter_guessed >= "a" and letter_guessed <= "z" or letter_guessed >= "A" and letter_guessed <= "Z") or (letter_guessed.lower() in old_letters_guessed):
        old_letters_guessed_str = ' -> '.join(sorted(old_letters_guessed))
        print("X")
        print(old_letters_guessed_str)
        return False
    old_letters_guessed += letter_guessed
    return True