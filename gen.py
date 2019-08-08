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
#        print(seen)


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


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)

def run_distinct():
    items = [5, 7, 7, 6, 5, 5, 8, 12, 1234567]
    for item in distinct(items):
        print(item)


def main():
    """
    test function
    :return: none
    """
#    run_take()
#    run_distinct()
    run_pipeline()
#    print("Done")


if __name__ == '__main__':
    main()
    exit(0)