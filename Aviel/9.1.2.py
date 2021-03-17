def main():
    file_path = input("Enter a file path: ")
    task = input("Enter a task: ")
    if task.lower() == "sort":
        sort(file_path)
        print("\n")
    elif task.lower() == "rev":
        rev(file_path)
        print("\n")
    elif task.lower() == "last":
        last(file_path)
        print("\n")
    
    
def rev(file_path):
    file_input = open(file_path, "r")
    for line in file_input:
        print(line[::-1])
    file_input.close()
    
def sort(file_path):
    file_input = open(file_path, "r")
    file_contant = file_input.read()
    file_contant.replace("\n", " ")
    words = file_contant.split()
    words = list(dict.fromkeys(words))
    words.sort()
    print(words)
    file_input.close() 
    
def last(file_path):
    n = int(input("Enter a number: "))
    file_input = open(file_path, "r")
    lines = file_input.readlines()
    for i in range(len(lines) - n, len(lines)):
        print(lines[i])
    file_input.close()
    
    
if __name__ == "__main__":
    main()