from mutagen.id3 import ID3, TIT2, TPE1  # Importing classes to read and modify ID3 tags in MP3 files
import os  # Importing the `os` module for file and directory operations

def soundscrape_tags(directory):
    """
    This function processes all MP3 files in a specified directory. 
    It extracts artist and title information from the filename, updates the ID3 tags,
    and renames the files accordingly.
    
    Parameters:
        directory (str): Path to the directory containing MP3 files to edit.
    """
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):  # Process only MP3 files
            # Load the ID3 tags of the MP3 file
            audio = ID3(os.path.join(directory, filename))

            # Split the filename into parts using " - " as a delimiter
            filename_split = list(filename.split(" - "))

            # Extract the artist and title from the filename
            artist = filename_split[1].strip()  # Assuming the second part is the artist
            title = filename_split[-1].strip()[:-4]  # Assuming the last part (without '.mp3') is the title

            # Update the ID3 tags for artist and title
            audio['TPE1'] = TPE1(encoding=3, text=artist)  # TPE1 is the ID3 tag for artist
            audio["TIT2"] = TIT2(encoding=3, text=title)  # TIT2 is the ID3 tag for title

            # Save the updated ID3 tags back to the MP3 file
            audio.save(os.path.join(directory, filename))

            # Rename the file using the extracted artist and title
            new_name = str(artist) + " - " + str(title) + ".mp3"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

            print(f"Edited and renamed: {filename} -> {new_name}")

# Prompt the user to input the directory containing MP3 files
directory = input("Please enter path with MP3 files to edit: ")

# Call the function to process the files
soundscrape_tags(directory)
