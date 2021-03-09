def chocolate_maker(small, big, x):
    if(small >= 5):
        minus = x % 5
        small = small - minus
        big = big + (small // 5)
        small = small % 5
        small = small + minus
 
    if((x % 5 > small) or (x // 5 > big)):
        return 0
    else:
        return 1