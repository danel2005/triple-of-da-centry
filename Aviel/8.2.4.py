def sort_anagrams(list_of_strings):
    """
    Returns a list of lists, in every list there will be all the anagrams of one word
    :param list_of_strings: list of words without spaces
    :param type: list
    :return: a list of lists, in every list there will be all the anagrams of one word
    :rtype: list
    """
    list_of_anagrams = []
    index = -1
    for string in list_of_strings:
        if not any(string in sublist for sublist in list_of_anagrams):
            list_of_anagrams += [[string]]
            index += 1
            for i in range(list_of_strings.index(string) + 1, len(list_of_strings)):
                if sorted(list(string)) == sorted(list(list_of_strings[i])):
                    list_of_anagrams[index] += [list_of_strings[i]]
                    
    return list_of_anagrams
            
def main():
    list_of_words = ['abc', 'cab', 'bac', 'lab', 'bal', 'alb']
    print(sort_anagrams(list_of_words))
    
if __name__ == "__main__":
    main()