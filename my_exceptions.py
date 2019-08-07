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


def sqrt(x):
    """
    compute the square root using method of Heron of Alexandria
    :param x: number to compute sqrt
    :return: sqrt of x
    :raise ValueError() on ZeroDivisionError
    """
    guess = x
    i = 0
    try:
        while guess*guess != x and i< 20:
            guess = (guess + x/guess)/2.0
            i +=1
    except ZeroDivisionError:
        raise ValueError()

    return guess


def main():
    """
    test function
    :return: none
    """

   # print (convert("11"))
    #print (convert("hello"))
   # print (convert([1, 4, 8]))

    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
        print(sqrt(100))
        print(sqrt(256))
        print(sqrt(255))
    except ValueError:
        print("Cannot compute")

    print("Done")






if __name__ == '__main__':
    main()
    exit(0)
