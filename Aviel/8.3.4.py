def inverse_dict(my_dict):
    """
    inversing a dict
    :param my_dict: the dict we want to inverse
    :type my_dict: dict
    :return: an inversed dict
    :rtype: dict
    """
    new_dict = {}
    for info in my_dict.items():
        if info[1] in new_dict.keys():
            new_dict[info[1]] += [info[0]]
        else:
            new_dict[info[1]] = [info[0]]
    for value in new_dict.values():
        value.sort()
    return new_dict
    
def main():
    course_dict = {'I' : 3, 'love' : 3, 'self.py!' : 2}
    print(inverse_dict(course_dict))
    
if __name__ == "__main__":
    main()