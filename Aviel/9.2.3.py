def who_is_missing(file_name):
    """
    Find the missing number in the text file, return it as an int and create a new file and write the number there
    :param file_name: path to a text file
    :type file_name: str
    :return: the missing number
    :rtype: int
    """
    nums = []
    missing_num = 0
    with open(file_name,"r") as file_input:
        nums = file_input.read().replace("\n", "").split(",")
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        if (i > 0) and not (nums[i] == nums[i - 1] + 1):
            missing_num = nums[i] - 1
            break
    if len(nums) == 1:
        missing_num = nums[0] - 1
    with open(r"e:\found.txt", "w") as file_missing_num:
        file_missing_num.write(str(missing_num))
    return missing_num 
    
    
def main():
    print(who_is_missing(r"e:\findMe.txt"))
    
if __name__ == "__main__":
    main()