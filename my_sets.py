"""
Learn about sets
an unordered collection of unique, immutable objects
Define it using {} but no key needed
You can use the set constructor to make one
"""


def main():
    """
    test function
    :return: none
    """
    p={6, 78, 21, 45}
    print(p, type(p))
    data = [1, 3, 5, 2, 88, 3, 1]
    print(data, type(data))
    # eliminated dups
    sdata = set(data)
    print(sdata, type(sdata))




if __name__ == '__main__':
    main()
    exit(0)