str = input("Enter string: ")
str = str.lower()
str = str.replace(" ", "")
backStr = str[::-1]
if str == backStr:
    print("OK")
else:
    print("NOT")