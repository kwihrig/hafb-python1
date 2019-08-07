"""
Learn about exceptions
when an exception is found, normal flow of program is interrupted

"""

import sys

def convert(s):
    """
    converts a string to integer
    :param s:
    :return:
    """
#    x = -1


    try:
 #       x = int(s)
        return int(s)
    except (ValueError, TypeError) as e:
        print("conversion error{}"\
              .format(str(e)), file=sys.stderr)
    return -1

def main():
    """
    test function
    :return: none
    """

    print (convert("11"))
    print (convert("hello"))
    print (convert([1, 4, 8]))



if __name__ == '__main__':
    main()
    exit(0)
