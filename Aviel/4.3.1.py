str = input("Guess a letter: ")
if len(str) > 1 and not(str >= "a" and str <= "z" or str >= "A" and str <= "Z"):
    print("E3")
elif len(str) > 1:
    print("E1")
elif not(str >= "a" and str <= "z" or str >= "A" and str <= "Z"):
    print("E2")
else:
    print(str.lower())