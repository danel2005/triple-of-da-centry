def check_win(secret_word, old_letters_guessesd):
    """
    Checks if the player wins
    :param secret_word: the word the player need to guess
    :param old_letters_guessesd: the letters that the player is already guessed
    :type secret_word: str
    :type old_letters_guessesd: list
    :return: if the player won the game or not
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessesd:
            return False
    return True
    
def show_hidden_word(secret_word, old_letters_guessesd):
    """
    Show the player his prograssion in the game, for example my name:(a v _ _ l)
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

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the guess is valid or not (valid guess is a single letter, that was not guessed already)
    :param letter_guessed: the guess that the user inputing
    :param old_letters_guessed: all the letters the user already guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: true or false, the letter is valid or not 
    :rtype: bool
    """
    if len(letter_guessed) >= 2 or not (letter_guessed >= "a" and letter_guessed <= "z" or letter_guessed >= "A" and letter_guessed <= "Z") or (letter_guessed.lower() in old_letters_guessed):
        return False
    return True
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Adds the letter guessed to the array of letters that has already been guessed
    :param letter_guessed: the guess that the user inputing
    :param old_letters_guessed: all the letters the user already guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: true or false, the letter is valid or not 
    :rtype: bool
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed_str = ' -> '.join(sorted(old_letters_guessed))
        print("X")
        if not len(old_letters_guessed) == 0:
            print(old_letters_guessed_str)
        return False
    old_letters_guessed += letter_guessed.lower()
    return True
    
def choose_word():
    """
    Choosing the word that the player will need to guess
    :return: the word that in place index that will be used as the word that the user need to guess
    :rtype: str
    """
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    with open(file_path, "r") as file_input:
        file_content = file_input.read()
    file_content.replace("\n", " ")
    words = file_content.split()
    guess_word = words[index % len(words) - 1]
    return guess_word

def print_hangman(num_of_tries):
    """
    Printing the hangman photo
    :param num_of_tries: the number of failed tries the user used
    :type num_of_tries: int
    """
    HANGMAN_PHOTOS = {
    1: 
    """
    x-------x
    """, 
    2:
    """
    x-------x
    |
    |
    |
    |
    |
    """,

    3:
    """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,

    4:
    """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    
    5:
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    6:
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7:
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """}
    print(HANGMAN_PHOTOS[num_of_tries])

def print_welcome():
    """
    Printing the welcome message at the beginning of the game
    """
    print("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
""")
    print("6\n")

def check_right_letter(secret_word, letter):
    """
    Checks if the letter in secret_word
    :param secret_word: the word the user tries to guess
    :param letter: the letter that the user guessed
    :type secret_word: str
    :type letter: str
    :return: true or false, if the letter is one of the letters in the secret word
    :rtype: bool
    """
    if letter in secret_word:
        return True
    return False
    
def print_wrong(num_of_tries):
    """
    Printing if the letter is not included in the secret word
    :param num_of_tries: the number of failed tries the user used
    :type num_of_tries: int
    """
    print(":(")
    print_hangman(num_of_tries + 1)
    
def print_end(is_won):
    """
    Printing the end of the game
    :param is_won: if the player guessed the word or not
    :type is_won: bool
    """
    if is_won:
        print("WIN")
    else:
        print("LOSE")
    
def game(secret_word, old_letters_guessed, num_of_tries, MAX_TRIES):
    """
    The Guessing game, asks the user for inputs and proceeding the game
    :param secret_word: the word that the user need to guess
    :param old_letters_guessed: list of letters that the user already guessed
    :param num_of_tries: number of failed tries of the user
    :param MAX_TRIES: the max number of failed tries (6)
    :type secret_word: str
    :type old_letters_guessed: list
    :type num_of_tries: int
    :type MAX_TRIES: int
    :return: true or false, the user wins the game or looses the game
    :rtype: bool
    """
    while not check_win(secret_word, old_letters_guessed):
        letter = input("Guess a letter: ")
        if (try_update_letter_guessed(letter, old_letters_guessed)):
            if not check_right_letter(secret_word, letter.lower()):
                num_of_tries += 1
                print_wrong(num_of_tries)
            print(show_hidden_word(secret_word, old_letters_guessed))
            if (num_of_tries == MAX_TRIES):
                return False
    return True
    
def main():
    MAX_TRIES = 6 # max number of fails
    secret_word = "" # the word the player need to guess
    old_letters_guessed = [] # the letters that the player is already guessed
    num_of_tries = 0 # num of fails the player already did
    
    print_welcome()
    secret_word = choose_word()
    print("\nLet's start!")
    print_hangman(num_of_tries + 1)
    print(show_hidden_word(secret_word, old_letters_guessed),"\n")
    print_end(game(secret_word, old_letters_guessed, num_of_tries, MAX_TRIES))
        
    
    
if __name__ == "__main__":
    main()