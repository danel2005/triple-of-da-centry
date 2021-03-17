def my_mp4_playlist(file_path, new_song):
    """
    Writing the name of the new song instead of the name of the song in the third row
    :param file_path: the path to the file
    :param new_song: name of a new song
    :type file_path: str
    :type new_song: str
    :return: none
    """
    with open(file_path, "r") as file_input:
        lines = file_input.readlines()
    if len(lines) < 3:
        while len(lines) < 2:
            lines += ["\n"]
        lines += [new_song + ";"]
    else:
        str = ""
        line3_items = lines[2].split(";")
        line3_items[0] = new_song
        for item in line3_items:
            if not item == "\n":
                str += item + ";"
            else:
                str += item
        lines[2] = str
    with open(file_path, "w") as writing_file:
        str = ""
        for line in lines:
            str += line
        writing_file.write(str)
        
    with open(file_path,"r") as file_input:
        print(file_input.read())
    
def main():
    my_mp4_playlist(r"e:\songs-long.txt", "Python Love Story")
    
if __name__ == "__main__":
    main()