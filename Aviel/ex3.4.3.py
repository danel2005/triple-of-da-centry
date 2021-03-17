str = input("Please enter a string: ")
middle = len(str) // 2
print(str[:middle].lower() + str[middle:].upper())
