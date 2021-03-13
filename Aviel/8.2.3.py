def mult_tuple(tuple1, tuple2):
    """
    Returns all of the combinations of the numbers in the tuples given to the func
    :param tuple1: tuple of numbers
    :param tuple2: tuple of numbers
    :type tuple1, tuple 2: tuple
    :return: all of the combinations of the numbers inside the tuples
    :rtype: tuple of tuples
    """
    list_of_tuples = []
    for number in tuple1:
        for number2 in tuple2:
            list_of_tuples += (number,number2) , (number2,number)
    return tuple(list_of_tuples)
    
def main():
    first_tuple = (1,2)
    second_tuple  = (4,5)
    print(mult_tuple(first_tuple, second_tuple))
    
if __name__ == "__main__":
    main()