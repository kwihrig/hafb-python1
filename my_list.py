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






if __name__ == '__main__':
    main()
    exit(0)
