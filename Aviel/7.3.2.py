def check_win(secret_word, old_letters_guessesd):
    """
    Checks if the player wins
    :param secret_word: the word the player need to guess
    :param old_letters_guessesd: the letters that the player is already guessed
    :type secret_word: str
    :type old_letters_guessesd: list
    :return: of the player finished the game or not
    :rtype: bool
    """
    win_game = True
    for letter in secret_word:
        if letter not in old_letters_guessesd:
            win_game = False
            break
    return win_game
    
    
def main():
    secret_word = "friends"
    old_letters_guessesd = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessesd))
    
if __name__ == "__main__":
    main()