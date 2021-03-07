def shift_left(my_list):
    my_list[0], my_list[1] = my_list[1], my_list[0]
    my_list[1], my_list[2] = my_list[2], my_list[1]
    return my_list