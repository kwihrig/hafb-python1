"""
Learn list comprehensions
Readable, expressive, and effective.
"""


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
        print (word)


if __name__ == '__main__':
    main()
    exit(0)
