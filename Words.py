"""
Get a file from the web:
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: count number of words in document
"""
from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

count = 0
with urlopen(file) as story:
    for line in story:
       words = line.decode('utf-8').split() #split with space as default
#       print(words)
       for word in words:
           count += 1
print ("Total number of words ", count)

