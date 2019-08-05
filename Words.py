"""
Get a file from the web:
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: count number of words in document
"""
from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

count = 0
data = {}           # Empty dictionary
with urlopen(file) as story:
    for line in story:
       words = line.decode('utf-8').split() #split with space as default
#       print(words)
       for word in words:
           if word in data:
               data[word] += 1
           else:
               data[word] = 1
           count += 1
print ("Total number of words ", count)
print ("Total data ", data)


