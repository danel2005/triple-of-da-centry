def copy_file_content(source, destination):
    """
    The function copy the content of the source file and paste it in the destination file
    :param source: the path to the source file
    :param destination: the path to the destination file
    :type source: str
    :type destination: str
    :return: none
    """
    content = ""
    with open(source, "r") as source_input_file:
        content = source_input_file.read()
    with open(destination, "w") as destination_file:
        destination_file.write(content)