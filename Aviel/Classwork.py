def main():
    password = input("Please enter a password: ")
    len_grade = check_length(password)
    varity_grade = check_varity(password)
    common_grade = check_common(password)
    avarage = (len_grade + varity_grade + common_grade) / 3
    print(f"Score: {avarage} - " ,end="")
    if (avarage) >= 0 and (avarage) <= 3:
        print("Weak")
    elif (avarage >= 4) and (avarage) <= 6:
        print("Medium")
    elif (avarage) >= 7 and (avarage) <= 8:
        print("Strong")
    elif (avarage) >= 9 and (avarage) <= 10:
        print("Verry Strong")
        
def check_length(password):
    password_length = len(password)
    if (password_length <= 4):
        return 0
    elif (password_length >= 5 and password_length <= 7):
        return 5
    else:
        return 10
        
def check_varity(password):
    numbers_included = 
    lower_letters = password.islower()
    upper_letters = password.isupper()
    signs = not password.isalnum()
    if numbers_included and lower_letters and upper_letters and signs:
        return 10
    elif numbers_included and lower_letters and upper_letters:
        print("varity is working")
        return 7
    elif numbers_included and lower_letters:
        return 5
    elif lower_letters or upper_letters:
        return 3
    else:
        return 0

def check_common(password):
    if password.lower() == "password" or password.lower() == "love" or password.lower() == "qwerty" or password.lower() == "abc":
        return 0
    else:
        return 10
    
    
if __name__ == "__main__":
    main()
    