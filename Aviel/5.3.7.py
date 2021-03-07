def chocolate_maker(small, big, x):
    num = x - small - big * 5
    if num > 0:
        return False
    elif num == 0:
        return True
    elif abs(num) <= small:
        return True
    elif (abs(num) % 5) <= small and abs(num) - (abs(num) % 5) <= big * 5 + (small - (abs(num) % 5)):
        return True
    return False
    