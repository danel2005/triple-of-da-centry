def my_mp3_playlist(file_path):
    """
    Finds the name of the longest song, count hopw many songs there is in the file, checks which singer appear the most in the file
    :param file_path: the path to the file
    :type file_path: str
    :return: the name of the longest song in the file, the number of songs in the file, name of the singer that that appear the most amont of time
    :rtype: tuple
    """
    songs = []
    songs_items = []
    songs_dict = {}
    name_of_long_song = ""
    num_of_songs = 0
    name_of_singer = ""
    max_time = [0,0]
    singers_dict = {}
    max_appear = 0
    with open(file_path, "r") as file_input:
        songs = file_input.read().split("\n")
        
    for song in songs:
        songs_items += [song.split(";")]
        
    for item in songs_items:
        songs_dict[item[0]] = item[1:-1]
        
    songs_dict.pop("",None)
    for key, value in songs_dict.items():
        num_of_songs += 1
        time = value[1].split(":")
        for i in range(len(time)):
            time[i] = int(time[i])
        if time[0] > max_time[0]:
            max_time[0] = time[0]
            max_time[1] = time[1]
            name_of_long_song = key
        elif time[0] == max_time[0] and time[1] > max_time[1]:
            max_time[1] = time[1]
            name_of_long_song = key
        if value[0] in singers_dict.keys():
            singers_dict[value[0]] += 1
        else:
            singers_dict[value[0]] = 1
    for key, value in singers_dict.items():
        if value > max_appear:
            max_appear = value
            name_of_singer = key
    
    return (name_of_long_song, num_of_songs, name_of_singer)
    
def main():
    print(my_mp3_playlist(r"e:\songs-long.txt"))
    
if __name__ == "__main__":
    main()