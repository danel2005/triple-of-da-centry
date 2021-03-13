def main():
    woman = {"first_name" : "Mariah", "last_name" : "Carey", "birth_date" : "27.03.1970", "hobbies" : ["Sing", "Compose", "Act"]}
    choice = int(input("Enter a number between 1 and 7: "))
    if choice == 1:
        print(woman["last_name"])
    elif choice == 2:
        print(woman["birth_date"][3:5])
    elif choice == 3:
        print(len(woman["hobbies"]))
    elif choice == 4:
        print(woman["hobbies"][-1])
    elif choice == 5:
        woman["hobbies"] += ["Cooking"]
    elif choice == 6:
        print((woman["birth_date"][0:2], woman["birth_date"][3:5], woman["birth_date"][6:]))
    elif choice == 7:
        woman["age"] = 50
        print(woman["age"])
    
    
if __name__ == "__main__":
    main()