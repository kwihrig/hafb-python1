"""
Learn about recursion - iterables, iterator objects, (light on memory)
Using the built-in
iter(): create an iterable object
next(): fetch the next element in the iterable object
"""


def main():
    """
    test function
    :return: none
    """
    iterable = ["spring", "summer", "fall", "winter"]
    iterator = iter(iterable) #give me an iterator
    print (type(iterator), iterator)
    print (next(iterator))
    print (next(iterator))
    print (next(iterator))
    print (next(iterator))


if __name__ == '__main__':
    main()
    exit(0)
