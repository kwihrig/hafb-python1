"""
To count words in a file
ALso counts occurrences of individual words
"""
from urllib.request import urlopen

file = "filename"

def fetch_words()
    """
    Fetch the words from a file on the web
    :return: 
    """
    count = 0
    data = {}           # Empty dictionary
    with urlopen(file) as story: # story is the variable for the text in the file
        for line in story:
           words = line.decode('utf-8').split() #split line into words using space as default separator
#           print(words)
           for word in words:
               if word in data:
                   data[word] += 1
               else:
                   data[word] = 1
               count += 1
print ("Total number of words ", count)
print ("Total data ", data)

