"""
Learn dictionaries
Dictionaries map keys to values
In some languages dictionaries are known as associative arrays or hashes, maps

Create them using {} containing a key-value pair.
Retrieve them by {key_value}
"""
d = {'alice': "801-123-45-8988",
     'pedro': '956-445-78-8966',
     'john': '651-321-66-4477'}
print (d, type(d))
# Access one element
print (d['pedro'])

# Add members to the dictionary, of names -> grades
roster={}      #Empty dictionary

# Ask user to enter 3 names, and add them to the list
total = 0
while total < 3:
    # Get key value
    name = input("enter a name\n")
    #Get value associated to key
    score = input("enter score\n")
    # Add element to dictionary.
    # Note: if key value exists, it will update the value otherwise it will be added to the dict.
    roster[name] = score
    total +=1
# display list
print(roster)