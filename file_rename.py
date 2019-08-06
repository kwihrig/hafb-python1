"""
Rename files from a folder
Get "http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip"
"""
import os

def rename_files():
    """
    rename files in a folder
    :return: nothing
    """
    folder_dir = r"C:\Users\kevinihrig\Desktop\hafb\prankOrig"
    files = os.listdir(folder_dir)
    saved_path = os.getcwd()   # save current directory
    # go to the file directory
    os.chdir(folder_dir)
    for file in files:
        # remove digits from file name
        new_file = file.lstrip('2345678910')
        print("old name", file, "     new name", new_file)
        # Rename file to new name
        os.rename(file, new_file)
# go to the home directory
    os.chdir(saved_path)



def main():
    """
    test function
    :return: nothing
    """
    rename_files()



if __name__== '__main__':
    main()
    exit(0)