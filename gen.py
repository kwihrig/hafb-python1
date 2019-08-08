"""
Learn about generator functions - Module for demonstratoin of the use of generator execution

"""



def take(count, iterable):
    """
    Take items from the fron of an iterable
    :param count: The max number of items to retrieve
    :param iterable: source series
    :yields: at most 'count' items for 'iterable'
    """

    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def run_take():
    """
    test the take() funct
    """
    items = [2, 4, 6, 8, 10]
    for item in take(11, items):
        print(item)

def distinct(iterable):
    """
    return unique utems by eliminating dups
    :param iterable: the source series
    :yields: unique elements in order from 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue # takes you back to the top of the loop block
        yield item
        seen.add(item)
#        print(item)

    # yield 1
    # yield 2
    # yield 3

# def gen246():
#     print("About to yield 2")
#     yield 2
#     print("About to yield 4")
#     yield 4
#     print("About to yield 6")
#     yield 6
#     print("About to return")



def main():
    """
    test function
    :return: none
    """
    run_take()
#    print("Done")


if __name__ == '__main__':
    main()
    exit(0)