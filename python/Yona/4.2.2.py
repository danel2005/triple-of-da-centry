string = input("Enter string to check philandrom: ")
string = string.replace(" ", "")
string = string.lower()
print(string)
print (string[ : :-1])
if(string == string[ : :-1]):
    print("OK")
else:
    print("NOT")