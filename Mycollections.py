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
    print(t2, type(t2))
    #tuple constructor: tuple()
    t_from_l = tuple([3, 77, 11])
    print (t_from_l, type(t_from_l))
    #test for membership
    print(5 in (3, 6, 8, 5, 12))
    print(5 not in (3, 6, 8, 5, 12))


def min_max(items):
    """
    return min adn max elements of a collection
    :param items: collection
    :return: min and max
    """
    return min(items), max (items)

def swap(obj1, obj2):
    """
    Swap values of the objects
    :param obj1: first
    :param obj2: second
    :return: values swapped
    """
    return obj2, obj1


def main():
    """
    test function
    :return: none
    """
    do_tuples()
    # output = min_max ([56,76,11,12,90])
    #
    # print("min", output[0])
    # print("max", output[1])
    # #tuple unpacking
    # lower, upper = min_max([56, 76, 11, 12, 90])
    # print("min", lower)
    # print("max", upper)
    # #Swap values
    # a = "jelly"
    # b = "bean"
    # print(a,b)
    # # call you function
    # a, b = swap(a,b)
    # print(a,b)
    # a, b = b, a
    # print(a,b)





if __name__ == '__main__':
    main()
    exit(0)
