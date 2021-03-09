def distance(num1, num2, num3):
    import math
    one_to_two = abs(num1 - num2)
    two_to_three = abs(num2 - num3)
    one_to_three = abs(num1 - num3)
    
    if((one_to_three <= 1) or (one_to_two <= 1)):
        if(((one_to_two >= 2) and (two_to_three >= 2)) or ((one_to_three >= 2) and (two_to_three >= 2))):
            return 1
    return 0