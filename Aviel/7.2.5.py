def sequence_del(my_str):
    """
    returning a string without duplicates
    :param my_str: the string we want to delete duplicates
    :type my_str: str 
    :return: new string without duplicates
    :rtype: str
    """
    next = ""
    new_str = ""
    for index, letter in enumerate(my_str):
        if index + 1 < len(my_str):
            next = my_str[index + 1]
        else:
            new_str += letter
        if not (letter == next):
            new_str += letter
    return new_str

def main():
    print(sequence_del("pppppyyyyyttttthhhhhoooonnnnnnnn"))
    
if __name__ == "__main__":
    main()