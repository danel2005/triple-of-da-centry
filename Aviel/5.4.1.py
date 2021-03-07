def func(num1, num2):
    """ The function adds up num1 and num2 and returning the value of it
    :param num1: the first number we want to add
    :param num2: the second number we want to add
    :type num1: integer
    :type num2: integer
    :return: the added value of the two numbers
    :rtype: integer"""
    return num1 + num2
    
def main():
    num = func(1,2)
    print(num)
    help(func)
    
if __name__ == "__main__":
    main()