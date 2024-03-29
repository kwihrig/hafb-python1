"""
Learn about range() collectionsas
"""


def main():
    """
    test function
    :return: none
    """
    
    #Default
    for i in range(5):
        print(i)
        
# Set the initial value
    print("Now setting initial value ")
    for i in range(5, 10):
        print(i)
        
# Create a list from range
    l = list(range(5, 10))
    print(l, type (l))
    l2 = list(range(5,10)) + list(range(30,40))
    print(l2, type(l2))
# Step arguement: (begin, stop step)
    l3 = list(range(0,20,2))
    print(l3, type(l3))
    #iterationover list using index notation
    s=[0,2,4,6]
    for i in range(len(s)):
            print(s[i])
# better way
    for v in s:
        print(v)

# enumerate(): return iterable series
    t = [6, 789, 128, 98, 3, 22]
    for p in enumerate(t):
        print (p, p[0], p[1])
    # a better way
    for i, v in enumerate(t):
        print ("i = {}, v={}".format(i, v))



if __name__ == '__main__':
    main()
    exit(0)
