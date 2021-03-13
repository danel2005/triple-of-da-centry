def extend_list_x(list_x, list_y):
    """
    list_y = map(str, list_y)
    list_y = list(list_y)
    list_y = ", ".join(list_y)
    """
    for i in range(len(list_y)):
        list_i = list_y[i]
        list_x.insert(i, list_i)

    return list_x
print(extend_list_x(['list', 'string', 'int'],[1, 2, 3]))