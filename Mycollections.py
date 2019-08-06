"""
File learn about collectoin: Tuples, Strings, range, List, Dictionaries, Sets
"""


def do_tuples():
    """
    practice tuples
    :return: none
    """
    #Immutable sequence of arbitrary objects
    # Use() to define a tuple
    t=("Odgen", 1.99, 2)
    print(t,type(t))
    print("Size ", len(t))
    print("One member:", t[0])
    # To iterate over a tuple
    for item in t:
        print (item)

    # Single tuples, must end with comma
    t1 = (6,)
    print(t1, type(t1))
# another wa to create tuples
    # Parentheses are optional
    t2 = 1, 2, 3, 5

def main():
    """
    test function
    :return: none
    """
    do_tuples()


if __name__ == '__main__':
    main()
    exit(0)
