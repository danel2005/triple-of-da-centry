def is_greater(my_list, n):
    """
    returns all the numbers from the list that are higher from n
    :param my_list: the list of numbers
    :param n: the boundary number
    :type my_list: list
    :type n: int
    :return: list of numbers that are higer then n
    :rtype: list
    """
    nums = []
    for item in my_list:
        if item > n:
            nums += [item]
    return nums
    
def main():
    print(is_greater([1,30,25,60,27,28], 28))
    
if __name__ == "__main__":
    main()