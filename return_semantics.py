"""
File Info Here
"""

def egg(var):
    """
    dummy function returns variable back to user
    :param var: input object
    :return: input object
    """
    return var

# Req'd parameters must come first
# Optional parameters after req'd parameters
def sum_two(num1, num2=8):
    """
    sum 2 input integer objects
    :param num1: object 1
    :param num2: object 2 (optional), default is = 8
    :return: sum of objects
    """
    total = num1 + num2
    print(num1," + ", num2, " = ", total)
    return num1 + num2


def banner(message, border='*'):
    """
    print message in banner form
    :param message: string to print
    :param border: border character for string
    :return:
    """

    #print("Enter a string")
    #response = input()  # take user input


    print(border*len(message))
    print(message)
    print(border * len(message))


def banner1(message, border='*'):
    """
    print message in banner form
    :param message: string to print
    :param border: border character for string
    :return:
    """

    #print("Enter a string")
    #response = input()  # take user input


    print("*", border*len(message), "*")
    print("*", message, "*")
    print("*", border * len(message), "*")

def main():
    """
    test function
    :return: none
    """

    c = [6,10,20]
    e = egg(c)
    print (c is e)
    n1 = 3
    n2 = 9
    sum_two(n1, n2)
    sum_two(n1)

    print("Only one input", sum_two(n1))

    banner("Weber State")
    banner("WeberState University", "$")

    banner("Weber State")
    banner("Weber State University", "$")

if __name__== '__main__':
        main()
        exit(0)
