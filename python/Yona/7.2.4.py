def seven_boom(end_number):
    num = 0
    list = []
    for num in range(end_number + 1):
        boom_bool = 0
        for c in range(num):
            if(c == 7):
                boom_bool = 1
        if(boom_bool == 1):
            list.append('BOOM')
        elif(num % 7 == 0):
            list.append('BOOM')
        else:
            list.append(num)
        num += 1
    return list