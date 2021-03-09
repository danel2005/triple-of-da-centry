HANGMAN_ASCII_ART = ("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")
import random
MAX_TRIES = random.randint(5,10)
print(HANGMAN_ASCII_ART,"\n", MAX_TRIES)

UNDERLINE_STRING = "_ _ _ _ _ _ _ _ _ _"
user_word = input("Please enter a word: ")
print(UNDERLINE_STRING[ : len(UNDERLINE_STRING) * 2 - 1])

first_guess = input("Guess a letter: ")
print(first_guess.lower())