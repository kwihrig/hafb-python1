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
    for file in files:
        new_file = file.lstrip('0123456789')
        print("old name", file, "     new name", new_file)



def main():
    """
    test function
    :return: nothing
    """
    rename_files()



if __name__== '__main__':
    main()
    exit(0)