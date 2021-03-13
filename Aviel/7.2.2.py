def numbers_letters_count(my_str):
    """
    returns a list that the first number is the numbers count and the second number is the letters count
    :param my_str: the string we want to check
    :type my_str: str
    :return: list that the first number is the numbers count and the second number is the letters count
    :rtype: list
    """
    count_letters = 0
    count_nums = 0
    for letter in my_str:
        if letter >= "0" and letter <= "9":
            count_nums += 1
        else:
            count_letters += 1
    return [count_nums, count_letters]
    
def main():
    print(numbers_letters_count("Python 3.6.3"))
    
if __name__ == "__main__":
    main()