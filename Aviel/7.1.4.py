def squared_numbers(start, stop):
    """
    returns all the numbers from start to stop squard
    :param start: the first number
    :param stop: the last number
    :type start: int
    :type stop: int 
    :return: all the numbers from start to stop squard
    :rtype: int
    """
    squared_numbers_list = []
    while start <= stop:
        squared_numbers_list += [start ** 2]
        start += 1
    return squared_numbers_list