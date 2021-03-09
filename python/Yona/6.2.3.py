def format_list(my_list):
    """
    the function gets list and prints any sec str
    :param my_list: a zugi list
    :type my_list: list
    :return: any sec str
    :rtype: list
    """
    
    new_list = my_list[2: -1]
    new_list = new_list[: : 2]
    new_list = [my_list[0]] + new_list
    new_list = new_list + ["and " + my_list[-1]]
    
    string = ', '.join(new_list)
    print(string)
format_list(['hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'magnesium'])