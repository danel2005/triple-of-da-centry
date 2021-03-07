def format_list(my_list):
    my_list = my_list[::2] + ["and " + my_list[-1]]
    my_str = ', '.join(my_list)
    return my_str