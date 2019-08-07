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







if __name__ == '__main__':
    main()
    exit(0)
