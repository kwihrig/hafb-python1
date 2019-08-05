"""
Learn about lists
Unlike strings, lists are mutable
You can update and append elements to it
"""

# use brackets to define lists
l=[1, 2, 3]
print ("List ", l, type (l))
# A list of objects (any type)
a = ["apple", "orange", "pear"]
# Access by index notation
print (a, a[0])
print (a, a[1])
# Replace an element
a[0] = "tomatoes"
print (a, a[1])
a[1] = "3.14"
print (a, a[1])

# Begin with an empty list
# names = []
# names = input("Enter your name")
names = []
# Ask user to enter 3 names, and add them to the list
total = 0
while total < 3:
    name = input("enter a name\n")
    names.append(name)
    total = total+1
# display list
print(names)