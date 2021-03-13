def sort_prices(list_of_tuples):
    """
    Sorting a list of tuples by the item price 
    :param list_of_tuples: the list of items
    :type item: list
    :return: the list of the items sorted from the bigest price item to the lowest
    :rtype: list
    """
    list_of_tuples.sort(key = get_price, reverse = True)
    return list_of_tuples
    
def get_price(item):
    """
    Returning the price of an item
    :param item: the item we cheking his price
    :type item: tuple
    :return: the price of the item
    :rtype: float
    """
    return float(item[1])
    
def main():
    products = [("milk", "5.5"), ("candy", "2.5"), ("bread", "9.0")]
    print(sort_prices(products))
    
if __name__ == "__main__":
    main()