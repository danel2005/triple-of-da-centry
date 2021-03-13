def shift_left(my_list):
    """
    Moving the array one step to the left
    :param my_list: the array we want to move to the left
    :type my_list: array
    :return: returns the new array
    :rtype: array
    """
    my_list[0], my_list[1] = my_list[1], my_list[0]
    my_list[1], my_list[2] = my_list[2], my_list[1]
    return my_list