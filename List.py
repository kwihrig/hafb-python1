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