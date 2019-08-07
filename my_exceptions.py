"""
Learn about exceptions
when an exception is found, normal flow of program is interrupted

"""


def convert (s):
    """
    converts a string to integer
    :param s:
    :return:
    """
    try:
        x = int(s)
    except ValueError:
        print("conversion failed!")
        x = -1
    return x

def main():
    """
    test function
    :return: none
    """

    print (convert("11"))
    print (convert("hello"))



if __name__ == '__main__':
    main()
    exit(0)
