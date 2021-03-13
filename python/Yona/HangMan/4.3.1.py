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
print(UNDERLINE_STRING[ : len(user_word) * 2 - 1])

first_guess = input("Guess a letter: ")
first_guess = first_guess.lower()

if((len(first_guess) > 1) and not first_guess.isalpha()):
    print("E3")

elif(len(first_guess) > 1):
    print("E1")

elif(first_guess > "z") or (first_guess < "a"):
    print("E2")

else:
    print(first_guess)

