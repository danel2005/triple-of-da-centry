def choose_word(file_path, index):
    """
    Choosing the word that the player will need to guess
    :param file_path: the path to the file of the words
    :param index: the number that represent the place of the word in the file, index starts from 1 not 0
    :type file_path: str
    :type index: int
    :return: the number of different words in the file, the word that in place index that will be used as the word that the user need to guess
    :rtype: tuple
    """
    with open(file_path, "r") as file_input:
        file_content = file_input.read()
    file_content.replace("\n", " ")
    words = file_content.split()
    guess_word = words[index % len(words) - 1]
    count_words = len(list(dict.fromkeys(words)))
    
    return (count_words, guess_word)
    
def main():
    print(choose_word(r"e:\words.txt", 3))
    
if __name__ == "__main__":
    main()