num = input("Enter three digits (each digit for one pig): ")
num1 = int(num) % 10
num2 = (int(num) // 10) % 10
num3 = int(num) // 100
sum = num1 + num2 + num3
print(sum)
print(sum // 3)
print(sum % 3)
The_Sum_Mithalek = sum % 3
print(not The_Sum_Mithalek)
