def main():
    str = input("Enter a string: ")
    items = str.split(",")
    for i in range(len(items)):
        items[i] = items[i].lower()
    choice = int(input("Enter a number: "))
    while choice != 9:
        if choice == 1:
            print(items)
            choice = int(input("Enter a number: "))
        elif choice == 2:
            print(len(items))
            choice = int(input("Enter a number: "))
        elif choice == 3:
            str = input("Entet an item: ")
            if str.lower() in items:
                print("True")
            else:
                print("False")
            choice = int(input("Enter a number: "))
        elif choice == 4:
            str = input("Enter an item: ")
            count = count_item(str, items)
            print("There is", count, str, "in the list")
            choice = int(input("Enter a number: "))
        elif choice == 5:
            str = input("Enter an item: ")
            if str.lower() in items:
                items.remove(str.lower())
            choice = int(input("Enter a number: "))
        elif choice == 6:
            str = input("Enter an item: ")
            items += [str.lower()]
            choice = int(input("Enter a number: "))
        elif choice == 7:
            for item in items:
                if len(item) < 3:
                    print(item.upper())
                for letter in item:
                    if not (letter >= "a" and letter <= "z" or letter >= "A" and letter <= "Z"):
                        print(item.upper())
            choice = int(input("Enter a number: "))
        elif choice == 8:
            for item in items:
                while count_item(item,items) > 1:
                    items.remove(item)
            choice = int(input("Enter a number: "))
    
def count_item(item_name, items):
    count = 0
    for item in items:
        if item == item_name.lower():
            count += 1
    return count
    
if __name__ == "__main__":
    main()