def are_files_equal(file1, file2):
    """
    Checks if two files are the same
    :param file1: the path to the file in the PC
    :param file2: the path to the file in the PC
    :type file1: str
    :type file2: str
    :retrun: if the files are the same
    :rtype: bool
    """
    same = False
    file_input1 = open(file1,"r")
    file_input2 = open(file2, "r")
    file1_contant = file_input1.read()
    file2_contant = file_input2.read()
    if file1_contant == file2_contant:
        same = True
    file_input1.close()
    file_input2.close()
    return same