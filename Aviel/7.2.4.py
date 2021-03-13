def seven_boom(end_number):
    """
    playing the game 7Boom until end_number
    :param end_number: the ending game number
    :type end_number: int 
    :return: list of numbers and "BOOM"s
    :rtype: list
    """
    nums = []
    for num in range(end_number + 1):
        if num % 7 == 0:
            nums += ["BOOM"]
        elif "7" in str(num):
            nums += ["BOOM"]
        else:
            nums += [num]
    return nums
    
def main():
    print(seven_boom(17))
    
if __name__ == "__main__":
    main()