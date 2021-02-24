import random
import termcolor
import colorama
from colorama import Fore, Back, Style

HANGMAN_ASCII_ART = ("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
""")
MAX_TRIES = 6

print(HANGMAN_ASCII_ART)
print(random.randint(1, MAX_TRIES))

print("""\npicture 1:
    x-------x""")

print("""picture 2:
    x-------x
    |
    |
    |
    |
    |""")
print("""picture 3:
    x-------x
    |       |
    |       0
    |
    |
    |""")
print("""picture 4:
    x-------x
    |       |
    |       0
    |       |
    |
    |""")

print("""picture 5:
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""")

print("""picture 6:
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""")
    
print("""picture 7:
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |\n""")
    
digit_one, digit_two, digit_three = input("Enter three digits: ")
sum = int(digit_one) + int(digit_two) + int(digit_three)
print(sum)
print(sum // 3)
print(sum % 3)
print(sum % 3 == 0)

guessed_letter = input("Enter a letter: ")
print(guessed_letter)

print(""""Shuffle, Shuffle, Shuffle", say it together!\nChange colors and directions,\nDon't back down and stop the player!\n\tDo you want to play Taki?\n\tPress y\\n""")
# s y z y g y

encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
print(encrypted_message[-1::-2])

# There is an 'e'
# Not only spaces
# Two 'p''s
# s p a c e s h i p

string = input("Please enter a string: ")
replace("e", string[0])