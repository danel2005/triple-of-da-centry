temp_with_char = input("Insert the temperature you would like to convert: ")
char = temp_with_char[-1]
char = char.lower()
temp = temp_with_char[0:-1]
int_temp = float(temp)
if(char == "f"):
    print((5 * int_temp - 160) / 9)
elif(char == "c"):
    print((9 * int_temp + 160) / 5)
else:
    print("There is a problem!")