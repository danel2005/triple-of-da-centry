tempStr = input("Insert the temperature you would like to convert: ")
temp = 0.0
if tempStr[-1] == "c" or tempStr[-1] == "C":
    temp = float(tempStr[:-1])
    temp = (9 * temp + (32 * 5)) / 5
    print(str(temp) + "F")
elif tempStr[-1] == "f" or tempStr[-1] == "F":
    temp = float(tempStr[:-1])
    temp = (5 * temp - 160) / 9
    print(str(temp) + "C")
