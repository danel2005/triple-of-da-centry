str = input("Please enter a string: ")
first_letter_d = str.find("d")
print(str[:first_letter_d + 1] + str.replace("d", "e")[first_letter_d + 1::])