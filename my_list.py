"""
Learn about list()
"""





def main():
    """
    test function
    :return: none
    """
    s = "show how to do it".split()
    print(s, type(s))
    #access by index
    print("s[3]", s[3])
    print("last member:", s[len(s) - 1]) # very un-Pythonic
    # Use negative index
    print("s[-1]:", s[-1])
    # slicing
    print(s, type(s))
    print("from first to one before the last member", s[1:-1])
    print("from first to three members", s[1:3])
    print("from first to three members, another way", s[1:-2])
    print("from 1 to the end", s[1:])
    print("from beg to three members", s[:3])
    print("all, from beg to end, whole list", s[:])
#make a copy of the list
    t=s #this defines t and s as the same list. redefine either one, both change - this is a shallow copy.
    print("s: ", s)
    print("t: ", t)
    print("t is s", t is s)
    t = s[:] # this is a deep copy - t is defined as the contents of s right now. we have made a copy of the data in t, s is still its own list
    # or this t = s.copy()
    # or this t = list(s)
    print("t is s", t is s)
    print("t == s", t == s)

    # shallow copies
    # A list of lists
    a = [[1,2], [3,4]]
    print(a, type(a))
    print("a[0][1]: ", a[0][1])
#copy the list of lists
    b = a[:]
    a[0] = [8,9]
    print("change a[0] to [8, 9]")
    print("b is a", b is a)
    print("a[0]: ", a[0])
    print("b[0]: ", b[0])
    print("a[0] is b[0] ", a[0] is b[0])
    print("a[1] is b[1] ", a[1] is b[1])
    #modify a[1]
    a[1].append(5)
    print("a[1]: ", a[1])
    print("b[1]: ", b[1])
    print("a[0] is b[0] ", a[0] is b[0])
    print("a[1] is b[1] ", a[1] is b[1])
    print("a: ", a)
    print("b: ", b)
    #repetition
    c = [21, 37]
    d = c * 4
    print("c ", c)
    print("d", d)
    s = [[-1, 1]]*5
    print(s)
    s[1].append(7)
    print(s)
    # index ()
    w = "the quick brown fox jumps over the lazy dog".split()
    i = w.index('fox')
    print("The index of 'fox' entry is:", i, w[i])
# if no index is found, it will throw a ValueError
#    i = w.index('cat')
#    print("The index of 'cat' entry is:", i, w[i])

# Membership testing with: count()
    print("'The' value is ", w.count("the"))
    # also test membership with : in, not in
    print(37 in [12, 22, 37, 99])
    print(78 not in [12, 22, 37, 99])






    #a= [[123,456], [444,888]]
    #print("a: ", a, type(a))










if __name__ == '__main__':
    main()
    exit(0)
