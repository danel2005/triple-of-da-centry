def numbers_letters_count(my_str):
    letters = 0
    numbers = 0
    list = []
    for i in my_str:
        if((i >= '0') and (i <= '9')):
            numbers += 1
    list.append(numbers)
    letters = len(my_str)
    letters = letters - numbers
    list.append(letters)
    return list