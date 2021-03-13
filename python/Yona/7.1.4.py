def squared_numbers(start, stop):
    list = []
    while(start <= stop):
        list.append(start * start)
        start += 1
    return list