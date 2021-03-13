def arrow(my_char, max_length):
    """
    Printing an arrow
    :param my_char: the char of the arrow
    :param max_length: the length of the arrow
    :type my_char: char
    :type max_length: int
    :return: string of the arrow
    :rtype: string
    """
    str = ""
    for i in range(1,max_length * 2):
        if i <= 5:
            str += (my_char) * i
        else:
            str += (my_char) * (max_length * 2 - i)
        if i + 1 < max_length * 2:
            str += "\n"
    return str
    
def main():
    print(arrow("*", 5))
    
if __name__ == "__main__":
    main()  