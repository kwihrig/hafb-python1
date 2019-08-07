"""
Learn list comprehensions
Readable, expressive, and effective.
"""
from math import factorial
from pprint import pprint as pp


def main():
    """
    test function
    :return: none
    """
    words = "Today I am very happy to learn about list comprehensions".split()
    print(words)
    data = []    # empty list
    for word in words:
        # Some analysis
        data.append(word)

    # "filter" data
    print (data)

    # Task: find the length in digits of the first 20 factorials
    info = [] #empty list
    for x in range(200):
        #print(factorial(x))
        info.append(len(str(factorial(x))))
    pp(info)
    #use a list comprehension: []
    info2 = [len(str(factorial(x))) for x in range(200)]
    pp(info2) # We tried pp with a second argument to print the type as well, as in
    # pp(info2, type(info2)), but pp doesn't take 2 arguments, only 1.

    # Set comprehensions: ()
    info3 = {len(str(factorial(x))) for x in range(200)}
    pp(info3)


if __name__ == '__main__':
    main()
    exit(0)
