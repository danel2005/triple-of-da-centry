def fix_age(age):
    if((age >= 13) and (age <= 19) and (age != 16) and (age != 15)):
        age = 0
    return age

def filter_teens(a = 13, b = 13, c = 13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    sum_ages = a + b + c
    return sum_ages

