def last_early(my_str):
    my_str = my_str.lower()
    return my_str[-1] in my_str[0:-1]
    
string = input("Enter a string: ")
print(last_early(string))
