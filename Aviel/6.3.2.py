def longest(my_list):
    my_list = sorted(my_list, key=len)
    return my_list[-1]