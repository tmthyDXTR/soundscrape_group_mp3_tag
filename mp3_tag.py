from mutagen.id3 import ID3, TIT2, TPE1
import os

def soundscrape_tags(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            audio = ID3(os.path.join(directory, filename))
            filename_split = list(filename.split(" - "))
            artist = filename_split[1].strip()
            title = filename_split[-1].strip()[:-4]
            audio['TPE1'] = TPE1(encoding=3, text=artist)
            audio["TIT2"] = TIT2(encoding=3, text=title)

            audio.save(os.path.join(directory, filename))
            new_name = str(artist) + " - " + str(title) + ".mp3"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print("mp3 edited")
directory = input("Please enter path with mp3 files to edit: ")

soundscrape_tags(directory)