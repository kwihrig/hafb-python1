"""
To count words in a file
Also counts occurrences of individual words
"""
from urllib.request import urlopen

def fetch_words(filename):
    """
    Count words in url file
    :param filename: url to file
    Fetch the words from a file on the web
    :return: a list with the items
    """
    count = 0
    data = []           # Empty list
    with urlopen(filename) as story: # story is the variable for the text in the file
        for line in story:
           words = line.decode('utf-8').split() #split line into words using space as default separator
#           print(words)
           for word in words:
               data.append(word)
    return data

def print_items(items):
    """
    Print elements of the collection
    :param items: a collection of objects
    :return: nothing
    """
    for item in items:
        print(item)



def main():
    """
    test function for words library
    :return: nothing
    """
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_words(file)
    print_items(words)

if __name__== '__main__':
    main()
    exit(0)
