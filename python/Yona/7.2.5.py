def sequence_del(my_str):
    list = ''
    for i in range(len(my_str)):
        if(my_str[i] != my_str[i + 1]):
            list += my_str[i]
        i += 1
    if(my_str[-1] != list[-1]):
        list += my_str[-1]
    return list
print(sequence_del('pyyyyyyttthhhooonnnn'))