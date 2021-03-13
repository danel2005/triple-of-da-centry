def show_hidden_word(secret_word, old_letters_guessesd):
    """
    Show the player his prograssion in the game
    :param secret_word: the word the player need to guess
    :param old_letters_guessesd: the letters that the player is already guessed
    :type secret_word: str
    :type old_letters_guessesd: list
    :return: string of the secret word but only with the letters that was already guessed
    :rtype: str
    """
    str = ""
    for letter in secret_word:
        if letter in old_letters_guessesd:
            str += letter + " "
        else:
            str += "_ "
    return str[:-1]
    
def main():
    secret_word = "mammals"
    old_letters_guessesd = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessesd))
    
if __name__ == "__main__":
    main()