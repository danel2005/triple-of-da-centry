def count_chars(my_str):
    """
    returns a dict that the keys are the letters and the valus are how many of them were in the string
    :param my_str: the string we want to count every letter
    :type my_str: str
    :return: a dict that the keys are the letters and the valus are how many of them were in the string
    :rtype: dict
    """
    dict = {}
    my_list = list(my_str.replace(" ", ""))
    for letter in my_list:
        if letter in dict.keys():
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict
    
def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))

if __name__ == "__main__":
    main()