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
    """
    guess = x
    i = 0
    while guess*guess != x and i< 20:
        guess = (guess + x/guess)/2.0
        i +=1

    return guess


def main():
    """
    test function
    :return: none
    """

   # print (convert("11"))
    #print (convert("hello"))
   # print (convert([1, 4, 8]))

    print(sqrt(9))
    print(sqrt(11))
    print(sqrt(-3))
    print(sqrt(100))
    print(sqrt(256))
    print(sqrt(255))






if __name__ == '__main__':
    main()
    exit(0)
