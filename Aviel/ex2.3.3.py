num = input("Enter three digits (each digit for one pig): ")
num = int(num)
sum = num % 10 + num // 10 % 10 + num // 100
print(sum)
print(sum // 3)
print(sum % 3)
print(sum % 3 == 0)